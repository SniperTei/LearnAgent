from typing import Optional, List, Dict
from pydantic import BaseModel, Field
from pydantic_ai import Agent, ModelRetry, RunContext, Tool
from pydantic_ai.models.gemini import GeminiModel
from dotenv import load_dotenv
# --------------------------------------------------------------
# 5. 带有工具的代理
# --------------------------------------------------------------

"""
这个示例展示了如何使用自定义工具增强代理的功能。
关键概念：
- 创建和注册工具
- 在工具中访问上下文
"""

load_dotenv()
model = GeminiModel(
    "gemini-2.5-flash-preview-04-17"
)

shipping_info_db: Dict[str, str] = {
    "12345": "Shipped on 2024-12-01",
    "67890": "Out for delivery",
}

# 定义订单 schema (与前例相同)
class Order(BaseModel):
    """订单详情的结构。"""
    order_id: str
    status: str
    items: List[str]

# 定义客户 schema (与前例相同)
class CustomerDetails(BaseModel):
    """传入的客户查询的结构。"""
    customer_id: str
    name: str
    email: str
    orders: Optional[List[Order]] = None

class ResponseModel(BaseModel):
    """带有元数据的结构化响应。"""
    response: str
    needs_escalation: bool
    follow_up_required: bool
    sentiment: str = Field(description="Customer sentiment analysis")

customer = CustomerDetails(
    customer_id="1",
    name="John Doe",
    email="john.doe@example.com",
    orders=[
        Order(order_id="12345", status="shipped", items=["Blue Jeans", "T-Shirt"]),
    ],
)

def get_shipping_info(ctx: RunContext[CustomerDetails]) -> str:
    """获取客户的物流信息。"""
    return shipping_info_db[ctx.deps.orders[0].order_id]

# 带有结构化输出和依赖项的代理
agent5 = Agent(
    model=model,
    result_type=ResponseModel,
    deps_type=CustomerDetails,
    retries=3,
    system_prompt=(
        "You are an intelligent customer support agent. "
        "Analyze queries carefully and provide structured responses. "
        "Use tools to look up relevant information."
        "Always great the customer and provide a helpful response." # 原文笔误，应为 greet
    ),  # 这些是在编写代码时已知的
    tools=[Tool(get_shipping_info, takes_ctx=True)],  # 通过 kwarg 添加工具
)

@agent5.system_prompt
async def add_customer_name(ctx: RunContext[CustomerDetails]) -> str:
    # 将客户信息转换为格式化的JSON字符串
    customer_json = ctx.deps.model_dump_json(indent=2)
    return f"""Customer Information (JSON format):{customer_json}"""

response = agent5.run_sync(
    user_prompt="What's the status of my last order?", deps=customer
)

response.all_messages()
print(response.output.model_dump_json(indent=2))

print(
    "Customer Details:\n"
    f"Name: {customer.name}\n"
    f"Email: {customer.email}\n\n"
    "Response Details:\n"
    f"{response.output.response}\n\n"
    "Status:\n"
    f"Follow-up Required: {response.output.follow_up_required}\n"
    f"Needs Escalation: {response.output.needs_escalation}"
)