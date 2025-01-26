import ccxt.pro
import asyncio

async def order_ccxt(order):
    """
    Function to place an order on an exchange using ccxt.pro
    :param order: Dictionary with order parameters
    :return: Result of the order placement or error information
    """
    exchange_name = order.get('exchange')
    sandbox_mode = order.get('sandbox_mode', False)
    api_key = order.get('api_key')
    secret_key = order.get('secret_key')
    market_type = order.get('market_type', 'spot')  # Added to specify spot or future

    # Initialize the exchange with API keys from order_data
    exchange_class = getattr(ccxt.pro, exchange_name)
    exchange = exchange_class({
        'apiKey': api_key,
        'secret': secret_key,
        'options': {
            'defaultType': market_type  # Use market_type to choose between 'spot' or 'future'
        }
    })

    if sandbox_mode:
        if exchange.has['sandbox']:
            exchange.set_sandbox_mode(True)

    try:
        await exchange.load_markets()

        order_type = order.get('type').lower()
        side = order.get('side').lower()
        symbol = order.get('symbol')
        amount = order.get('amount')
        params = order.get('params', {})

        # Handle market orders
        if order_type == 'market':
            response = await exchange.create_market_order(symbol, side, amount, params)
        
        # Placeholder for limit orders
        elif order_type == 'limit':
            # Future implementation for limit orders
            pass
        
        # Placeholder for stop orders
        elif order_type == 'stop':
            # Future implementation for stop orders
            pass
        
        # Placeholder for stop-limit orders
        elif order_type == 'stop_limit':
            # Future implementation for stop-limit orders
            pass
        
        # Placeholder for trailing stop orders
        elif order_type == 'trailing_stop':
            # Future implementation for trailing stop orders
            pass
        
        else:
            raise ValueError(f"Order type '{order_type}' is not yet implemented")

        return response

    except ccxt.BaseError as e:
        print(f"Error placing order: {str(e)}")
        return {'error': str(e)}
    finally:
        await exchange.close()

# Example of using the function
if __name__ == "__main__":
    order_data_spot = {
        'exchange': 'binance',
        'sandbox_mode': True,
        'api_key': 'YOUR_API_KEY',
        'secret_key': 'YOUR_SECRET_KEY',
        'market_type': 'spot',
        'symbol': 'BTC/USDT',
        'type': 'market',
        'side': 'buy',
        'amount': 0.001,
        'params': {
            'timeInForce': 'GTC'
    }
}

    order_data_future = {
        'exchange': 'binance',
        'sandbox_mode': True,
        'api_key': 'YOUR_API_KEY',
        'secret_key': 'YOUR_SECRET_KEY',
        'market_type': 'future',
        'symbol': 'BTC/USDT',
        'type': 'market',
        'side': 'buy',
        'amount': 0.001,
        'params': {
            'reduceOnly': 'false',
            'marginMode': 'cross'
    }
}

#    result = asyncio.run(order_ccxt(order_data_spot))
    result = asyncio.run(order_ccxt(order_data_future))
    print(result)
