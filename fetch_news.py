import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class NewsAPIFetcher:
    """Fetch news from NewsAPI.org"""
    def __init__(self):
        self.api_key = os.getenv('GNEWS_API_KEY')
        self.base_url = 'https://gnews.io/api/v4'
    
    def fetch_top_headlines(self, category='general', country='us', max_articles=10):
        """
        Fetch top headlines from GNews API
        
        Args:
            category: News category (general, business, technology, sports, etc.)
            country: Country code (us, in, gb, etc.)
            max_articles: Maximum number of articles to fetch
        """
        try:
            url = f'{self.base_url}/top-headlines'
            params = {
                'token': self.api_key,
                'lang': 'en',
                'country': country,
                'max': max_articles,
                'topic': category
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            articles = data.get('articles', [])
            
            formatted_articles = []
            for article in articles:
                formatted_articles.append({
                    'title': article.get('title', ''),
                    'description': article.get('description', ''),
                    'url': article.get('url', ''),
                    'source': article.get('source', {}).get('name', ''),
                    'publishedAt': article.get('publishedAt', '')
                })
            
            return formatted_articles
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news: {e}")
            return []
    
    def format_articles_for_summary(self, articles):
        """Format articles into a text suitable for summarization"""
        if not articles:
            return "No news articles found."
        
        formatted_text = f"News articles from {datetime.now().strftime('%B %d, %Y')}:\n\n" 
        
        for i, article in enumerate(articles, 1):
            title = article['title'][:120]  # Limit title length
            description = article['description'][:300] if article['description'] else ""
            formatted_text += f"{i}. {title}\n"
            formatted_text += f"   Source: {article['source']}\n"
            if description:
                formatted_text += f"   {description}\n"
            formatted_text += f"   URL: {article['url']}\n\n"
        
        return formatted_text


# Alternative free news source (no API key needed)
class NewsDataFetcher:
    """Fetch news from NewsData.io (alternative)"""
    def __init__(self):
        self.base_url = 'https://newsdata.io/api/1/news'
        # NewsData.io offers a free tier with API key
        # Sign up at https://newsdata.io to get a free key
    
    def fetch_top_headlines(self, category='top', country='us', max_articles=10):
        """Fetch news - placeholder for NewsData.io implementation"""
        # Implementation similar to above if you want to use NewsData.io
        pass