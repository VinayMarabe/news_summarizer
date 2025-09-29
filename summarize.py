import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

class NewsSummarizer:
    def __init__(self):
        """Initialize the news summarizer with Google Gemini"""
        self.api_key = os.getenv('GEMINI_API_KEY')
        
        # Initialize Gemini model
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=self.api_key,
            temperature=0.3,
            convert_system_message_to_human=True
        )
        
        # Create summarization prompt
        self.prompt_template = PromptTemplate(
            input_variables=["news_text"],
            template="""You are a professional news summarizer. Your task is to create a concise, 
                        informative daily news digest from the following news articles.

                        Please provide:
                        1. A brief overview (2 sentences) of the day's major themes
                        2. Key highlights from each important story (bullet points)
                        3. Keep the summary engaging and easy to read
                        4. Limit the summary to approximately 500 words

                        News Articles:
                        {news_text}

                        Daily News Summary:"""
        )
        
        # Create LangChain
        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt_template
        )
    
    def summarize_news(self, news_text):
        """
        Summarize news articles using Gemini
        
        Args:
            news_text: Formatted news articles text
            
        Returns:
            Summarized news digest
        """
        try:
            if not news_text or news_text == "No news articles found.":
                return "⚠️ Unable to fetch news articles at this time. Please try again later."
            
            # Generate summary using LangChain
            summary = self.chain.run(news_text=news_text)
            
            # Format for WhatsApp
            formatted_summary = f"📰 *Daily News Digest*\n"
            formatted_summary += f"{'='*30}\n\n"
            formatted_summary += summary
            formatted_summary += f"\n\n{'='*30}\n"
            formatted_summary += "🤖 _Powered by AI News Summarizer_"
            
            return formatted_summary
        
        except Exception as e:
            print(f"Error summarizing news: {e}")
            return f"⚠️ Error generating summary: {str(e)}"
    
    def summarize_by_category(self, news_text, category):
        """
        Summarize news for a specific category
        
        Args:
            news_text: Formatted news articles text
            category: News category (business, technology, sports, etc.)
            
        Returns:
            Categorized news summary
        """
        category_prompt = PromptTemplate(
            input_variables=["news_text", "category"],
            template="""You are a professional news summarizer specializing in {category} news.

                        Create a concise summary of the following {category} news articles:
                        - Focus on the most important developments in {category}
                        - Highlight key trends and significant events
                        - Keep it informative yet brief (300-400 words)

                        News Articles:
                        {news_text}

                        {category} News Summary:"""
        )
        
        try:
            category_chain = LLMChain(llm=self.llm, prompt=category_prompt)
            summary = category_chain.run(news_text=news_text, category=category.title())
            
            formatted_summary = f"📊 *{category.title()} News Digest*\n"
            formatted_summary += f"{'='*30}\n\n"
            formatted_summary += summary
            formatted_summary += f"\n\n{'='*30}"
            
            return formatted_summary
        
        except Exception as e:
            print(f"Error summarizing {category} news: {e}")
            return f"⚠️ Error generating {category} summary: {str(e)}"