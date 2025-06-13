async def mock_get_swap_data(*args, **kwargs):
    return {
        "tx": {
            "to": "0xMockPool",
            "data": "0x1234",
            "value": str(int(0.1 * 1e18)),  # 0.1 ETH
            "gas": "200000"
        }
    }