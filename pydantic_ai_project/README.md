# Pydantic AI Agent 项目

这是一个基于pydantic的AI代理系统，支持多种模型和代理类型的灵活切换。

## 环境配置

1.  首先克隆项目并安装依赖：
    ```bash
    git clone <repository_url>
    cd pydantic_ai_project
    pip install -r requirements.txt
    ```

2.  配置环境变量：
    -   复制环境变量示例文件：
        ```bash
        cp .env.example .env
        ```
    -   编辑 `.env` 文件，填入你的API密钥：
        ```plaintext
        QWEN_API_KEY=your_qwen_api_key_here
        GPT_API_KEY=your_openai_api_key_here
        GEMINI_API_KEY=your_gemini_api_key_here
        ```

3.  获取API密钥：
    -   Qwen API密钥：访问通义千问开放平台获取
    -   GPT API密钥：访问OpenAI平台获取
    -   Gemini API密钥：访问Google AI Studio获取

## 使用方法

1.  运行主程序：
    ```bash
    python main.py
    ```

2.  自定义使用示例：
    ```python
    import asyncio
    from agents.agent_factory import AgentFactory, AgentType
    from models.model_factory import ModelType
    from tools.tool_factory import ToolType

    async def main():
        # 创建一个BASIC类型的代理，使用GEMINI模型和FILE工具
        agent = AgentFactory.create_agent(
            agent_type=AgentType.BASIC,
            model_type=ModelType.GEMINI,
            tool_types=[ToolType.FILE]
        )

        # 运行代理并获取响应
        response = await agent.run("你好，请帮我列出当前目录下的所有文件。")
        print(response)

    if __name__ == "__main__":
        # 确保已配置 GEMINI_API_KEY 环境变量
        asyncio.run(main())
    ```

## 注意事项

-   请确保 `.env` 文件中的API密钥正确配置
-   不要将 `.env` 文件提交到版本控制系统
-   建议将 `.env` 添加到 `.gitignore` 文件中