from core.service import CryptoWillService
from core.models import Asset, AssetType
from eth_account import Account
import time

def demo():
    # Инициализация
    service = CryptoWillService()
    
    # Создаем тестовые аккаунты
    owner = Account.create()
    guardian1 = Account.create()
    guardian2 = Account.create()
    
    print("🔑 Аккаунты:")
    print(f"Владелец: {owner.address}")
    print(f"Хранители: {guardian1.address}, {guardian2.address}")

    # Создаем контракт
    contract_addr = service.create_will(
        owner=owner.address,
        guardians=[guardian1.address, guardian2.address],
        required_signatures=2,
        assets=[Asset(AssetType.ETH, 10.0)]
    )
    print(f"\n📜 Контракт создан: {contract_addr}")

    # Имитируем неактивность
    print("\n⏳ Имитируем 1 год неактивности...")
    contract = service.blockchain.get_contract(contract_addr)
    contract.last_activity = time.time() - 366 * 86400  # 366 дней назад

    # Проверяем триггеры
    print("\n🔍 Проверяем условия активации...")
    if service.check_triggers(contract_addr):
        print("✅ Условия выполнены! Собираем подписи...")
        
        # Хранители подписывают
        service.add_signature(contract_addr, guardian1.address)
        print(f"- {guardian1.address[:8]}... подписал")
        
        service.add_signature(contract_addr, guardian2.address)
        print(f"- {guardian2.address[:8]}... подписал")
        
        # Пытаемся разблокировать
        assets = service.release_assets(contract_addr)
        if assets:
            print("\n🎉 Активы разблокированы!")
            for asset in assets:
                print(f"  - {asset.amount} {asset.type.value}")
        else:
            print("\n❌ Не удалось разблокировать активы")
    else:
        print("❌ Условия не выполнены")

if __name__ == "__main__":
    print("🚀 Демонстрация работы CryptoWill")
    print("========================================")
    demo()
    print("========================================")