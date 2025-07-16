import requests

# 方法1：通过经纬度获取城市名字

def get_forecast(lat, lon):
    """
    传入纬度lat和经度lon，返回对应的城市名字。
    使用OpenStreetMap Nominatim API。
    """
    url = f"https://nominatim.openstreetmap.org/reverse"
    params = {
        'lat': lat,
        'lon': lon,
        'format': 'json',
        'zoom': 10,
        'addressdetails': 1
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; MyWeatherApp/1.0)'
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        address = data.get('address', {})
        # 优先返回 city，没有则返回 town 或 state
        return address.get('city') or address.get('town') or address.get('state') or '未知城市'
    else:
        return '查询失败'

# 方法2：通过城市名字获取天气

def get_weather_by_city(city_name, api_key=None):
    """
    传入城市名字，返回该城市的天气信息。
    使用OpenWeatherMap API。
    需要注册获取API key。
    """
    if api_key is None:
        raise ValueError('请提供OpenWeatherMap的API key')
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'lang': 'zh_cn',
        'units': 'metric'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # 返回主要天气描述和温度
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"{city_name} 天气：{weather}，温度：{temp}°C"
    else:
        return '天气查询失败'
