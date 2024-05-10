import os

from dotenv import load_dotenv

load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///db.sqlite3'

DATA_PARSE_URL = "https://www.google.com/finance/quote/USD-UAH"
