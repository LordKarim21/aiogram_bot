import re

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.polls import Poll

"""Команда /polls создавать опрос"""


@dp.message_handler(commands="polls")
async def survey(message: types.Message):
    await Poll.question.set()
    await message.answer("Кол-во вариантов ответа варьируется от 2 до 6.\nВведите вопрос:")


@dp.message_handler(state=Poll.question, content_types=types.ContentTypes.TEXT)
async def get_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question'] = message.text
        await Poll.is_anonymous.set()
        await message.answer('Введите будет ли анонимный опрос (Да/Нет):')


@dp.message_handler(state=Poll.is_anonymous, content_types=types.ContentTypes.TEXT)
async def get_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if re.findall('нет', message.text.lower()):
            data['is_anonymous'] = False
        else:
            data['is_anonymous'] = True
        await Poll.count.set()
        await message.answer('Введите количество вариантов ответа:')


@dp.message_handler(state=Poll.count, content_types=types.ContentTypes.TEXT)
async def get_count(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.isdigit() and 1 < int(message.text) < 7:
            data['count'] = message.text
            await Poll.answers.set()
            await message.answer(
                f"Количество успешно сохранено!\n"
                f"Введите вариант ответа № 1 или закончите создание опроса."
            )
        else:
            await Poll.count.set()
            await message.answer('Введите количество вариантов ответа:')


@dp.message_handler(state=Poll.answers, content_types=types.ContentTypes.TEXT)
async def get_answers(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['answers'] = data['answers'] + ', ' + message.text
        except KeyError:
            data['answers'] = message.text
        count = int(data['count'])
        answer_len = len(data['answers'].split(', '))

        if count > answer_len:
            await Poll.answers.set()
            await message.answer(f"Вариант № {answer_len} успешно сохранен!\n"
                                 f"Введите вариант ответа № {answer_len + 1} "
                                 f"или закончите создание опроса.")
        elif count == answer_len:
            await Poll.position.set()
            await message.answer(f"Вариант № {count} успешно сохранен!\n"
                                 f"Введите верный вариант ответа: ")


@dp.message_handler(state=Poll.position, content_types=types.ContentTypes.TEXT)
async def get_position(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['position'] = message.text
        position = data['answers'].split(', ').index(message.text)
        await message.answer_poll(
            question=data['question'],
            options=data['answers'].split(', '),
            is_anonymous=data['is_anonymous'],
            correct_option_id=position
        )
        del data['answers']
        await state.finish()
