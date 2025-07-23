import json
import os

def read_mock_movie_data() -> list:
    """
    读取 mock_movie_data.json 文件，返回电影数据列表
    """
    file_path = os.path.join(os.path.dirname(__file__), "data", "mock_movie_data.json")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # 返回 data_list 部分
    return data.get("data_list", [])


def get_movie_by_id(movie_id: str) -> dict:
    """
    根据电影id获取电影数据
    """
    movies = read_mock_movie_data()
    for movie in movies:
        if movie.get("movie_id") == movie_id:
            return movie
    return {}

def get_movies_by_star(star_name: str) -> list:
    """
    根据电影明星姓名获取所有相关电影数据
    """
    movies = read_mock_movie_data()
    result = []
    for movie in movies:
        if "movie_star" in movie and star_name in movie["movie_star"]:
            result.append(movie)
    return result



