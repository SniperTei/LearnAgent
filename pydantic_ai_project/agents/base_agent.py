from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from models.base_model import AIModel

class Tool(BaseModel):
    """Represents a tool that an agent can use"""
    name: str = Field(..., description="Name of the tool")
    description: str = Field(..., description="Description of what the tool does")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Parameters required by the tool")

    async def execute(self, **kwargs) -> Any:
        """Execute the tool with given parameters"""
        raise NotImplementedError("Tool execution must be implemented")

class BaseAgent(BaseModel):
    """Base class for all AI agents"""
    name: str = Field(..., description="Name of the agent")
    model: AIModel = Field(..., description="AI model used by the agent")
    tools: List[Tool] = Field(default_factory=list, description="List of tools available to the agent")
    memory: Dict[str, Any] = Field(default_factory=dict, description="Agent's memory storage")
    config: Dict[str, Any] = Field(default_factory=dict, description="Additional agent configuration")

    async def process(self, input_text: str) -> str:
        """Process input and generate response using the AI model"""
        raise NotImplementedError("Subclasses must implement process")

    async def use_tool(self, tool_name: str, **kwargs) -> Any:
        """Use a specific tool from the agent's toolset"""
        tool = next((t for t in self.tools if t.name == tool_name), None)
        if not tool:
            raise ValueError(f"Tool '{tool_name}' not found")
        return await tool.execute(**kwargs)

class ChatAgent(BaseAgent):
    """Chat-focused agent implementation"""
    conversation_history: List[Dict[str, str]] = Field(
        default_factory=list,
        description="History of the conversation"
    )

    async def process(self, input_text: str) -> str:
        # Add user message to history
        self.conversation_history.append({"role": "user", "content": input_text})
        
        # Generate response using the model
        response = await self.model.generate_response(input_text)
        
        # Add assistant response to history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response

class TaskAgent(BaseAgent):
    """Task-focused agent implementation"""
    current_task: Optional[str] = Field(None, description="Current task being processed")
    task_history: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="History of completed tasks"
    )

    async def process(self, input_text: str) -> str:
        # Set current task
        self.current_task = input_text
        
        # Generate task execution plan
        response = await self.model.generate_response(
            f"Task: {input_text}\nGenerate step-by-step plan."
        )
        
        # Add task to history
        self.task_history.append({
            "task": input_text,
            "plan": response,
            "status": "completed"
        })
        
        return response