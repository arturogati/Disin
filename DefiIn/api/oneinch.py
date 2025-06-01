import aiohttp
from config.settings import settings

async def get_swap_data(from_token: str, to_token: str, amount: float, user_address: str) -> dict:
    url = (
        f"https://api.1inch.io/v5.0/1/swap"
        f"?fromTokenAddress={from_token}"
        f"&toTokenAddress={to_token}"
        f"&amount={amount}"
        f"&fromAddress={user_address}"
        f"&slippage=1"
    )
    
    headers = {"Authorization": f"Bearer {settings.ONEINCH_API_KEY}"}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            return await resp.json()
        

"""
api/oneinch.py (Интеграция с 1inch API)
Функционал:

Получение данных для свапа токенов

Формирование оптимальных маршрутов обмена

Пример запроса:


Особенности:
Использует асинхронные запросы через aiohttp для скорости.
"""