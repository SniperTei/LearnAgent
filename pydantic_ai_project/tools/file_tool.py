import os
import shutil
from typing import List, Optional, Union
from pathlib import Path
import zipfile
from pydantic import BaseModel

class FileTool:
    @staticmethod
    def read_file(file_path: Union[str, Path], encoding: str = 'utf-8') -> str:
        """读取文件内容

        Args:
            file_path: 文件路径
            encoding: 文件编码，默认utf-8

        Returns:
            str: 文件内容
        """
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()
    
    @staticmethod
    def write_file(file_path: Union[str, Path], content: str, encoding: str = 'utf-8') -> None:
        """写入文件内容

        Args:
            file_path: 文件路径
            content: 要写入的内容
            encoding: 文件编码，默认utf-8
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(content)
    
    @staticmethod
    def append_file(file_path: Union[str, Path], content: str, encoding: str = 'utf-8') -> None:
        """追加内容到文件

        Args:
            file_path: 文件路径
            content: 要追加的内容
            encoding: 文件编码，默认utf-8
        """
        with open(file_path, 'a', encoding=encoding) as f:
            f.write(content)
    
    @staticmethod
    def delete_file(file_path: Union[str, Path]) -> None:
        """删除文件

        Args:
            file_path: 要删除的文件路径
        """
        if os.path.exists(file_path):
            os.remove(file_path)
    
    @staticmethod
    def list_files(directory: Union[str, Path], pattern: Optional[str] = None) -> List[str]:
        """列出目录下的所有文件

        Args:
            directory: 目录路径
            pattern: 文件匹配模式，例如 '*.py'

        Returns:
            List[str]: 文件路径列表
        """
        if pattern:
            return [os.path.join(root, file)
                    for root, _, files in os.walk(directory)
                    for file in files
                    if file.endswith(pattern.replace('*', ''))]
        return [os.path.join(root, file)
                for root, _, files in os.walk(directory)
                for file in files]
    
    @staticmethod
    def copy_file(src: Union[str, Path], dst: Union[str, Path]) -> None:
        """复制文件

        Args:
            src: 源文件路径
            dst: 目标文件路径
        """
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    
    @staticmethod
    def move_file(src: Union[str, Path], dst: Union[str, Path]) -> None:
        """移动文件

        Args:
            src: 源文件路径
            dst: 目标文件路径
        """
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
    
    @staticmethod
    def create_directory(directory: Union[str, Path]) -> None:
        """创建目录

        Args:
            directory: 目录路径
        """
        os.makedirs(directory, exist_ok=True)
    
    @staticmethod
    def delete_directory(directory: Union[str, Path]) -> None:
        """删除目录及其内容

        Args:
            directory: 要删除的目录路径
        """
        if os.path.exists(directory):
            shutil.rmtree(directory)
    
    @staticmethod
    def get_file_size(file_path: Union[str, Path]) -> int:
        """获取文件大小

        Args:
            file_path: 文件路径

        Returns:
            int: 文件大小（字节）
        """
        return os.path.getsize(file_path)
    
    @staticmethod
    def get_file_modification_time(file_path: Union[str, Path]) -> float:
        """获取文件最后修改时间

        Args:
            file_path: 文件路径

        Returns:
            float: 最后修改时间的时间戳
        """
        return os.path.getmtime(file_path)
    
    @staticmethod
    def compress_file(file_path: Union[str, Path], output_path: Optional[Union[str, Path]] = None) -> str:
        """压缩单个文件

        Args:
            file_path: 要压缩的文件路径
            output_path: 输出的压缩文件路径，如果不指定则在原文件目录下创建同名zip文件

        Returns:
            str: 压缩文件的路径
        """
        if output_path is None:
            output_path = str(file_path) + '.zip'
        
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.write(file_path, os.path.basename(file_path))
        
        return output_path

    @staticmethod
    def compress_directory(directory: Union[str, Path], output_path: Optional[Union[str, Path]] = None) -> str:
        """压缩整个目录

        Args:
            directory: 要压缩的目录路径
            output_path: 输出的压缩文件路径，如果不指定则在原目录下创建同名zip文件

        Returns:
            str: 压缩文件的路径
        """
        if output_path is None:
            output_path = str(directory) + '.zip'
        
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, directory)
                    zf.write(file_path, arcname)
        
        return output_path

    @staticmethod
    def extract_zip(zip_path: Union[str, Path], extract_path: Optional[Union[str, Path]] = None) -> str:
        """解压缩zip文件

        Args:
            zip_path: zip文件路径
            extract_path: 解压目标路径，如果不指定则解压到当前目录

        Returns:
            str: 解压目标路径
        """
        if extract_path is None:
            extract_path = os.path.dirname(zip_path)
        
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(extract_path)
        
        return extract_path

# 工具定义
class FileToolWrapper(BaseModel):
    @classmethod
    def get_tools(cls):
        """返回所有文件操作工具"""
        return [
            {
                "function": FileTool.read_file,
                "name": "read_file",
                "description": "读取文件内容"
            },
            {
                "function": FileTool.write_file,
                "name": "write_file",
                "description": "写入内容到文件"
            },
            {
                "function": FileTool.append_file,
                "name": "append_file",
                "description": "追加内容到文件"
            },
            {
                "function": FileTool.delete_file,
                "name": "delete_file",
                "description": "删除文件"
            },
            {
                "function": FileTool.list_files,
                "name": "list_files",
                "description": "列出目录下的文件"
            },
            {
                "function": FileTool.copy_file,
                "name": "copy_file",
                "description": "复制文件"
            },
            {
                "function": FileTool.move_file,
                "name": "move_file",
                "description": "移动文件"
            },
            {
                "function": FileTool.create_directory,
                "name": "create_directory",
                "description": "创建目录"
            },
            {
                "function": FileTool.delete_directory,
                "name": "delete_directory",
                "description": "删除目录及其内容"
            },
            {
                "function": FileTool.compress_file,
                "name": "compress_file",
                "description": "压缩单个文件"
            },
            {
                "function": FileTool.compress_directory,
                "name": "compress_directory",
                "description": "压缩整个目录"
            },
            {
                "function": FileTool.extract_zip,
                "name": "extract_zip",
                "description": "解压缩zip文件"
            }
        ]