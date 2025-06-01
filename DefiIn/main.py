import asyncio
from core.blockchain import w3, get_balance
from core.risk_engine import validate_pool_address
from core.transactions import sign_transaction
from api.oneinch import get_swap_data
from config.settings import settings

async def one_click_deposit(user_address: str, pool_address: str, amount_eth: float):
    # 1. Валидация
    if not validate_pool_address(pool_address):
        raise ValueError("Invalid pool address")
    
    if get_balance(user_address) < amount_eth:
        raise ValueError("Insufficient balance")

    # 2. Свап ETH в USDC
    swap_data = await get_swap_data(
        from_token="0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
        to_token="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        amount=w3.to_wei(amount_eth, 'ether'),
        user_address=user_address
    )

    # 3. Подпись транзакции
    tx_data = {
        'to': swap_data['tx']['to'],
        'data': swap_data['tx']['data'],
        'value': int(swap_data['tx']['value']),
        'gas': int(swap_data['tx']['gas']),
        'nonce': w3.eth.get_transaction_count(user_address)
    }
    
    tx_hash = sign_transaction(tx_data, settings.PRIVATE_KEY)
    print(f"Swap TX Hash: {tx_hash}")

if __name__ == "__main__":
    asyncio.run(one_click_deposit(
        user_address="0xYourAddress",
        pool_address=settings.TEST_POOL,
        amount_eth=0.1
    ))



"""
main.py (Ядро приложения)
Логика workflow:

Валидация входных данных

Обмен токенов через 1inch

Депозит в выбранный пул

Обработка результатов

Главный процесс:

python
async def one_click_deposit(user_address, pool_address, amount_eth):
    # 1. Проверка баланса
    # 2. Свап через 1inch
    # 3. Депозит в пул
    # 4. Подтверждение
Интеграция:
Объединяет все модули в единый pipeline.

"""