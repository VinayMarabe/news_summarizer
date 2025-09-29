# News Summarizer WhatsApp Bot

A Python bot that fetches the latest news, summarizes them using the Google Gemini model via LangChain, and sends the digest to your WhatsApp number daily using Twilio.

## Table of Contents

1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Configuration](#configuration)  
4. [Usage](#usage)  
5. [Project Structure](#project-structure)  
6. [Customization](#customization)  
7. [Future Improvements](#future-improvements)  
8. [Contributing](#contributing)  
9. [License](#license)  

## Features

- **Automated News Fetching**: Retrieves top headlines from GNews API (by category & country).  
- **Intelligent Summarization**: Uses Google Gemini (via LangChain) to produce concise, readable summaries.  
- **WhatsApp Delivery**: Delivers daily digests to your phone via Twilio’s WhatsApp API.  
- **Scheduling**: Uses the `schedule` library to run automatically at a set time each day.  
- **Easy Configuration**: API keys and phone numbers managed via environment variables.

## Tech Stack

- **Language**: Python  
- **LLM / Framework**: LangChain + Google Gemini  
- **News API**: GNews API  
- **Messaging**: Twilio (WhatsApp)  
- **Scheduler**: `schedule` Python library  
- **Other dependencies**: `python-dotenv`, `requests`

## Getting Started

### Prerequisites

- Python 3.8+  
- A Google Gemini API key  
- A GNews API key  
- A Twilio account with WhatsApp sandbox enabled  
- Your WhatsApp phone number (with country code)  
- `git` installed (if cloning repository)

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/VinayMarabe/news_summarizer.git
   cd news_summarizer
(Optional but recommended) Create and activate a virtual environment:

bash
Copy code
# On Unix / macOS
python3 -m venv venv
source venv/bin/activate

# On Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configuration
Create a file named .env in the project root directory.

Add the following environment variables (replace placeholders with actual values):

text
Copy code
# For summarization
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"

# For news fetching
GNEWS_API_KEY="YOUR_GNEWS_API_KEY"

# For WhatsApp via Twilio
TWILIO_ACCOUNT_SID="YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN="YOUR_TWILIO_AUTH_TOKEN"
TWILIO_WHATSAPP_NUMBER="whatsapp:+1415XXXXXXX"     # Your Twilio sandbox or WhatsApp number
MY_WHATSAPP_NUMBER="whatsapp:+91XXXXXXXXXX"       # Your personal WhatsApp number
Make sure your Twilio sandbox is configured to accept and send messages from your WhatsApp number.

Usage
Run the main script:

bash
Copy code
python main.py
You’ll be presented with options:

Send news summary now — triggers an immediate summary + send

Start scheduler (run daily at 08:00 AM) — schedule default

Custom schedule time — set a specific time (HH:MM, 24h format)

Once scheduled, the bot will fetch articles, generate summaries, and send them to your WhatsApp daily.

Project Structure
bash
Copy code
news_summarizer/
├── assets/
│   └── news.mp4                 # (demo / media, if any)
├── debug_fetch.py               # helper / debugging script for news fetch
├── fetch_news.py                # module to fetch news articles
├── summarize.py                 # module to summarize using Gemini & LangChain
├── main.py                       # entry point / CLI & scheduler logic
├── requirements.txt             # Python dependencies
└── README.md                     # Project documentation
fetch_news.py — handles GNews API calls and retrieving articles

summarize.py — builds prompts, interacts with Gemini via LangChain

main.py — user interface, scheduling, orchestrates fetch + summarize + send

debug_fetch.py — for debugging / testing news fetch logic

assets/ — media / demo files

Customization
Change the news categories or country by editing fetch logic in fetch_news.py.

Adjust summarization prompt, tone, length, etc., inside summarize.py.

You can extend to send via other channels (email, Telegram, etc.).

Add error handling, logging, retries, caching for robustness.

Future Improvements
Add logging with different levels (INFO / WARNING / ERROR)

Implement fallback mechanism if Gemini API fails

Rate limiting / batching for large news volumes

Better prompt engineering or fine-tuning summarization

A web UI or dashboard to configure times, categories, etc.

Dockerize or package as a service (cron / serverless)

Contributing
Contributions are welcome! If you find bugs or want to add features:

Fork the repository

Create a new branch (git checkout -b feature/YourFeature)

Commit your changes

Push to your fork

Raise a Pull Request describing your changes

Please ensure code is well documented and follows PEP8 / Python style guidelines.

License
Specify your license here. E.g.,
MIT License © 2025 [Your Name or Organization]
