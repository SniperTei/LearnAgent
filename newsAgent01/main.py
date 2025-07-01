from agent_news import NewsAgent
from dotenv import load_dotenv

def main():
    agent = NewsAgent()
    
    # 获取最新10条新闻
    topic = "财经"
    agent.get_latest_news(topic, 2)
    
    # print(f"=== {topic} 最新新闻 ===")
    # print(f"消息: {result.message}")
    # print(f"总数: {result.total_count} 条新闻")
    
    # if result.news:
    #     for i, news in enumerate(result.news, 1):
    #         print(f"\n--- 新闻 {i} ---")
    #         print(f"标题: {news.title}")
    #         print(f"来源: {news.source}")
    #         print(f"日期: {news.date}")
    #         print(f"内容: {news.content[:200]}...")
    #         print(f"链接: {news.url}")
    #         print(f"分类: {news.category}")
    #         print(f"标签: {', '.join(news.tags)}")
    # else:
    #     print("\n没有找到相关新闻。")


if __name__ == "__main__":
    main()



