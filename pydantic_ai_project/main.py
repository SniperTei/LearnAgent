import asyncio
from typing import Dict, Type
from models.base_model import AIModel, GPTModel, LlamaModel
from agents.base_agent import BaseAgent, ChatAgent, TaskAgent
from tools.basic_tools import SearchTool, CalculatorTool, DateTimeTool, NoteTool

class AgentFactory:
    """Factory class for creating and managing different types of agents"""
    
    def __init__(self):
        self.models: Dict[str, Type[AIModel]] = {
            'gpt': GPTModel,
            'llama': LlamaModel
        }
        
        self.agents: Dict[str, Type[BaseAgent]] = {
            'chat': ChatAgent,
            'task': TaskAgent
        }
        
        self.tools = [
            SearchTool(),
            CalculatorTool(),
            DateTimeTool(),
            NoteTool()
        ]
    
    def create_model(self, model_type: str, **config) -> AIModel:
        """Create an AI model instance"""
        if model_type not in self.models:
            raise ValueError(f"Unknown model type: {model_type}")
        
        model_class = self.models[model_type]
        return model_class(model_type=model_type, **config)
    
    def create_agent(self, agent_type: str, model: AIModel, **config) -> BaseAgent:
        """Create an agent instance"""
        if agent_type not in self.agents:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        agent_class = self.agents[agent_type]
        return agent_class(
            model=model,
            tools=self.tools,
            **config
        )

async def main():
    # Initialize the agent factory
    factory = AgentFactory()
    
    # Example: Create a GPT-based chat agent
    gpt_model = factory.create_model(
        model_type='gpt',
        model_name='gpt-3.5-turbo',
        api_key='your-api-key-here'
    )
    
    chat_agent = factory.create_agent(
        agent_type='chat',
        model=gpt_model,
        name='ChatBot'
    )
    
    # Example: Create a Llama-based task agent
    llama_model = factory.create_model(
        model_type='llama',
        model_name='llama-2-70b',
        api_key='your-api-key-here'
    )
    
    task_agent = factory.create_agent(
        agent_type='task',
        model=llama_model,
        name='TaskBot'
    )
    
    # Example usage of different agents
    chat_response = await chat_agent.process("Hello! How can you help me today?")
    print(f"Chat Agent Response: {chat_response}")
    
    task_response = await task_agent.process("Create a project timeline for developing a web application")
    print(f"Task Agent Response: {task_response}")

if __name__ == "__main__":
    asyncio.run(main())