from python_weather import Client, IMPERIAL


async def get_weather(city: str) -> str:
    """
    Используя пакет python_weather отправлю тестовое сообщение о погоде
    :param city:
    :return weather:
    """
    async with Client(format=IMPERIAL) as client:
        weather = await client.get(city)
    temperature = str(weather.current.temperature) + '°C'  # темпиратура
    description = weather.current.description
    humidity = str(weather.current.humidity) + '%'  # Влажность, %
    wind_speed = str(weather.current.wind_speed) + 'м/с'  # Скорость ветра m/c
    return f'Город: {city.capitalize()}\n' \
           f'Погода: {description}\n' \
           f'Температура: {temperature}\n' \
           f'Скорость ветра: {wind_speed}\n' \
           f'Влажность: {humidity}'
