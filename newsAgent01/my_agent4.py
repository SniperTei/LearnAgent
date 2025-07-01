from typing import Optional, List
from pydantic import BaseModel, Field
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai import Agent

from dotenv import load_dotenv

load_dotenv()
model = GeminiModel("gemini-2.5-flash-preview-04-17")
# --------------------------------------------------------------
# 4. 带有结构化响应和依赖项的代理
# --------------------------------------------------------------
"""
这个示例展示了如何在代理中使用依赖项和上下文。
关键概念：
- 使用 Pydantic 定义复杂的数据模型
- 注入运行时依赖项
- 使用动态系统提示
"""

class Movie(BaseModel):
    """电影的结构。"""
    title: str
    year: int
    rating: float

class CustomerInfo(BaseModel):
    """个人信息。"""
    name: str
    email: str
    watch_history: Optional[List[Movie]] = None
    like_list: Optional[List[Movie]] = None

class ResponseModel(BaseModel):
    """带有元数据的结构化响应。"""
    response: str
    sentiment: str = Field(description="my sentiment after I see the movie")

# 添加基于依赖项的动态系统提示
@agent5.system_prompt
async def add_customer_name(ctx: RunContext[CustomerDetails]) -> str:
    return f"Customer details: {to_markdown(ctx.deps)}"

# 带有结构化输出和依赖项的代理
agent = Agent(
    model=model,
    result_type=ResponseModel,
    deps_type=CustomerInfo,
    retries=3,
    system_prompt=(
        "You are an intelligent customer movie manager. "
        "Analyze movies carefully and provide structured responses. "
        "Recommend movies to me based on my watch history and like list. "
        "You will receive customer information as a dependency. "
    ),
)
