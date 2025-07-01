import requests
import json
from datetime import datetime

def test_network_connection():
    """测试网络连接"""
    print("🌐 测试网络连接...")
    
    # 测试基本网络连接
    try:
        response = requests.get("https://www.google.com", timeout=5)
        print(f"✅ 基本网络连接正常 (状态码: {response.status_code})")
    except Exception as e:
        print(f"❌ 基本网络连接失败: {e}")
        return False
    
    # 测试DuckDuckGo API
    print("\n🔍 测试DuckDuckGo API...")
    try:
        url = "https://api.duckduckgo.com/"
        params = {
            'q': 'test',
            'format': 'json',
            'no_html': '1',
            'skip_disambig': '1'
        }
        
        response = requests.get(url, params=params, timeout=10)
        print(f"✅ DuckDuckGo API连接正常 (状态码: {response.status_code})")
        
        data = response.json()
        print(f"📄 响应数据: {json.dumps(data, indent=2)[:500]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ DuckDuckGo API连接失败: {e}")
        return False

def test_search_functionality():
    """测试搜索功能"""
    print("\n🔍 测试搜索功能...")
    
    try:
        url = "https://api.duckduckgo.com/"
        params = {
            'q': '中国娱乐明星',
            'format': 'json',
            'no_html': '1',
            'skip_disambig': '1'
        }
        
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        print(f"📊 搜索关键词: 中国娱乐明星")
        print(f"📄 响应数据大小: {len(str(data))} 字符")
        
        # 检查是否有摘要
        if data.get('Abstract'):
            print(f"✅ 找到摘要: {data.get('Abstract', '')[:100]}...")
        else:
            print("❌ 没有找到摘要")
        
        # 检查相关主题
        related_topics = data.get('RelatedTopics', [])
        print(f"📚 相关主题数量: {len(related_topics)}")
        
        if related_topics:
            for i, topic in enumerate(related_topics[:3]):
                if isinstance(topic, dict) and topic.get('Text'):
                    print(f"📖 主题 {i+1}: {topic.get('Text', '')[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ 搜索功能测试失败: {e}")
        return False

if __name__ == "__main__":
    print("🚀 开始网络诊断...")
    
    network_ok = test_network_connection()
    search_ok = test_search_functionality()
    
    print("\n📋 诊断结果:")
    if network_ok and search_ok:
        print("✅ 网络和搜索功能都正常")
        print("💡 问题可能在于AI模型的处理逻辑")
    elif network_ok and not search_ok:
        print("⚠️ 网络正常但搜索功能有问题")
        print("💡 可能是DuckDuckGo API的问题")
    elif not network_ok:
        print("❌ 网络连接有问题")
        print("💡 请检查网络连接或代理设置") 