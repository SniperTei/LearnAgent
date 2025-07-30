from enum import Enum
from typing import Optional, List
from pydantic_ai import Agent, Tool

from models.model_factory import ModelFactory, ModelType
from tools.tool_factory import ToolFactory, ToolType

class AgentType(Enum):
    """agent枚举"""
    NEWES = "News"
    WEATHER = "Weather"
    FILE_MANAGER = "FileManager"
    SERVICE = "Service"
    # 可以添加更多agent

class AgentFactory:
    """agent工厂类,用于创建和管理不同类型的agent实例"""
    
    @classmethod
    def create_agent(cls, agent_type: AgentType, model_type: ModelType, tool_types: Optional[List[ToolType]] = None) -> Agent:
        """创建agent实例"""
        model = ModelFactory.get_model(model_type)
        tools = ToolFactory.get_tool(ToolType.FILE)
        # tools = [ToolFactory.get_tool(tool_type) for tool_type in tool_types] if tool_types else []
        # 打印tools
        # print(tools)
        return Agent(model=model, tools=tools)
