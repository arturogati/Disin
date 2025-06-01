from core.service import CryptoWillService
from core.models import Asset, AssetType

if __name__ == "__main__":
    service = CryptoWillService()
    
    # Создание контракта
    contract_address = service.create_will(
        owner="0xAlice",
        guardians=["0xBob", "0xCarol"],
        required_signatures=2,
        assets=[Asset(AssetType.ETH, 5.0)]
    )
    
    print(f"Contract deployed at: {contract_address}")



"""
app.py
Назначение: Точка входа для демонстрации.
Что делает:

Создает пример контракта наследования.

Выводит адрес созданного контракта.
Для чего нужен:

Быстрый старт для проверки работы.

Пример использования для разработчиков.

"""