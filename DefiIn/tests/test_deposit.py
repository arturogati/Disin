from core.risk_engine import validate_pool_address

def test_pool_validation():
    assert validate_pool_address("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48") is True
    assert validate_pool_address("0x0") is False