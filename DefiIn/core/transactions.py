from eth_account import Account
from web3 import Web3
from core.blockchain import w3

def sign_transaction(tx_data: dict, private_key: str) -> str:
    signed = Account.sign_transaction(tx_data, private_key)
    return w3.eth.send_raw_transaction(signed.rawTransaction).hex()


"""
core/transactions.py (Подпись транзакций)
Ответственность:

Подпись сырых транзакций через eth-account

Отправка подписанных транзакций в сеть

Ключевая функция:


Безопасность:
Приватные ключи должны передаваться только в зашифрованном виде!

"""