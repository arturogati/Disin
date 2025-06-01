from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Optional

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
    signatures: Dict[str, bool] = None
    
    def __post_init__(self):
        self.signatures = {guardian: False for guardian in self.guardians}



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