import logging

from aiogram import Dispatcher

from decouple import config


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(config('ADMIN'), "Bot ishga tushdi")

    except Exception as err:
        logging.exception(err)
