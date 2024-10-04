from pybit.unified_trading import HTTP
import creds
session = HTTP(
    testnet=True,
    api_key=creds.apikey,
    api_secret=creds.apisecret,
)
session.get_orderbook(category="linear", symbol="BTCUSDT")
session = HTTP(testnet=True)
print(session.get_kline(
    category="spot",
    symbol="BTCUSD",
    interval=60,
    start=1670601600000,
    end=1670608800000,
))
print(session.get_orderbook(
    category='spot',
    symbol='BTCUSDT'
))
print(session.place_order(
    category="spot",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Limit",
    qty="0.01",
    price="15600",
    timeInForce="PostOnly",
    orderLinkId="spot-test-postonly",
    isLeverage=0,
    orderFilter="Order",
))
print(session.cancel_all_orders(
    category="linear",
    settleCoin="USDT",
))

