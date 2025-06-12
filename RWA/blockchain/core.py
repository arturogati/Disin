"""
Ответственность:
Ядро симуляции блокчейна — управление бизнесами, инвесторами и базовыми операциями.

Что делает:

Содержит дата-классы для ключевых сущностей:

Business — данные бизнеса (выручка, доля токенизации).

Investor — информация об инвесторах (кошельки, токены).

BusinessFinancials — финансовые показатели (аудит).

BlockchainSimulator — класс для:

Регистрации бизнесов (register_business).

Добавления инвесторов (register_investor).

Хранения состояния (словари businesses, investors).

"""


from dataclasses import dataclass
from typing import Dict, List
from uuid import uuid4

@dataclass
class Business:
    id: str
    name: str
    revenue_per_month: float
    tokenized_share: float
    tokens_issued: int = 0
    financials: 'BusinessFinancials' = None

@dataclass
class Investor:
    id: str
    name: str
    wallet: str
    tokens: Dict[str, int]  # {business_id: amount}

@dataclass
class BusinessFinancials:
    avg_monthly_revenue: float
    tax_debts: float
    last_audit_date: str

class BlockchainSimulator:
    def __init__(self):
        self.businesses: Dict[str, Business] = {}
        self.investors: Dict[str, Investor] = {}
    
    def register_business(self, name: str, revenue: float, share: float) -> Business:
        business = Business(
            id=str(uuid4()),
            name=name,
            revenue_per_month=revenue,
            tokenized_share=share
        )
        self.businesses[business.id] = business
        return business
    
    def register_investor(self, name: str, wallet: str) -> Investor:
        investor = Investor(
            id=str(uuid4()),
            name=name,
            wallet=wallet,
            tokens={}
        )
        self.investors[investor.id] = investor
        return investor