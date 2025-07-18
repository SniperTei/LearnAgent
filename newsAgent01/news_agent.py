from pydantic_ai import Agent, Tool
from pydantic_ai.models.gemini import GeminiModel
from dotenv import load_dotenv
from news_tools import get_tiktok_news, get_zhihu_hot

load_dotenv()

model = GeminiModel("gemini-2.5-flash")

@Tool
def summarize_news_tool() -> str:
    """获取并总结今日新闻标题"""
    try:
        # 获取头条新闻
        toutiao_data = get_tiktok_news()
        zhihu_data = get_zhihu_hot()
        
        titles = []
        
        # 处理头条新闻
        if "items" in toutiao_data and isinstance(toutiao_data["items"], list):
            for item in toutiao_data["items"]:
                if "title" in item:
                    titles.append(item["title"])
        
        # 处理知乎热榜
        if isinstance(zhihu_data, list):
            for item in zhihu_data:
                if "title" in item:
                    titles.append(item["title"])
        elif "title" in zhihu_data:
            titles.append(zhihu_data["title"])
        
        # 返回前10条新闻标题
        result = "今日新闻标题：\n"
        for i, title in enumerate(titles[:10], 1):
            result += f"{i}. {title}\n"
        
        return result
        
    except Exception as e:
        return f"获取新闻失败: {str(e)}"

agent = Agent(
    model,
    system_prompt="You are a news agent, you need to use the tools to get the news, and then you need to summarize the news, and then you need to answer the question in Chinese",
    result_type=str,
    tools=[get_tiktok_news, get_zhihu_hot, summarize_news_tool]
)

result = agent.run_sync("what is the news today? give me 10 news title")
print(result.output)