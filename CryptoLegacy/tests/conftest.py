import pytest
from core.service import CryptoWillService
from core.models import Asset, AssetType
from utils.blockchain import MockBlockchain
from utils.oracle import DeathOracle

@pytest.fixture
def mock_service():
    service = CryptoWillService()
    service.blockchain = MockBlockchain()  # Переопределяем реальный блокчейн
    service.oracle = DeathOracle(is_dead=False)
    return service

@pytest.fixture
def sample_assets():
    return [
        Asset(type=AssetType.ETH, amount=5.0),
        Asset(type=AssetType.BTC, amount=0.1)
    ]

@pytest.fixture
def sample_guardians():
    return ["0xGuardian1", "0xGuardian2", "0xGuardian3"]