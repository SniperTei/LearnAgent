from enum import Enum
from typing import Optional, Union, List, Callable, Dict # 导入 Callable
# from pydantic_ai import Tool # 移除对 Tool 类的导入，因为我们不再直接使用它

from .file_tool import FileTool

class ToolType(Enum):
    """工具类型枚举"""
    FILE = "file"
    # 在这里可以添加更多工具类型

class ToolFactory:
    """工具工厂类，用于创建和管理不同类型的工具实例"""
    
    _tools = {
        ToolType.FILE: [
            FileTool.read_file, # 直接存储函数引用
            FileTool.write_file,
            FileTool.append_file,
            FileTool.delete_file,
            FileTool.list_files,
            FileTool.copy_file,
            FileTool.move_file,
            FileTool.create_directory,
            FileTool.delete_directory,
            FileTool.compress_file,
            FileTool.compress_directory,
            FileTool.extract_zip
        ]
    }
    
    @classmethod
    def get_tools(cls, tool_type: ToolType) -> List[Callable]: # 返回 Callable 列表
        """获取指定类型的工具实例

        Args:
            tool_type (ToolType): 工具类型

        Returns:
            List[Callable]: 函数列表

        Raises:
            ValueError: 当指定的工具类型不存在时抛出
        """
        if tool_type not in cls._tools:
            raise ValueError(f"Unsupported tool type: {tool_type}")
        
        return cls._tools[tool_type]
    
    @classmethod
    def register_tool(cls, tool_type: ToolType, tool_list: List[Callable]) -> None:
        """注册新的工具类型

        Args:。
            tool_type (ToolType): 工具类型
            tool_list (List[Callable]): 函数列表
        """
        cls._tools[tool_type] = tool_list
    
    @classmethod
    def list_available_tools(cls) -> list:
        """列出所有可用的工具类型

        Returns:
            list: 可用工具类型列表
        """
        return list(cls._tools.keys())