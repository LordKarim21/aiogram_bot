from loader import dp
from aiogram import types
from utils.kitty_img.get_kitty_img import get_image

"""Команда /send_img отправлять случайную картинку с милыми кошками"""


@dp.message_handler(commands="send_img")
async def send_img(message: types.Message):
    await message.answer_photo(caption='Посмотри, какого котика я тебе нашёл', photo=get_image())
