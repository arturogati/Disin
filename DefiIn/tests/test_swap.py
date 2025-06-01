import pytest
from api.oneinch import get_swap_data

@pytest.mark.asyncio
async def test_swap():
    data = await get_swap_data(
        from_token="0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE",
        to_token="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        amount=10**18,
        user_address="0x0000000000000000000000000000000000000000"
    )
    assert 'tx' in data