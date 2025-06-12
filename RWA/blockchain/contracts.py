"""
Ответственность:
Логика смарт-контрактов для токенизации.

Что делает:

TokenContract — модель контракта:

Хранит параметры токенов (цена, общее количество).

Рассчитывает дивиденды (calculate_dividends).

Фиксирует историю выплат (dividend_payments).
"""

from dataclasses import dataclass
from typing import List

@dataclass
class TokenContract:
    business_id: str
    total_supply: int
    price_per_token: float
    dividend_payments: List[float] = None

    def __post_init__(self):
        self.dividend_payments = []
    
    def calculate_dividends(self, revenue_share: float) -> float:
        return revenue_share / self.total_supply