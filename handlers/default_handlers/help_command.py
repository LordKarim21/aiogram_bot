from aiogram import types
from loader import dp
from config_data.config import command


@dp.message_handler(commands="help")
async def start(message: types.Message):
    text = [f'{cmd} - {description}' for cmd, description in command]
    await message.answer('\n'.join(text))
