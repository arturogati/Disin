import pytest
from blockchain.core import BlockchainSimulator, Business, Investor

@pytest.fixture
def blockchain():
    return BlockchainSimulator()

@pytest.fixture
def sample_business():
    return Business(
        id="test_biz_123",
        name="Test Cafe",
        revenue_per_month=50000,
        tokenized_share=0.1
    )

def test_register_business(blockchain):
    """Тест регистрации бизнеса"""
    biz = blockchain.register_business("Test Biz", 100000, 0.2)
    assert biz.name == "Test Biz"
    assert blockchain.businesses[biz.id] == biz

def test_register_investor(blockchain):
    """Тест регистрации инвестора"""
    inv = blockchain.register_investor("Alice", "0xAlice123")
    assert inv.name == "Alice"
    assert blockchain.investors[inv.id] == inv

def test_business_financials(sample_business):
    """Тест финансовых данных бизнеса"""
    sample_business.financials = {
        "avg_monthly_revenue": 52000,
        "tax_debts": 0,
        "last_audit_date": "2023-11-20"
    }
    assert sample_business.financials["avg_monthly_revenue"] == 52000