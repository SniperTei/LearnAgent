from pydantic import BaseModel, Field
from pydantic_ai import Agent, Tool
from pydantic_ai.models.gemini import GeminiModel
from dotenv import load_dotenv
# from pydantic_ai.common_tools.duckduckgo import duckduckgo_search_tool
# from pydantic_ai.common_tools.tavily import tavily_search_tool
from duckduckgo_search import DDGS
from typing import List
import time

load_dotenv()

class SearchResult(BaseModel):
    title: str = Field(description="Page title")
    url: str = Field(description="Page URL")
    snippet: str = Field(description="Page snippet")

@Tool
def search_duckduckgo(query: str) -> List[SearchResult]:
    for attempt in range(3):  # Retry up to 3 times
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=5))
            return [SearchResult(title=r['title'], url=r['href'], snippet=r['body']) for r in results]
        except Exception as e:
            if 'ratelimit' in str(e).lower():
                print(f"Rate limit hit, retrying in {2 ** attempt} seconds...")
                time.sleep(2 ** attempt)  # Exponential backoff: 1s, 2s, 4s
            else:
                raise e
    raise Exception("Failed after retries due to rate limit")

class SearchAgent:
    def __init__(self):
        self.model = GeminiModel("gemini-2.5-flash")
        self.agent = Agent(
            self.model,
            system_prompt='Search DuckDuckGo and return structured results.',
            tools=[search_duckduckgo]
        )


    def search(self, query: str):
        result = self.agent.run_sync(query)
        return result
    
def main():
    search_agent = SearchAgent()
    print("欢迎使用搜索助手！输入 'exit' 退出。")
    while True:
        user_input = input("你：")
        if user_input.strip().lower() in ["exit", "quit", "退出"]:
            print("再见！")
            break
        result = search_agent.search(user_input)
        print("AI：", result.output)

if __name__ == "__main__":
    main()