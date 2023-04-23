from loader import dp
from aiogram import types
from utils.kitty_img.get_kitty_img import get_image


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'send_img')
async def send_img(call: types.CallbackQuery):
    await call.message.reply_photo(caption='Посмотри, какого котика я тебе нашёл', photo=get_image())
