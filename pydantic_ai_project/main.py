import asyncio
from agents.agent_factory import AgentFactory, AgentType
from models.model_factory import ModelType
from tools.tool_factory import ToolType

async def main():
    print("Initializing agent...")
    # 创建一个使用Gemini模型和文件工具的基础代理
    agent = AgentFactory.create_agent(
        agent_type=AgentType.FILE_MANAGER,
        model_type=ModelType.GEMINI,
        tool_types=[ToolType.FILE]
    )
    print("Agent initialized. Running...")
    
    # 运行代理并获取响应
    response = await agent.run("帮我读取README.md中的内容好吗")
    print(f"Agent Response: {response}")

if __name__ == "__main__":
    asyncio.run(main())