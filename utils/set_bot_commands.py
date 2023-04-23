from aiogram import types
from config_data.config import command


async def set_default_commands(dp):
    """
    Добавляет команды в бот
    :param dp:
    :return:
    """
    await dp.bot.set_my_commands(
            [types.BotCommand(*i) for i in command]
    )
