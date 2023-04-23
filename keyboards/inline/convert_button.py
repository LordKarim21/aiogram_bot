from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def currency_buttons():
    """
    Кнопки конвертора
    :return:
    """
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons1 = [
        InlineKeyboardButton(text='RUB', callback_data='RUB'),
        InlineKeyboardButton(text='EUR', callback_data='EUR')
    ]

    buttons2 = [
        InlineKeyboardButton(text='GBP', callback_data='GBP'),
        InlineKeyboardButton(text='USD', callback_data='USD')
    ]

    keyboard.add(*buttons1)
    keyboard.add(*buttons2)
    return keyboard
