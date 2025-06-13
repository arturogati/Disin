from unittest.mock import Mock
from web3 import Web3

def get_mock_web3():
    mock = Mock(spec=Web3)
    mock.eth = Mock()
    mock.is_address = Mock(return_value=True)
    mock.to_wei = lambda x, _: int(x * 1e18)  # ETH → wei
    
    # Мокируем методы
    mock.eth.get_balance.return_value = int(10 * 1e18)  # 10 ETH
    mock.eth.get_transaction_count.return_value = 0
    mock.eth.send_raw_transaction.return_value = b'mock_tx_hash'
    
    return mock