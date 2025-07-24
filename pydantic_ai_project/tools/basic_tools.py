from typing import Any, Dict
from agents.base_agent import Tool
import datetime
import json

class SearchTool(Tool):
    """Tool for performing web searches"""
    name: str = "search"
    description: str = "Perform a web search and return results"
    parameters: Dict[str, Any] = {
        "query": {"type": "string", "description": "Search query"},
        "max_results": {"type": "integer", "description": "Maximum number of results to return"}
    }

    async def execute(self, query: str, max_results: int = 5) -> list:
        # Implement actual search functionality here
        # This is a mock implementation
        return [f"Search result {i} for: {query}" for i in range(max_results)]

class CalculatorTool(Tool):
    """Tool for performing mathematical calculations"""
    name: str = "calculator"
    description: str = "Perform mathematical calculations"
    parameters: Dict[str, Any] = {
        "expression": {"type": "string", "description": "Mathematical expression to evaluate"}
    }

    async def execute(self, expression: str) -> float:
        try:
            # Warning: eval is used here for demonstration. In production,
            # use a safer evaluation method
            return float(eval(expression))
        except Exception as e:
            raise ValueError(f"Invalid mathematical expression: {e}")

class DateTimeTool(Tool):
    """Tool for date and time operations"""
    name: str = "datetime"
    description: str = "Get current date and time or perform date calculations"
    parameters: Dict[str, Any] = {
        "operation": {"type": "string", "description": "Operation to perform (now, format, add_days)"}
    }

    async def execute(self, operation: str, **kwargs) -> str:
        now = datetime.datetime.now()
        
        if operation == "now":
            return now.isoformat()
        elif operation == "format":
            format_str = kwargs.get("format", "%Y-%m-%d %H:%M:%S")
            return now.strftime(format_str)
        elif operation == "add_days":
            days = kwargs.get("days", 0)
            result = now + datetime.timedelta(days=days)
            return result.isoformat()
        else:
            raise ValueError(f"Unknown operation: {operation}")

class NoteTool(Tool):
    """Tool for taking and managing notes"""
    name: str = "note"
    description: str = "Create and manage notes"
    parameters: Dict[str, Any] = {
        "action": {"type": "string", "description": "Action to perform (create, read, list)"},
        "content": {"type": "string", "description": "Note content for create action"},
        "note_id": {"type": "string", "description": "Note ID for read action"}
    }
    
    _notes: Dict[str, str] = {}

    async def execute(self, action: str, **kwargs) -> Any:
        if action == "create":
            content = kwargs.get("content")
            if not content:
                raise ValueError("Content is required for create action")
            note_id = str(len(self._notes) + 1)
            self._notes[note_id] = content
            return {"note_id": note_id, "content": content}
        
        elif action == "read":
            note_id = kwargs.get("note_id")
            if not note_id or note_id not in self._notes:
                raise ValueError(f"Invalid note_id: {note_id}")
            return {"note_id": note_id, "content": self._notes[note_id]}
        
        elif action == "list":
            return [
                {"note_id": k, "content": v}
                for k, v in self._notes.items()
            ]
        
        else:
            raise ValueError(f"Unknown action: {action}")