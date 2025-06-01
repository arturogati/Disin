from web3 import Web3
import os
from dotenv import load_dotenv
from core.models import CryptoWillContract

load_dotenv()

class Blockchain:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(os.getenv("INFURA_URL")))
        self.contracts = {}

    def deploy_contract(self, contract: CryptoWillContract) -> str:
        address = self.w3.eth.account.create().address
        self.contracts[address] = contract
        return address

    def get_contract(self, address: str) -> CryptoWillContract:
        return self.contracts.get(address)
    


"""
utils/blockchain.py
Назначение: Работа с блокчейном через Web3.py.
Что делает:

Подключается к Ethereum через Infura API.

Имитирует деплой контрактов (в тестах).
Для чего нужен:

Отправка реальных транзакций в mainnet/testnet.

Абстракция для работы с разными сетями (Ethereum, TON и др.).


"""