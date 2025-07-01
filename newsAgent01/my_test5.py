from typing import Optional, List
from pydantic import BaseModel, Field
from pydantic_ai import Agent, ModelRetry, RunContext, Tool
# from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.models.gemini import GeminiModel
# import nest_asyncio
from dotenv import load_dotenv


load_dotenv()
model = GeminiModel(
    "gemini-2.5-flash-preview-04-17"
)


# 定义订单 schema
class Order(BaseModel):
    """订单详情的结构。"""
    order_id: str
    status: str
    items: List[str]

# 定义客户 schema
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

# 带有结构化输出和依赖项的代理
agent5 = Agent(
    model=model,
    result_type=ResponseModel,
    deps_type=CustomerDetails,
    retries=5,  # 增加重试次数
    system_prompt=(
        "You are an intelligent customer support agent. "
        "Analyze queries carefully and provide structured responses. "
        "Always greet the customer and provide a helpful response."
    ),
)

# 添加基于依赖项的动态系统提示
@agent5.system_prompt
async def add_customer_name(ctx: RunContext[CustomerDetails]) -> str:
    # 将客户信息转换为格式化的JSON字符串
    customer_json = ctx.deps.model_dump_json(indent=2)
    return f"""Customer Information (JSON format):{customer_json}

Please use this customer information to provide personalized responses."""

customer = CustomerDetails(
    customer_id="1",
    name="John Doe",
    email="john.doe@example.com",
    orders=[
        Order(order_id="12345", status="shipped", items=["Blue Jeans", "T-Shirt"]),
    ],
)

try:
    response = agent5.run_sync(user_prompt="What did I order?", deps=customer)
    
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
    
except Exception as e:
    print(f"发生错误: {e}")
    print("请检查网络连接或稍后重试")