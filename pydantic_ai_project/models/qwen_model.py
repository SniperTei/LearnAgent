from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIModel

qwen_provider = OpenAIProvider(
            base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
            api_key=os.getenv("QWEN_API_KEY")
            )
qwen_model = OpenAIModel(
            model_name='qwen-plus',
            provider=qwen_provider
            )