from aiogram import executor

from loader import dp
import middlewares, handlers
from utils.notify_admin import on_startup_notify


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
