# python_forex-backtest
A trading bot and system for backtesting Forex strategies in Python.

### Data Collection
- The data was obtained by first creating a demo account on [Oanda](https://oanda.com).
- Upon successful account creation, you will receive a unique API key, which will be used to make API requests to the server.
- Postman was used to send and retrieve data.
- The documentation can be found at: [OANDA Developer API](https://developer.oanda.com/rest-live-v20/instrument-ep/)
- Sample requests include:
  - `https://api-fxpractice.oanda.com/v3/instruments/EUR_USD/candles?count=10&granularity=H1` - Retrieves the 10 most recent EUR/USD 1-hour candles.
  - `https://api-fxpractice.oanda.com/v3/accounts/{account_number}/instruments` - Retrieves the instruments available for a particular account.
