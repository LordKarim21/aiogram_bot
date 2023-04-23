from loader import dp
from aiogram import types
from utils.weather.get_weather import get_weather
from states.city import City
from aiogram.dispatcher import FSMContext

"""Команда /weather определяет текущую погоду в определенном городе"""


@dp.message_handler(commands="weather")
async def weather(message: types.Message):
    await City.city.set()
    await message.reply('Напишите какой город: ')


@dp.message_handler(state=City.city)
async def process_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        weather = await get_weather(message.text)
        await message.answer(text=weather)
        await state.finish()
