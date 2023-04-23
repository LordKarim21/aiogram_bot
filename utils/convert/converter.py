import aiohttp


async def get_amount(volute_from: str, volute_to: str, amount: int) -> int:
    """
    Отправляет запрос на сайт и обрабатывает ответ о отправляя конвертируемую сумму
    :param volute_from:
    :param volute_to:
    :param amount:
    :return converted_amount:
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://open.er-api.com/v6/latest/{volute_from}") as resp:
            data = await resp.json()
    if data["result"] == "success":
        value = data["rates"][volute_to]
        return round(int(value) * amount, 2)

