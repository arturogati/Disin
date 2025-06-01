from typing import List
from .models import CryptoWillContract, Asset, AssetType
from .signatures import verify_signature
from utils.blockchain import Blockchain
from utils.oracle import DeathOracle

class CryptoWillService:
    def __init__(self):
        self.blockchain = Blockchain()
        self.oracle = DeathOracle()

    def create_will(self, owner: str, guardians: List[str], 
                   required_signatures: int, assets: List[Asset]) -> str:
        contract = CryptoWillContract(
            owner=owner,
            guardians=guardians,
            required_signatures=required_signatures,
            assets=assets
        )
        return self.blockchain.deploy_contract(contract)

    def add_signature(self, contract_address: str, guardian: str, 
                     message: str, signature: str) -> bool:
        contract = self.blockchain.get_contract(contract_address)
        if not contract or not contract.is_active:
            return False
            
        if not verify_signature(message, signature, guardian):
            return False
            
        contract.signatures[guardian] = True
        return True
    

"""
core/service.py
Назначение: Основная бизнес-логика сервиса.
Что делает:

create_will: Создает новый контракт наследования.

add_signature: Обрабатывает подписи хранителей.
Для чего нужен:

Связывает модели данных, подписи и блокчейн.

Реализует сценарии использования (например, активацию наследства).

"""