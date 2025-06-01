from eth_account import Account
from eth_keys.datatypes import PrivateKey
from web3 import Web3

def sign_message(message: str, private_key: str) -> dict:
    """Подпись сообщения с использованием ECDSA."""
    account = Account.from_key(private_key)
    signed = Account.sign_message(
        {"message": Web3.keccak(text=message)},
        private_key
    )
    return {
        "signature": signed.signature.hex(),
        "address": account.address
    }

def verify_signature(message: str, signature: str, expected_address: str) -> bool:
    """Проверка подписи."""
    message_hash = Web3.keccak(text=message)
    address = Account.recover_message(
        {"message": message_hash},
        signature=signature
    )
    return address.lower() == expected_address.lower()


"""
core/signatures.py
Назначение: Криптографические операции с подписями.
Что делает:

sign_message: Подписывает сообщение приватным ключом (ECDSA).

verify_signature: Проверяет, что подпись соответствует адресу.
Для чего нужен:

Безопасное подтверждение действий хранителей.

Интеграция с Ethereum (алгоритм secp256k1).

"""