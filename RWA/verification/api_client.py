import random
from datetime import datetime, timedelta

class BankAPIClient:
    @staticmethod
    def fetch_transactions(business_id: str) -> dict:
        return {
            "last_12m_revenue": [random.uniform(40000, 60000) for _ in range(12)],
            "last_update": datetime.now().isoformat()
        }

class TaxAPIClient:
    @staticmethod
    def fetch_tax_debts(business_id: str) -> dict:
        return {
            "tax_debts": random.choice([0, 0, 0, 1000]),
            "last_report_date": (datetime.now() - timedelta(days=30)).isoformat()
        }
    

"""
Ответственность:
Имитация внешних API для проверки бизнеса.

Что делает:

BankAPIClient — "подключается" к Open Banking (Plaid/Tink):

Возвращает фейковые данные о выручке за 12 месяцев.

TaxAPIClient — проверяет налоги:

Генерирует случайные налоговые долги (25% шанс).

Зачем:
Для тестирования логики верификации без реальных запросов.
"""