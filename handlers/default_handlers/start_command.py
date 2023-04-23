from loader import dp
from aiogram import types
from keyboards.inline.start_button import inline_buttons


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.username}!", reply_markup=inline_buttons())
