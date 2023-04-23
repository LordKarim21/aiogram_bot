import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

#  Ключ
BOT_TOKEN = os.getenv('BOT_TOKEN')

#  Команды
command = (
    ('start', "Запустить бота"),
    ('help', 'Вывести справку'),
    ('weather', 'Определяет текущую погоду в определенном городе'),
    ('convert', 'Конвертировать валюты'),
    ('send_img', 'Отправлять случайную картинку с милыми животными'),
    ('polls', 'Создавать опросы')
)
