"""
Ответственность:
Демонстрация работы всей системы.

Что делает:

Создает экземпляры BlockchainSimulator и BusinessVerifier.

Регистрирует бизнес и проверяет его.

Если проверка пройдена — выпускает токены.
"""

from blockchain.core import BlockchainSimulator, BusinessFinancials, Investor
from blockchain.contracts import TokenContract
from verification.verifier import BusinessVerifier
from datetime import datetime

def run_full_demo():
    print("=== Демонстрация работы платформы токенизации ===")
    
    # Инициализация системы
    blockchain = BlockchainSimulator()
    verifier = BusinessVerifier()
    
    # 1. Регистрация бизнеса (аргументы должны соответствовать определению класса)
    print("\n1. Регистрация бизнеса")
    cafe = blockchain.register_business(
        name="Coffee House", 
        revenue=50000,  # Было revenue_per_month, должно быть revenue
        share=0.1
    )
    print(f"Зарегистрирован бизнес: {cafe.name} (ID: {cafe.id[:8]}...)")
    
    # 2. Верификация бизнеса
    print("\n2. Проверка бизнеса через API")
    print("Запрашиваем данные из банковского API и налоговой...")
    verification_result = verifier.verify(cafe.id)
    
    print(f"\nРезультат проверки: {verification_result['status'].value}")
    print(f"Средняя выручка: ${verification_result['avg_revenue']:,.2f}/мес")
    print(f"Налоговые долги: ${verification_result['tax_debts']:,.2f}")
    
    if verification_result["status"].value != "APPROVED":
        print("\nБизнес не прошел проверку. Токенизация невозможна.")
        return
    
    # 3. Выпуск токенов
    print("\n3. Выпуск токенов бизнеса")
    contract = TokenContract(
        business_id=cafe.id,
        total_supply=100_000,
        price_per_token=1.00
    )
    
    # Сохраняем финансовые данные
    cafe.financials = BusinessFinancials(
        avg_monthly_revenue=verification_result["avg_revenue"],
        tax_debts=verification_result["tax_debts"],
        last_audit_date=datetime.now().strftime("%Y-%m-%d")
    )
    
    print(f"Выпущено {contract.total_supply:,} токенов по ${contract.price_per_token:.2f}")
    print(f"Каждый токен дает право на {cafe.tokenized_share*100}% от выручки")
    
    # 4. Регистрация инвесторов
    print("\n4. Регистрация инвесторов")
    alice = blockchain.register_investor("Alice", "0xAlice123")
    bob = blockchain.register_investor("Bob", "0xBob456")
    
    print(f"Зарегистрированы инвесторы: {alice.name} и {bob.name}")
    
    # 5. Покупка токенов
    print("\n5. Покупка токенов инвесторами")
    alice_tokens = 50_000
    bob_tokens = 30_000
    
    alice.tokens[cafe.id] = alice_tokens
    bob.tokens[cafe.id] = bob_tokens
    
    print(f"{alice.name} покупает {alice_tokens:,} токенов за ${alice_tokens:,.2f}")
    print(f"{bob.name} покупает {bob_tokens:,} токенов за ${bob_tokens:,.2f}")
    
    # 6. Выплата дивидендов
    print("\n6. Выплата дивидендов (после месяца работы)")
    monthly_revenue = 55_000
    revenue_share = monthly_revenue * cafe.tokenized_share
    dividend_per_token = contract.calculate_dividends(revenue_share)
    
    print(f"\nВыручка кафе за месяц: ${monthly_revenue:,.2f}")
    print(f"10% от выручки на дивиденды: ${revenue_share:,.2f}")
    print(f"Дивиденд на 1 токен: ${dividend_per_token:.4f}")
    
    alice_payout = alice_tokens * dividend_per_token
    bob_payout = bob_tokens * dividend_per_token
    
    print(f"\nВыплаты инвесторам:")
    print(f"{alice.name}: {alice_tokens:,} ток. × ${dividend_per_token:.4f} = ${alice_payout:,.2f}")
    print(f"{bob.name}: {bob_tokens:,} ток. × ${dividend_per_token:.4f} = ${bob_payout:,.2f}")
    
    contract.dividend_payments.append(dividend_per_token)
    
    print("\n=== Токенизация успешно завершена ===")

if __name__ == "__main__":
    run_full_demo()