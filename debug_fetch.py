import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_gnews_api():
    """Test GNews API connection and fetch"""
    api_key = os.getenv('GNEWS_API_KEY')
    
    print("="*60)
    print("🔍 DEBUGGING GNEWS API")
    print("="*60)
    
    # Check if API key exists
    if not api_key:
        print("❌ ERROR: GNEWS_API_KEY not found in .env file!")
        print("   Please add your API key to .env file")
        return
    
    print(f"✅ API Key found: {api_key[:10]}...{api_key[-4:]}")
    
    # Test API endpoint
    url = 'https://gnews.io/api/v4/top-headlines'
    params = {
        'token': api_key,
        'lang': 'en',
        'country': 'us',
        'max': 5,
        'topic': 'general'
    }
    
    print(f"\n📡 Testing API endpoint: {url}")
    print(f"Parameters: {params}")
    print("\nMaking request...\n")
    
    try:
        response = requests.get(url, params=params, timeout=15)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}\n")
        
        if response.status_code == 200:
            data = response.json() 
            print("✅ SUCCESS! API is working")
            print(f"\nTotal Articles: {data.get('totalArticles', 0)}")
            
            articles = data.get('articles', [])
            if articles:
                print(f"\n📰 Fetched {len(articles)} articles:\n")
                for i, article in enumerate(articles, 1):
                    print(f"{i}. {article.get('title', 'No title')}")
                    print(f"   Source: {article.get('source', {}).get('name', 'Unknown')}")
                    print(f"   URL: {article.get('url', 'No URL')}\n")
            else:
                print("⚠️  No articles in response")
                print(f"Full response: {data}")
        
        elif response.status_code == 401:
            print("❌ ERROR 401: Unauthorized")
            print("   Your API key is invalid or expired")
            print("   Please get a new key from https://gnews.io/")
        
        elif response.status_code == 403:
            print("❌ ERROR 403: Forbidden")
            print("   You may have exceeded your API quota")
            print(f"   Response: {response.text}")
        
        elif response.status_code == 429:
            print("❌ ERROR 429: Too Many Requests")
            print("   You've exceeded the rate limit")
            print("   Free tier: 100 requests/day")
        
        else:
            print(f"❌ ERROR {response.status_code}")
            print(f"Response: {response.text}")
    
    except requests.exceptions.Timeout:
        print("❌ ERROR: Request timed out")
        print("   Check your internet connection")
    
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Connection failed")
        print("   Check your internet connection")
    
    except Exception as e:
        print(f"❌ ERROR: {type(e).__name__}: {e}")


def test_alternative_newsapi():
    """Test alternative free news APIs"""
    print("\n" + "="*60)
    print("🔍 TESTING ALTERNATIVE: NewsAPI.org")
    print("="*60)
    
    # NewsAPI.org offers free tier
    # You can get a key from https://newsapi.org/
    print("\nNewsAPI.org offers:")
    print("- Free tier: 100 requests/day")
    print("- More reliable than GNews")
    print("- Get key from: https://newsapi.org/register")
    print("\nIf GNews doesn't work, I can provide code for NewsAPI.org")


if __name__ == "__main__":
    test_gnews_api()
    test_alternative_newsapi()