from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from dotenv import load_dotenv
from pydantic_ai.common_tools.tavily import tavily_search_tool

load_dotenv()

class SearchAgent:
    def __init__(self):
        self.model = GeminiModel("gemini-2.5-flash-preview-04-17")
        self.agent = Agent(self.model, 
                           system_prompt="You are a powerful search assistant.", 
                           tools=[tavily_search_tool()])


    def search(self, query: str):
        result = self.agent.run_sync(query)
        return result
    
def main():
    search_agent = SearchAgent()
    result = search_agent.search("What is the capital of in Japan?")
    print(result.output)

if __name__ == "__main__":
    main()