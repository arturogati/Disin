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


#!/usr/bin/env python3
import asyncio
import sys
from web3 import Web3
from eth_account import Account
from typing import Dict, Any

# --- Конфигурация режимов ---
IS_DEMO = "--demo" in sys.argv

if IS_DEMO:
    print("\n🔹 ДЕМО-РЕЖИМ: Используются мок-данные")
    from tests.mocks.blockchain import get_mock_web3
    from tests.mocks.oneinch import mock_get_swap_data as get_swap_data
    w3 = get_mock_web3()
else:
    from core.blockchain import w3
    from api.oneinch import get_swap_data
    from config.settings import settings

# --- Константы ---
ETH_ADDRESS = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
USDC_ADDRESS = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

# --- Основная логика ---
async def one_click_deposit(
    user_address: str,
    pool_address: str,
    amount_eth: float
) -> Dict[str, Any]:
    """Основной процесс депозита с автоматическим свапом"""
    
    # 1. Валидация адресов
    if not Web3.is_address(user_address):
        raise ValueError(f"Неверный адрес кошелька: {user_address}")
    
    if not Web3.is_address(pool_address):
        raise ValueError(f"Неверный адрес пула: {pool_address}")

    checksum_address = Web3.to_checksum_address(user_address)

    # 2. Проверка баланса
    balance_wei = w3.eth.get_balance(checksum_address)
    balance_eth = Web3.from_wei(balance_wei, 'ether')
    
    print(f"\n1. Проверяем баланс... {balance_eth:.4f} ETH")
    if balance_eth < amount_eth:
        raise ValueError(f"Недостаточно ETH. Нужно: {amount_eth}, есть: {balance_eth}")

    # 3. Обмен ETH → USDC через 1inch
    print(f"2. Инициируем обмен {amount_eth} ETH на USDC...")
    swap_data = await get_swap_data(
        from_token=ETH_ADDRESS,
        to_token=USDC_ADDRESS,
        amount=Web3.to_wei(amount_eth, 'ether'),
        user_address=checksum_address
    )

    # 4. Подготовка транзакции депозита
    print(f"3. Подготавливаем депозит в пул {pool_address[:10]}...")
    tx_data = {
        'to': swap_data['tx']['to'],
        'data': swap_data['tx']['data'],
        'value': int(swap_data['tx']['value']),
        'gas': int(swap_data['tx']['gas']),
        'nonce': w3.eth.get_transaction_count(checksum_address),
        'chainId': 1  # Ethereum Mainnet
    }

    # 5. Подпись и отправка (или мок в демо-режиме)
    if IS_DEMO:
        tx_hash = "0x" + "mock_hash".ljust(64, '0')
    else:
        signed_tx = Account.sign_transaction(tx_data, settings.PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()

    print(f"\n✅ Успешно! Транзакция: {tx_hash}")
    return {
        'status': 'success',
        'tx_hash': tx_hash,
        'amount_eth': amount_eth,
        'pool_address': pool_address
    }

# --- Точка входа ---
if __name__ == "__main__":
    # Параметры по умолчанию
    params = {
        'user_address': "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",  # Пример валидного адреса
        'pool_address': "0x5777d92f208679DB4b9778590Fa3CAB3aC9e2168",  # Пример пула (DAI-USDC)
        'amount_eth': 0.01
    }

    # Переопределение параметров из аргументов
    if len(sys.argv) > 1 and not sys.argv[1] == "--demo":
        params['user_address'] = sys.argv[1]
    if len(sys.argv) > 2 and not sys.argv[2] == "--demo":
        params['pool_address'] = sys.argv[2]
    if len(sys.argv) > 3 and not sys.argv[3] == "--demo":
        params['amount_eth'] = float(sys.argv[3])

    try:
        result = asyncio.run(one_click_deposit(**params))
        if IS_DEMO:
            print("\n[ДЕМО] Итоговые данные:", result)
    except Exception as e:
        print(f"\n❌ Ошибка: {str(e)}")
        if not IS_DEMO:
            print("Проверьте:")
            print("- Достаточно ли ETH на балансе")
            print("- Корректность адресов")
            print("- Подключение к интернету")
