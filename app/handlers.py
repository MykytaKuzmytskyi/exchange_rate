from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_test1(message: Message):
    await message.answer("Hello! Try to use /get_exchange_rate command")
