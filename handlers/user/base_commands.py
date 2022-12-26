from aiogram import types
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from loader import dp


@dp.message_handler(CommandStart(), state=None)
async def start(message: types.Message):
    await message.answer(text=f"Assalomu alaykum {message.from_user.full_name}!")
