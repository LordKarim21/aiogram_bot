from loader import dp
from aiogram import types
from states.city import City


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'weather')
async def weather(call: types.CallbackQuery):
    await City.city.set()
    await call.message.reply('Напишите какой город: ')
