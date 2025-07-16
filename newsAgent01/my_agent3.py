from pydantic import BaseModel, Field
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai import Agent

from dotenv import load_dotenv

load_dotenv()
model = GeminiModel("gemini-2.0-flash")

# --------------------------------------------------------------
# 3. 带有结构化响应的代理
# --------------------------------------------------------------
"""
这个示例展示了如何从代理获得结构化、类型安全的响应。
关键概念：
- 使用 Pydantic 模型定义响应结构
- 类型验证和安全性
- 字段描述，以便模型更好地理解
"""

class ResponseModel(BaseModel):
    """带有元数据的结构化响应。"""
    response: str
    needs_escalation: bool
    follow_up_required: bool
    sentiment: str = Field(description="Customer sentiment analysis")

# demo3
agent = Agent(model,
              system_prompt="You are an intelligent customer support agent. "
                            "Analyze queries carefully and provide structured responses.",
              result_type=ResponseModel)

result = agent.run_sync("I'm having trouble with my account. Can you help me?")
print(result.output)