AI News Summarizer WhatsApp Bot
A Python bot that fetches the latest news, uses LangChain and Google Gemini to create a summarized digest, and sends it to your WhatsApp number daily using Twilio.

![Project Demo GIF or Image - if you have one]

🌟 Features
Automated News Fetching: Fetches top headlines from the GNews API based on specified categories and countries.

Intelligent Summarization: Utilizes Google's gemini-1.5-flash model via LangChain to generate high-quality, readable summaries of multiple articles.

Direct WhatsApp Delivery: Sends the formatted news digest directly to your phone using the Twilio API for WhatsApp.


Daily Scheduling: Uses the schedule library to automate the process, ensuring you get your news summary at the same time every day.

Easy Configuration: All API keys and personal numbers are managed securely through a .env file.

🛠️ Tech Stack
Language: Python


LLM Framework: LangChain 

LLM: Google Gemini

News Source: GNews API


Messaging: Twilio API 


Scheduling: schedule 


Dependencies: python-dotenv, requests 

⚙️ Setup and Installation
Clone the repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Create a virtual environment and install dependencies:

Bash

# For Unix/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
Create a .env file:
Create a file named .env in the root directory and add your API keys and credentials.

Code snippet

# summarize.py
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"

# fetch_news.py
GNEWS_API_KEY="YOUR_GNEWS_API_KEY"

# main.py
TWILIO_ACCOUNT_SID="YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN="YOUR_TWILIO_AUTH_TOKEN"
TWILIO_WHATSAPP_NUMBER="YOUR_TWILIO_WHATSAPP_SANDBOX_NUMBER"
MY_WHATSAPP_NUMBER="YOUR_PERSONAL_WHATSAPP_NUMBER_WITH_COUNTRY_CODE"
🚀 Usage
Run the main script from your terminal:

Bash

python main.py
You will be presented with three options:

Send news summary now: For immediate testing.

Start scheduler (run daily at 8:00 AM): Runs the bot at the default time.

Custom schedule time: Allows you to set a custom daily time in HH:MM format
