from pybit.unified_trading import HTTP
import creds

class TradingSession:
    def __init__(self, testnet=True, api_key=creds.apikey, api_secret=creds.apisecret):
        self.session = HTTP(
            testnet=testnet,
            api_key=api_key,
            api_secret=api_secret,
        )
    def get_kline(self, category="spot", symbol="BTCUSDT", interval=60, start=1670601600000, end=1670608800000):
        return self.session.get_kline(
            category=category,
            symbol=symbol,
            interval=interval,
            start=start,
            end=end,
        )#used
    def orderbook(self, category='spot', symbol='BTCUSDT'):
        return self.session.get_orderbook(
            category=category,
            symbol=symbol,
        )#used
    def place_order(self, category="spot", symbol="BTCUSDT", side="Buy", orderType="Limit", qty="0.01", price="15600", timeInForce="PostOnly", orderLinkId="spot-test-postonly", isLeverage=0, orderFilter="Order"):
        return self.session.place_order(
            category=category,
            symbol=symbol,
            side=side,
            orderType=orderType,
            qty=qty,
            price=price,
            timeInForce=timeInForce,
            orderLinkId=orderLinkId,
            isLeverage=isLeverage,
            orderFilter=orderFilter,
        )#used
    def cancel_all_orders(self, category="linear", settleCoin="USDT"):
        return self.session.cancel_all_orders(
            category=category,
            settleCoin=settleCoin,
        )#used
    def getrecenttrades(self,category='spot',symbol='BTCUSDT',limit=1):
        return self.session.get_public_trade_history(
            category=category,
            symbol=symbol,
            limit=limit
            )
    def accountbalance(self,accounttype='UNIFIED',coin='BTC'):
        return self.session.get_wallet_balance(
            accounttype=accounttype,
            coin=coin
        )#used
    #here first check the open orders then only close the orders with the proper orderid
    def cancelorder(self,category='spot',symbol='BTCUSDT',orderid="c6f055d9-7f21-4079-913d-e6523a9cfffa"):
        return self.session.cancel_order(
            category=category,
            symbol=symbol,
            orderid=orderid
        )#won't use
    def feerateinfo(self,symbol='BTCUSDT'):
        return self.session.get_fee_rates(symbol=symbol)#used
    
    def coinbalance(self,accounttype='UNIFIED',coin='USDC'):
        return self.session.get_coins_balance(accounttype=accounttype,coin=coin)
    
    def getpositions(self,category='spot',symbol='BTCUSDT'):
        return self.session.get_positions(category=category,symbol=symbol)
    
    def historicalvolatility(self,category='spot',basecoin='BTC',period=30):
        self.session.get_historical_volatility(category=category,basecoin=basecoin,period=period)#used

    def tickers(self,category='spot',symbol='BTCUSDT'):
        self.session.get_tickers(category=category,symbol=symbol)  #used

trading_session = TradingSession()
"""print(trading_session.accountbalance())"""
print(trading_session.get_kline())
print(trading_session.orderbook())
print(trading_session.tickers())
"""print(trading_session.historicalvolatility())"""
print(trading_session.feerateinfo())
print(trading_session.place_order())
print(trading_session.getpositions())
print(trading_session.cancel_all_orders())
print(trading_session.getrecenttrades())
print(trading_session.accountbalance())
