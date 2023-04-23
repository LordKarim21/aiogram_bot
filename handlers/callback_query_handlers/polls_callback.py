from aiogram import types
from loader import dp
from states.polls import Poll


@dp.callback_query_handler(lambda call: call.data == 'polls')
async def survey(call: types.CallbackQuery):
    await Poll.question.set()
    await call.message.answer("Кол-во вариантов ответа варьируется от 2 до 6.\nВведите вопрос:")
