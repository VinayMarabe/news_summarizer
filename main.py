import os
import schedule
import time
from datetime import datetime
from dotenv import load_dotenv
from twilio.rest import Client
from fetch_news import NewsAPIFetcher
from summarize import NewsSummarizer

load_dotenv()

class NewsBot:
    def __init__(self):
        """Initialize the news bot with Twilio credentials"""
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.twilio_whatsapp = os.getenv('TWILIO_WHATSAPP_NUMBER')
        self.my_whatsapp = os.getenv('MY_WHATSAPP_NUMBER')
        
        # Initialize Twilio client
        self.client = Client(self.account_sid, self.auth_token)
        
        # Initialize news fetcher and summarizer
        self.news_fetcher = NewsAPIFetcher()
        self.summarizer = NewsSummarizer()
    
    def send_whatsapp_message(self, message):
        """
        Send WhatsApp message via Twilio
        
        Args:
            message: Message text to send
        """
        try:
            # Twilio WhatsApp format: whatsapp:+1234567890
            from_number = f"whatsapp:{self.twilio_whatsapp}"
            to_number = f"whatsapp:{self.my_whatsapp}"
            
            message_obj = self.client.messages.create(
                body=message, 
                from_=from_number,
                to=to_number
            )
            
            print(f"✅ Message sent successfully! SID: {message_obj.sid}")
            return True
        
        except Exception as e:
            print(f"❌ Error sending WhatsApp message: {e}")
            return False
    
    def generate_and_send_news_summary(self, category='general', country='us'):
        """
        Fetch news, generate summary, and send via WhatsApp
        
        Args:
            category: News category
            country: Country code
        """
        print(f"\n{'='*50}")
        print(f"🤖 Starting news summary generation at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*50}\n")
        
        # Fetch news articles
        print("📡 Fetching news articles...")
        articles = self.news_fetcher.fetch_top_headlines(
            category=category,
            country=country,
            max_articles=4
        )
        
        if not articles:
            print("⚠️  No articles fetched. Aborting.")
            return
        
        print(f"✅ Fetched {len(articles)} articles")
        
        # Format articles for summarization
        news_text = self.news_fetcher.format_articles_for_summary(articles)
        
        # Generate summary
        print("🤖 Generating AI summary...")
        summary = self.summarizer.summarize_news(news_text)

        # Truncate summary to 1600 characters for Twilio WhatsApp
        max_length = 1500
        if len(summary) > max_length:
            summary = summary[:max_length - 3] + "..."

        print("✅ Summary generated")
        print("\n" + "="*50)
        print("SUMMARY PREVIEW:")
        print("="*50)
        print(summary[:500] + "..." if len(summary) > 500 else summary)
        print("="*50 + "\n")

        # Send via WhatsApp
        print("📱 Sending WhatsApp message...")
        success = self.send_whatsapp_message(summary)
        
        if success:
            print("✅ Daily news summary sent successfully!\n")
        else:
            print("❌ Failed to send news summary\n")
    
    def run_daily_summary(self):
        """Run the daily news summary job"""
        self.generate_and_send_news_summary()
    
    def start_scheduler(self, time_str="08:00"):
        """
        Start the scheduler to run daily at specified time
        
        Args:
            time_str: Time in HH:MM format (24-hour)
        """
        print(f"\n{'='*50}")
        print(f"🚀 News Summarizer Bot Started!")
        print(f"{'='*50}")
        print(f"⏰ Scheduled to run daily at {time_str}")
        print(f"🌍 Timezone: System local time")
        print(f"📱 Will send to: {self.my_whatsapp}")
        print(f"{'='*50}\n")
        
        # Schedule the job
        schedule.every().day.at(time_str).do(self.run_daily_summary)
        
        # Keep the script running
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute


def main():
    """Main function to run the news bot"""
    bot = NewsBot()
    
    # Option 1: Run immediately (for testing)
    print("Choose an option:")
    print("1. Send news summary now (test)")
    print("2. Start scheduler (run daily at 8:00 AM)")
    print("3. Custom schedule time")
    
    choice = input("\nEnter your choice (1/2/3): ").strip()
    
    if choice == '1':
        bot.generate_and_send_news_summary()
    elif choice == '2':
        bot.start_scheduler("08:00")
    elif choice == '3':
        custom_time = input("Enter time (HH:MM in 24-hour format): ").strip()
        bot.start_scheduler(custom_time)
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()