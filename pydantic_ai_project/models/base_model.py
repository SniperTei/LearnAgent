from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class AIModel(BaseModel):
    """Base class for all AI models"""
    model_name: str = Field(..., description="Name of the AI model")
    model_type: str = Field(..., description="Type of the model (e.g., 'gpt', 'llama', 'claude')")
    api_key: Optional[str] = Field(None, description="API key for the model service")
    model_config: Dict[str, Any] = Field(default_factory=dict, description="Additional model configuration")

    async def generate_response(self, prompt: str) -> str:
        """Generate a response for the given prompt"""
        raise NotImplementedError("Subclasses must implement generate_response")

class GPTModel(AIModel):
    """OpenAI GPT model implementation"""
    def __init__(self, **data):
        super().__init__(**data)
        if self.model_type != 'gpt':
            raise ValueError("model_type must be 'gpt' for GPTModel")

    async def generate_response(self, prompt: str) -> str:
        # Implement OpenAI GPT API call here
        pass

class LlamaModel(AIModel):
    """Llama model implementation"""
    def __init__(self, **data):
        super().__init__(**data)
        if self.model_type != 'llama':
            raise ValueError("model_type must be 'llama' for LlamaModel")

    async def generate_response(self, prompt: str) -> str:
        # Implement Llama API call here
        pass