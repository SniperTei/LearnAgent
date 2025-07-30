from pydantic_ai.models.gemini import GeminiModel
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# 打印环境变量
print("gemini api key:", os.getenv("GEMINI_API_KEY"))
# Initialize the Gemini model
gemini_model = GeminiModel(model_name='gemini-2.0-flash')