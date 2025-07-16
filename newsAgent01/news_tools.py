import requests
import os
from dotenv import load_dotenv

load_dotenv()

# 获取新闻方法
def get_news():
    #     接口地址： https://whyta.cn/api/toutiao
    # 返回格式： JSON
    # 请求方式： GET
    # 请求示例：https://whyta.cn/api/toutiao?key=你的APIKEY
    # 获取环境变量的API_KEY
    API_KEY = os.getenv("WHYTA_HOT_NEWS_APP_KEY")
    print("API_KEY:", API_KEY)
    url = "https://whyta.cn/api/toutiao"
    params = {
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    print("response:", response.json())
    return response.json()

# main
if __name__ == "__main__":
    news = get_news()
    print("news:", news)