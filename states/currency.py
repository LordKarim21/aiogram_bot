from aiogram.dispatcher.filters.state import State, StatesGroup


class Currency(StatesGroup):
    """
    Для определения с какой валюты в какую валюту конвертировать
    """
    volute_from = State()
    volute_to = State()
    amount = State()
