from enum import Enum
from typing import Optional, Union, List, Dict
from pydantic_ai import Tool # 导入 Tool 类

from .file_tool import FileTool

class ToolType(Enum):
    """工具类型枚举"""
    FILE = "file"
    # 在这里可以添加更多工具类型

class ToolFactory:
    """工具工厂类，用于创建和管理不同类型的工具实例"""
    
    _tools = {
        ToolType.FILE: [
            Tool(
                function=FileTool.read_file,
                name="read_file",
                description="读取文件内容"
            ),
            Tool(
                function=FileTool.write_file,
                name="write_file",
                description="写入内容到文件"
            ),
            Tool(
                function=FileTool.append_file,
                name="append_file",
                description="追加内容到文件"
            ),
            Tool(
                function=FileTool.delete_file,
                name="delete_file",
                description="删除文件"
            ),
            Tool(
                function=FileTool.list_files,
                name="list_files",
                description="列出目录下的文件"
            ),
            Tool(
                function=FileTool.copy_file,
                name="copy_file",
                description="复制文件"
            ),
            Tool(
                function=FileTool.move_file,
                name="move_file",
                description="移动文件"
            ),
            Tool(
                function=FileTool.create_directory,
                name="create_directory",
                description="创建目录"
            ),
            Tool(
                function=FileTool.delete_directory,
                name="delete_directory",
                description="删除目录及其内容"
            ),
            Tool(
                function=FileTool.compress_file,
                name="compress_file",
                description="压缩单个文件"
            ),
            Tool(
                function=FileTool.compress_directory,
                name="compress_directory",
                description="压缩整个目录"
            ),
            Tool(
                function=FileTool.extract_zip,
                name="extract_zip",
                description="解压缩zip文件"
            )
        ]
    }
    
    @classmethod
    def get_tool(cls, tool_type: ToolType) -> List[Tool]:
        """获取指定类型的工具实例

        Args:
            tool_type (ToolType): 工具类型

        Returns:
            List[Tool]: 工具列表

        Raises:
            ValueError: 当指定的工具类型不存在时抛出
        """
        if tool_type not in cls._tools:
            raise ValueError(f"Unsupported tool type: {tool_type}")
        
        return cls._tools[tool_type]
    
    @classmethod
    def register_tool(cls, tool_type: ToolType, tool_list: List[Tool]) -> None:
        """注册新的工具类型

        Args:
            tool_type (ToolType): 工具类型
            tool_list (List[Tool]): 工具列表
        """
        cls._tools[tool_type] = tool_list
    
    @classmethod
    def list_available_tools(cls) -> list:
        """列出所有可用的工具类型

        Returns:
            list: 可用工具类型列表
        """
        return list(cls._tools.keys())