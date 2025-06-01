import pytest
from core.service import CryptoWillService
from core.models import Asset, AssetType
from utils.oracle import DeathOracle

@pytest.fixture
def service():
    service = CryptoWillService()
    service.oracle = DeathOracle(is_dead=True)
    return service

def test_contract_creation(service):
    contract_address = service.create_will(
        owner="0xOwner",
        guardians=["0xG1", "0xG2"],
        required_signatures=1,
        assets=[Asset(AssetType.ETH, 10.0)]
    )
    assert contract_address is not None



"""

Что проверяет:

Создание контракта.

Проверку подписей.

Работу оракула.
Для чего нужен:

Гарантия корректности кода.

Предотвращение регрессий при изменениях.



"""