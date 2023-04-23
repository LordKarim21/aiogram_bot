from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_buttons():
    """
    Стартовые кнопки
    :return:
    """
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(
            text='Определяет текущую погоду в определенном городе',
            callback_data='weather'
        ),
        InlineKeyboardButton(
            text='Конвертировать валюты',
            callback_data='convert'
        ),
        InlineKeyboardButton(
            text='Отправлять случайную картинку с милыми кошками',
            callback_data='send_img'
        ),
        InlineKeyboardButton(
            text='Создавать опросы',
            callback_data='polls'
        )
    ]
    for button in buttons:
        keyboard.add(button)
    return keyboard
