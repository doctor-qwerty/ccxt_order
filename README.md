### Package Description


This package provides an interface for placing orders on cryptocurrency exchanges using the https://github.com/ccxt library. It supports different order types and allows switching between spot and futures markets. The package is designed to simplify interaction with exchanges and automate trading operations.

### Package structure:

```
ccxt_order_package/
│
├── ccxt_order/
│   ├── __init__.py             # Package initialization
│   ├── ccxt_order.py           # Basic logic of order placement
│
├── tests/
│   ├── __init__.py             # Test initialization
│   ├── test_market_order_future.py  # Tests for futures orders
│   ├── test_market_order_spot.py    # Tests for spot orders
│
├── pyproject.toml              
└── README.md                   
```

---
### Execution of the Order:
Use the order_ccxt function to place an order:

```python
import asyncio

result = asyncio.run(order_ccxt(order_data))
print(result)
```
### Start testing:

```
poetry run pytest
```

### Example of Parameters for Spot Order:

```python
order_data_spot = {
    'exchange': 'binance',        # Name of the exchange on which the order will be placed
    'sandbox_mode': True,         # Whether to use sandbox mode for testing
    'api_key': 'YOUR_API_KEY',    # API key for access to the exchange
    'secret_key': 'YOUR_SECRET_KEY', # Secret key to access the exchange
    'market_type': 'spot',        # Market type: 'spot' for spot trading
    'symbol': 'BTC/USDT',         # Trading pair in “BASE/QUOTE” format
    'type': 'market',             # Order type: 'market' for market order
    'side': 'buy',                # Order side: 'buy' to buy or 'sell' to sell
    'amount': 0.001,              # Quantity of underlying asset to buy or sell
    'params': {                   # Additional order parameters
        'timeInForce': 'GTC'      # Order validity time: 'GTC' (Good-Til-Canceled)
    }
}
```

### Example of Parameters for Future Order:

```python
order_data_future = {
    'exchange': 'binance',        # Name of the exchange on which the order will be placed
    'sandbox_mode': True,         # Whether to use sandbox mode for testing
    'api_key': 'YOUR_API_KEY',    # API key for access to the exchange
    'secret_key': 'YOUR_SECRET_KEY', # Secret key to access the exchange
    'market_type': 'future',      # Market type: 'future' for spot trading
    'symbol': 'BTC/USDT',         # Trading pair in “BASE/QUOTE” format
    'type': 'market',             # Order type: 'market' for market order
    'side': 'buy',                # Order side: 'buy' to buy or 'sell' to sell
    'amount': 0.001,              # Quantity of underlying asset to buy or sell
    'params': {                   # Additional order parameters
        'reduceOnly': 'false',    # Parameter indicating that the order only reduces the position (false to open a new position)
        'marginMode': 'cross'     # Margin mode: 'cross' for cross margin or 'isolated' for isolated margin
    }
}
```

