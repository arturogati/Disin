"""

Что проверяет:

Создание контракта.

Проверку подписей.

Работу оракула.
Для чего нужен:

Гарантия корректности кода.

Предотвращение регрессий при изменениях.

"""


import pytest
from eth_account import Account
from web3 import Web3

def test_contract_creation(mock_service, sample_assets, sample_guardians):
    # Создаем контракт
    contract_addr = mock_service.create_will(
        owner="0xOwner",
        guardians=sample_guardians,
        required_signatures=2,
        assets=sample_assets
    )
    
    # Проверяем результат
    assert contract_addr is not None
    assert len(mock_service.blockchain.contracts) == 1

def test_signature_verification(mock_service, sample_guardians):
    # 1. Создаем контракт
    contract_addr = mock_service.create_will(
        owner="0xOwner",
        guardians=sample_guardians,
        required_signatures=2,
        assets=[]
    )
    
    # 2. Генерируем тестовую подпись
    priv_key = "0x" + "1"*64  # Приватный ключ для теста
    guardian = Account.from_key(priv_key)
    message = Web3.keccak(text="ReleaseAssets")
    signed = Account.sign_message({"message": message}, priv_key)
    
    # 3. Проверяем подпись
    assert mock_service.add_signature(
        contract_addr,
        guardian.address,
        message.hex(),
        signed.signature.hex()
    )

def test_asset_release(mock_service, sample_assets):
    # 1. Настраиваем оракул на "смерть"
    mock_service.oracle.is_dead = True
    
    # 2. Создаем контракт
    contract_addr = mock_service.create_will(
        owner="0xOwner",
        guardians=["0xG1", "0xG2"],
        required_signatures=1,
        assets=sample_assets
    )
    
    # 3. Активируем release
    released = mock_service.release_assets(contract_addr)
    assert len(released) == len(sample_assets)
