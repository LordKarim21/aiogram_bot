import handlers
from loader import dp
from aiogram import executor
from utils.set_bot_commands import set_default_commands
import asyncio


async def main(dispatcher):
    await set_default_commands(dispatcher)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=main, skip_updates=True)
