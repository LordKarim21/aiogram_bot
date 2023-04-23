from aiogram.dispatcher.filters.state import StatesGroup, State


class Poll(StatesGroup):
    """
    Для создания опроса
    """
    question = State()
    count = State()
    position = State()
    is_anonymous = State()
    answers = State()
