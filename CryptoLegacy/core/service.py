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

from typing import List
from core.models import CryptoWillContract, Asset
from utils.blockchain import Blockchain
from utils.oracle import DeathOracle

class CryptoWillService:
    def __init__(self):
        self.blockchain = Blockchain()
        self.oracle = DeathOracle()

    def create_will(self, owner: str, guardians: List[str],
                   required_signatures: int, assets: List[Asset],
                   inactivity_days: int = 365) -> str:
        contract = CryptoWillContract(
            owner=owner,
            guardians=guardians,
            required_signatures=required_signatures,
            assets=assets
        )
        return self.blockchain.deploy_contract(contract)

    def check_triggers(self, contract_address: str) -> bool:
        contract = self.blockchain.get_contract(contract_address)
        if not contract:
            return False
        return (contract.check_inactivity(365) or 
                self.oracle.check_death(contract.owner))

    def add_signature(self, contract_address: str, guardian: str) -> bool:
        contract = self.blockchain.get_contract(contract_address)
        if not contract or not contract.is_active:
            return False
        return contract.add_signature(guardian)

    def release_assets(self, contract_address: str) -> List[Asset]:
        contract = self.blockchain.get_contract(contract_address)
        if not contract or not contract.is_active:
            return []
        if not contract.can_release():
            return []
        
        contract.is_active = False
        return contract.assets
