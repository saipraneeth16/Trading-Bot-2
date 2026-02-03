# Trading-Bot-2
## Setup
1. Create Binance Futures Testnet account
2. Set environment variables:
   - BINANCE_API_KEY
   - BINANCE_API_SECRET
3. Install dependencies:
   pip install -r requirements.txt

## Run Examples
Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000
