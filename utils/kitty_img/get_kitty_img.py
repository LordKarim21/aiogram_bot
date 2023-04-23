import requests
from loader import logger


def get_image() -> str:
    """
    Получить картинку котика и отправляет ее ссылку

    :return url:
    """
    try:
        response = requests.get('https://api.thecatapi.com/v1/images/search').json()
    except Exception as error:
        logger.error(f'Ошибка при запросе к основному API: {error}')
        response = requests.get('https://api.thedogapi.com/v1/images/search').json()
    return response[0].get('url')
