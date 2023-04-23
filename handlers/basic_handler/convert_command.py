from loader import dp
from aiogram import types
from utils.convert.converter import get_amount
from keyboards.inline.convert_button import currency_buttons
from states.currency import Currency
from aiogram.dispatcher import FSMContext

"""Команда /convert конвертирует валюту"""


@dp.message_handler(commands="convert")
async def convert(message: types.Message):
    await Currency.volute_from.set()
    await message.answer('Напишите с какой волюты: ', reply_markup=await currency_buttons())


@dp.callback_query_handler(state=Currency.volute_from)
async def process_volute_from(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['volute_from'] = call.data
        await Currency.volute_to.set()
        await call.message.answer('Напишите в какую валюту: ', reply_markup=await currency_buttons())


@dp.callback_query_handler(state=Currency.volute_to)
async def process_volute_to(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['volute_to'] = call.data
        await Currency.amount.set()
        await call.message.answer('Напишите значение конвертируемой суммы: ')


@dp.message_handler(state=Currency.amount)
async def process_amount(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount'] = message.text
        amount = await get_amount(data['volute_from'], data['volute_to'], int(data['amount']))
        await message.answer(
            text=f'{data["amount"]} {data["volute_from"]} => {str(amount)} {data["volute_to"]}'
        )
        await state.finish()
