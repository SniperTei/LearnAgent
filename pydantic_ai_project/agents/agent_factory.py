from enum import Enum
from typing import Optional, List
from pydantic_ai import Agent, Tool

from models.model_factory import ModelFactory, ModelType
from tools.tool_factory import ToolFactory, ToolType

class AgentType(Enum):
    """agent枚举"""
    BASIC = "Basic"
    NEWES = "News"
    WEATHER = "Weather"
    FILE_MANAGER = "FileManager"
    SERVICE = "Service"
    # 可以添加更多agent

class AgentFactory:
    """agent工厂类,用于创建和管理不同类型的agent实例"""
    
    @classmethod
    def create_agent(cls, agent_type: AgentType, model_type: ModelType, tool_types: List[ToolType]) -> Agent:
        """创建agent实例"""
        model = ModelFactory.get_model(model_type)
        # tools = ToolFactory.get_tool(ToolType.FILE)
        # 把List[ToolType]
        tools = ToolFactory.get_tools(tool_types)
        return Agent(model=model, tools=tools)
