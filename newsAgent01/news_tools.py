import requests
import os
from dotenv import load_dotenv

load_dotenv()

# 获取头条新闻方法

def get_tiktok_news():
    API_KEY = os.getenv("WHYTA_HOT_NEWS_APP_KEY")
    # print("API_KEY:", API_KEY)
    url = "https://whyta.cn/api/toutiao"
    params = {
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    # print("response:", response.json())
    # 返回格式
    # {
    #   "items":[
    #     {
    #       "id": "7501109588381404711",
    #       "title": "赵心童世锦赛夺冠奖金有多少",
    #       "url": "https://www.toutiao.com/trending/7501109588381404711/",
    #       "extra": {}
    #     },
    #     {
    #       "id": "7499709158896680970",
    #       "title": "春晚机器人五一兼职累到翘二郎腿",
    #       "url": "https://www.toutiao.com/trending/7499709158896680970/",
    #       "extra": {}
    #     }
    #   ]
    # }
    return response.json()

# 获取知乎热榜
def get_zhihu_hot():
    API_KEY = os.getenv("WHYTA_HOT_NEWS_APP_KEY")
    # print("API_KEY:", API_KEY)
    url = "https://whyta.cn/api/zhihu"
    params = {
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    # print("response:", response.json())
    # 返回格式
    # {
    #   "id": 1889380471143622700,
    #   "title": "《哪吒 2》总票房已破 154 亿元，冲击全球影史票房榜第 4，能否超越《泰坦尼克号》再创纪录？",
    #   "extra": {},
    #   "url": "https://www.zhihu.com/question/1889380471143622651"
    # }
    return response.json()

# 整理总结新闻
def summarize_news(news_json):
    """
    news_json: dict, 包含 item 列表或单条新闻
    返回所有新闻的title列表
    """
    titles = []
    # 处理头条新闻格式
    if "items" in news_json and isinstance(news_json["items"], list):
        for item in news_json["items"]:
            if "title" in item:
                titles.append(item["title"])
    # 处理知乎热榜格式（单条或多条）
    elif isinstance(news_json, list):
        for item in news_json:
            if "title" in item:
                titles.append(item["title"])
    elif "title" in news_json:
        titles.append(news_json["title"])
    return titles

# main
if __name__ == "__main__":
    news = get_tiktok_news()  # 或 get_zhihu_hot()
    titles = summarize_news(news)
    print("所有新闻标题：")
    for t in titles:
        print("-", t)