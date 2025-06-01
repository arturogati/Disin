from web3 import Web3
from config.settings import settings

w3 = Web3(Web3.HTTPProvider(settings.INFURA_URL))

def get_balance(address: str) -> float:
    return w3.from_wei(w3.eth.get_balance(address), 'ether')

def get_transaction_count(address: str) -> int:
    return w3.eth.get_transaction_count(address)

"""
core/blockchain.py (Работа с блокчейном)
Основные задачи:

Подключение к ноде Ethereum через Web3.py

Чтение данных из блокчейна:

Балансы кошельков (get_balance)

Номера транзакций (get_transaction_count)


Критические зависимости:
web3 – основной инструмент взаимодействия с Ethereum.
"""