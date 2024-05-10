import requests
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from bs4 import BeautifulSoup
from datetime import datetime

from app.database.crud import set_rate
from config import DATA_PARSE_URL


def parse_exchange_rate():
    page = requests.get(DATA_PARSE_URL).content
    soup = BeautifulSoup(page, "html.parser")
    rate = float(soup.find("div", {"jsname": "LXPcOd"}).text)
    return rate


async def store_exchange_rate():
    rate = parse_exchange_rate()
    current_time = (
        datetime.now()
        .replace(second=0, microsecond=0)
    )
    await set_rate(time=current_time, rate=rate)


def start_exchange_rate_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(store_exchange_rate, trigger=CronTrigger(minute='0'))
    scheduler.start()
