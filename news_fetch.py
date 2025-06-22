import requests

def get_news():
    api_key = "36c3b3a471504fbf8c2f3db643943c01"  # ✅ Your real API key
    url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=5&apiKey={api_key}"
    
    response = requests.get(url)
    data = response.json()
    
    articles = data.get("articles", [])
    return [(a["title"], a["description"]) for a in articles if a.get("description")]

