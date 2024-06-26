# Exchange - Rate - Bot

A Telegram bot with which you can receive information about the dynamics
of the dollar to hryvnia exchange rate using the /get_exchange_rate command.
### Installing using GitHub

1. Clone the source code:

```bash
git clone https://github.com/MykytaKuzmytskyi/exchange_rate.git
cd exchange_rate
```

2. Install modules and dependencies:

```bash
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

3. `.env_sample`
This is a sample .env file for use in local development.
 Copy this file as `.env` in the root of your project
 and update the environment variables according to your unique variables.
   - **TELEGRAM_BOT_TOKEN:**: https://sendpulse.ua/ru/knowledge-base/chatbot/telegram/create-telegram-chatbot

4. Add an existing or newly created Telegram bot to the chat.

5. Start the app:

```bash
python runner.py
```
