from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from dotenv import load_dotenv
import requests
import os

load_dotenv()

model = GeminiModel("gemini-2.5-flash-preview-04-17")

agent = Agent(
    model,
    system_prompt="You are my lover",
    result_type=str
)

result = agent.run_sync("Who are you")
print(result.output)