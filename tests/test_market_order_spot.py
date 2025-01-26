import ccxt.pro
import asyncio
import time
import pytest

@pytest.mark.asyncio
async def test_market_order():
    # Replace these values with your actual API credentials and desired parameters
    exchange_name = 'binance'
    api_key = 'dCDo9PdSzlXpkvJGMbrmrn3Lj1C5rCNyeHyYLU06OcqiHo8IUBCzTLNAIvSW9aKd'
    secret_key = 'CCAX6JJWmwhhysPIOP7WbEOVvndhzxhrNJPI1fQ3KPtXccm3GQUafstadKXAnx0C'
    symbol = 'BTC/USDT'
    amount = 0.001
    side = 'buy'  # 'buy' to open a long position, 'sell' to open a short position
    sandbox_mode = True

    # Initialize the exchange
    exchange_class = getattr(ccxt.pro, exchange_name)
    exchange = exchange_class({
        'apiKey': api_key,
        'secret': secret_key,
        'options': {
            'defaultType': 'spot'  # Use 'spot' if you're testing on spot markets
        }
    })

    if sandbox_mode and exchange.has['sandbox']:
        exchange.set_sandbox_mode(True)

    try:
        await exchange.load_markets()

        # Open a market order
        print(f"Placing {side} market order for {amount} {symbol}")
        order = await exchange.create_market_order(symbol, side, amount)
        assert order is not None, "Failed to place market order"
        print("Order placed:", order)

        # Wait for a few seconds
        time.sleep(5)

        # Close the position by placing the opposite market order
        opposite_side = 'sell' if side == 'buy' else 'buy'
        print(f"Closing position with {opposite_side} market order for {amount} {symbol}")
        close_order = await exchange.create_market_order(symbol, opposite_side, amount)
        assert close_order is not None, "Failed to close market order"
        print("Position closed:", close_order)

    except ccxt.BaseError as e:
        pytest.fail(f"An error occurred: {str(e)}")
    finally:
        await exchange.close()
