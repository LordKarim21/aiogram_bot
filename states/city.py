from aiogram.dispatcher.filters.state import State, StatesGroup


class City(StatesGroup):
    """
    Для определения текущую погоду в определенном городе
    """
    city = State()
