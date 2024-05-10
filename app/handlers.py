import os

import pandas as pd
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

from app.database.crud import get_rate_list
from app.database.models import ExchangeRate

router = Router()


def generate_excel_file(name: str, rate_list: [ExchangeRate]):
    df = pd.DataFrame([(item.time, item.rate) for item in rate_list], columns=['Time', 'Rate'])
    df.to_excel(name, index=False)


@router.message(CommandStart())
async def cmd_test1(message: Message):
    await message.answer("Hello! Try to use /get_exchange_rate command")


@router.message(Command("get_exchange_rate"))
async def get_list_rates(message: Message):
    rate_list = await get_rate_list()
    generate_excel_file("exchange_rate_report.xlsx", rate_list)
    await message.reply_document(
        document=FSInputFile("exchange_rate_report.xlsx")
    )
    os.remove("exchange_rate_report.xlsx")
