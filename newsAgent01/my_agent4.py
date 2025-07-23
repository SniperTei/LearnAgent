from typing import Optional, List
from pydantic import BaseModel, Field
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai import Agent, Tool

from dotenv import load_dotenv
from data_tool import get_movie_by_id, get_movies_by_star

load_dotenv()
model = GeminiModel("gemini-2.5-flash")
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

@Tool
def tool_get_movie_by_id(movie_id: str) -> dict:
    """根据电影id获取电影数据"""
    return get_movie_by_id(movie_id)

@Tool
def tool_get_movies_by_star(star_name: str) -> list:
    """根据电影明星姓名获取所有相关电影数据"""
    return get_movies_by_star(star_name)

# 带有结构化输出和依赖项的代理
agent = Agent(
    model=model,
    system_prompt=(
        "你是我的movie_manager。"
        "当我说电影id时，帮我查找对应电影；"
        "当我说明星名字时，帮我查找所有他/她参演的电影。"
        "直接调用工具获取数据并用中文简明回复。"
    ),
    tools=[tool_get_movie_by_id, tool_get_movies_by_star],
    result_type=str,
    retries=3,
)

# 示例用法
if __name__ == "__main__":
    print("welcome! please input 'exit' to exit")
    while True:
        user_input = input("You：")
        if user_input.strip().lower() in ["exit", "quit", "退出"]:
            print("good bye！")
            break
        result = agent.run_sync(user_input)
        print("AI:", result.output)
