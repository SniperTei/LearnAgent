import asyncio
from agents.agent_factory import AgentFactory, AgentType
from models.model_factory import ModelType
from tools.tool_factory import ToolType

async def main():
    print("Initializing agent...")
    # 创建一个使用Gemini模型和文件工具的基础代理
    agent = AgentFactory.create_agent(
        agent_type=AgentType.BASIC,
        model_type=ModelType.GEMINI,
        tool_types=[ToolType.FILE]
    )
    print("Agent initialized. Running...")
    
    # # 运行代理并获取响应
    # response = await agent.run("帮我读取README.md中的内容好吗")
    # print(f"Agent Response: {response}")
    # 欢迎语
    print("Welcome to use the agent! Type 'exit' to quit.")
    # 循环运行代理
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting...")
            break
        response = await agent.run(user_input)
        print(f"Agent: {response}")

if __name__ == "__main__":
    asyncio.run(main())