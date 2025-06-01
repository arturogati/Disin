from enum import Enum
from .api_client import BankAPIClient, TaxAPIClient

class BusinessStatus(Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class BusinessVerifier:
    def __init__(self):
        self.bank_client = BankAPIClient()
        self.tax_client = TaxAPIClient()
    
    def verify(self, business_id: str) -> dict:
        bank_data = self.bank_client.fetch_transactions(business_id)
        tax_data = self.tax_client.fetch_tax_debts(business_id)
        
        avg_revenue = sum(bank_data["last_12m_revenue"]) / 12
        is_consistent = all(0.7 * avg_revenue < x < 1.3 * avg_revenue for x in bank_data["last_12m_revenue"])
        
        return {
            "status": BusinessStatus.APPROVED if is_consistent and tax_data["tax_debts"] == 0 else BusinessStatus.REJECTED,
            "avg_revenue": avg_revenue,
            "tax_debts": tax_data["tax_debts"]
        }


"""
Ответственность:
Проверка бизнеса перед токенизацией.

Что делает:

BusinessVerifier:

Запрашивает данные через BankAPIClient и TaxAPIClient.

Проверяет критерии:

Стабильность выручки (нет резких скачков).

Отсутствие налоговых долгов.

Возвращает статус (APPROVED/REJECTED).
"""