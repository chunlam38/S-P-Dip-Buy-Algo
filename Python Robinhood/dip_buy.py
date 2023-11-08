import robin_stocks.robinhood as robin
import creds #stores mi ma

#setup (logging in to RH)
login = robin.login(creds.RH_User, creds.RH_Pass, store_session=True)
data = robin.load_phoenix_account()

prev_close = robin.get_quotes("VOO", "previous_close")

#1% dip price
dip_buy_price = float(prev_close[0])*0.99

curr_price = float(robin.get_quotes("VOO", "last_trade_price")[0])

print("Prices", curr_price, dip_buy_price)

if curr_price <= dip_buy_price: 
    robin.order_buy_fractional_by_price("VOO", 50.00, None, "gfd")

print(dip_buy_price, curr_price)

print(prev_close)