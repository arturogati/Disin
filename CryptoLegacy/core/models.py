"""
Назначение: Модели данных на Python.
Что содержит:

AssetType: Перечисление типов активов (ETH, BTC, NFT).

Asset: Описывает криптоактив (тип, количество, контракт для NFT).

CryptoWillContract: Основной контракт с правилами наследования.
Для чего нужен:

Универсальное представление данных в коде.

Валидация входных параметров (через dataclasses).

"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional
import time

class AssetType(Enum):
    ETH = "ETH"
    BTC = "BTC"
    NFT = "NFT"

@dataclass
class Asset:
    type: AssetType
    amount: float = 0.0
    contract_address: Optional[str] = None

@dataclass
class CryptoWillContract:
    owner: str
    guardians: List[str]
    required_signatures: int
    assets: List[Asset]
    is_active: bool = True
    last_activity: float = field(default_factory=time.time)
    signatures: Dict[str, bool] = field(default_factory=dict)

    def check_inactivity(self, days: int) -> bool:
        """Проверяет, был ли владелец неактивен N дней"""
        return (time.time() - self.last_activity) > (days * 86400)

    def can_release(self) -> bool:
        """Проверяет, собрано ли достаточно подписей"""
        return sum(self.signatures.values()) >= self.required_signatures

    def add_signature(self, guardian: str) -> bool:
        """Добавляет подпись хранителя"""
        if guardian in self.guardians:
            self.signatures[guardian] = True
            return True
        return False