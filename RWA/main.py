from blockchain.core import BlockchainSimulator, BusinessFinancials
from blockchain.contracts import TokenContract
from verification.verifier import BusinessVerifier

def setup_demo():
    blockchain = BlockchainSimulator()
    verifier = BusinessVerifier()
    
    # Регистрация бизнеса
    cafe = blockchain.register_business("Coffee House", 50000, 0.1)
    
    # Проверка бизнеса
    result = verifier.verify(cafe.id)
    print(f"Verification result: {result['status'].value}")
    
    if result["status"].value == "APPROVED":
        # Выпуск токенов
        contract = TokenContract(
            business_id=cafe.id,
            total_supply=100000,
            price_per_token=1.0
        )
        print(f"Tokens issued: {contract.total_supply}")
        
        # Обновляем финансовые данные
        cafe.financials = BusinessFinancials(
            avg_monthly_revenue=result["avg_revenue"],
            tax_debts=result["tax_debts"],
            last_audit_date="2023-11-20"
        )

if __name__ == "__main__":
    setup_demo()

"""
Ответственность:
Демонстрация работы всей системы.

Что делает:

Создает экземпляры BlockchainSimulator и BusinessVerifier.

Регистрирует бизнес и проверяет его.

Если проверка пройдена — выпускает токены.
"""