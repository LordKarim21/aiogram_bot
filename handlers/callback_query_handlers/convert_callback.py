from loader import dp
from aiogram import types
from keyboards.inline.convert_button import currency_buttons
from states.currency import Currency


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'convert')
async def convert(call: types.CallbackQuery):
    await Currency.volute_from.set()
    await call.message.answer('Напишите с какой волюты: ', reply_markup=await currency_buttons())
