from enum import Enum
from typing import Optional

from models.gemini_model import gemini_model
from models.qwen_model import qwen_model

class ModelType(Enum):
    GEMINI = "gemini"
    QWEN = "qwen"

class ModelFactory:
    @staticmethod
    def get_model(model_type: ModelType):
        """获取指定类型的模型实例

        Args:
            model_type (ModelType): 模型类型

        Returns:
            Model: 模型实例
        """
        if model_type == ModelType.GEMINI:
            return gemini_model
        elif model_type == ModelType.QWEN:
            return qwen_model
        else:
            raise ValueError(f"Unsupported model type: {model_type}")