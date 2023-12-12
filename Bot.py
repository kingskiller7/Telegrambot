#_Main_body

import telepot
from telepot.loop import MessageLoop

# Your trading strategy functions (RSI, MACD, signal generation)
# Define these functions or import them from your trading module

# Function to generate signals and send them to the user
def generate_signals_and_send(chat_id):
    # Simulated data for demonstration purposes
    # Replace this with your actual data source or API integration
    data = {
        'timestamp': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
        'open': [100, 102, 105, 110, 108],
        'close': [102, 104, 108, 109, 107],
    }
    df = pd.DataFrame(data)

    # Apply your trading strategy to generate signals
    df['RSI'] = calculate_rsi(df)
    calculate_macd(df)
    df['Signal'] = df.apply(generate_signal, axis=1)

    # Extract the latest signal
    latest_signal = df.iloc[-1]['Signal']

    # Send the signal to the user
    bot.sendMessage(chat_id, f"Latest signal: {latest_signal}")

# Telegram bot commands and handlers
def handle_start(msg):
    chat_id = msg['chat']['id']
    bot.sendMessage(chat_id, "Welcome to the Trading Bot! Use /signal to get the latest trading signal.")

def handle_help(msg):
    chat_id = msg['chat']['id']
    bot.sendMessage(chat_id,
                    "Available commands:\n"
                    "/start - Start the bot\n"
                    "/help - Display available commands\n"
                    "/signal - Get the latest trading signal")

def handle_signal(msg):
    chat_id = msg['chat']['id']
    generate_signals_and_send(chat_id)

# Telegram bot initialization
bot = telepot.Bot('6601901997:AAFTBWHB9chcV9acDrhZaWItiAd_RylGu8c')

# Start message loop and define handlers
MessageLoop(bot, {
    'chat': lambda msg: handle_signal(msg),  # Handles all incoming messages
    'text': {
        '/start': lambda msg: handle_start(msg),
        '/help': lambda msg: handle_help(msg),
        '/signal': lambda msg: handle_signal(msg),
    }
}).run_as_thread()

# Keep the program running
while True:
    pass


#_Pocket_Option_Api

#Debugging:

import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')

#Check win and buy sample:

from pocketoptionapi.stable_api import PocketOption
ssid=r"""42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"123123123123\";s:10:\"ip_address\";s:12:\"2.111.11.5\";s:10:\"user_agent\";s:104:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36\";s:13:\"last_activity\";i:123232;}1232321213","isDemo":0,"uid":"123232132"}]"""
account=PocketOption(ssid)
check_connect,message=account.connect()
if check_connect:
account.change_balance("PRACTICE")#"REAL"
asset="EURUSD"
amount=1
dir="call"#"call"/"put"
duration=30#sec
print("Balance: ",account.get_balance())
buy_info=account.buy(asset,amount,dir,duration)
#need this to close the connect
print("----Trade----")
print("Get: ",account.check_win(buy_info["id"]))
print("----Trade----")
print("Balance: ",account.get_balance())
#need close ping server thread
account.close()

#Login:

from pocketoptionapi.stable_api import PocketOption
ssid=r"""42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"123123123\";s:10:\"ip_address\";s:12:\"1.2.3.4\";s:10:\"user_agent\";s:123:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36\";s:13:\"last_activity\";i:123;}123","isDemo":1,"uid":"123"}]"""
account=PocketOption(ssid)
check,message=account.connect()
account.close()

#Get Balance:

from pocketoptionapi.stable_api import PocketOption
ssid=r"""42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"123123123\";s:10:\"ip_address\";s:12:\"1.2.3.4\";s:10:\"user_agent\";s:123:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36\";s:13:\"last_activity\";i:123;}123","isDemo":1,"uid":"123"}]"""
account=PocketOption(ssid)
check,message=account.connect()
account.change_balance("PRACTICE")
balance=account.get_balance()
print(balance)
account.close()

#Buy:

from pocketoptionapi.stable_api import PocketOption
ssid=r"""42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"123123123\";s:10:\"ip_address\";s:12:\"1.2.3.4\";s:10:\"user_agent\";s:123:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36\";s:13:\"last_activity\";i:123;}123","isDemo":1,"uid":"123"}]"""
account=PocketOption(ssid)
check,message=account.connect()
if check:
account.change_balance("PRACTICE")
asset="EURUSD"
amount=1
dir="call"#"call"/"put"
duration=60#sec
print(account.buy(asset,amount,dir,duration))
account.close()

#Sell:

from pocketoptionapi.stable_api import PocketOption
ssid=r"""42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"123123123\";s:10:\"ip_address\";s:12:\"1.2.3.4\";s:10:\"user_agent\";s:123:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36\";s:13:\"last_activity\";i:123;}123","isDemo":1,"uid":"123"}]"""
account=PocketOption(ssid)
check_connect,message=account.connect()
if check_connect:
account.change_balance("PRACTICE")#"REAL"
asset="EURUSD"
amount=1
dir="call"#"call"/"put"
duration=120#sec
print("Balance: ",account.get_balance())
buy_info=account.buy(asset,amount,dir,duration)
#need this to close the connect
account.sell_option(buy_info["id"])
account.close()

#Get Candle:

from pocketoptionapi.stable_api import PocketOption
ssid=r"""42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"123123123\";s:10:\"ip_address\";s:12:\"1.2.3.4\";s:10:\"user_agent\";s:123:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36\";s:13:\"last_activity\";i:123;}123","isDemo":1,"uid":"123"}]"""
account=PocketOption(ssid)
check_connect,message=account.connect()
import time
if check_connect:
asset="EURUSD"
_time=int(time.time())#the candle end of time
offset=120#how much sec want to get _time-offset --->your candle <---_time
period=60#candle size in sec
print("You will get the candle from: "+str(_time-offset)+" to: "+str(_time))
print("------\n")
candle=account.get_candle(asset,_time,offset,period)
for c in candle["data"]:
print(c)
account.close()

#Asset Option:

from pocketoptionapi.stable_api import PocketOption
ssid=r"""42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"123123123\";s:10:\"ip_address\";s:12:\"1.2.3.4\";s:10:\"user_agent\";s:123:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36\";s:13:\"last_activity\";i:123;}123","isDemo":1,"uid":"123"}]"""
account=PocketOption(ssid)
check_connect,message=account.connect()
import time
if check_connect:
print("Check Asset Open")
for i in account.get_all_asset_name():
print(i,account.check_asset_open(i))
account.close()

#Get Realtime Candle:

from pocketoptionapi.stable_api import PocketOption
ssid=r"""42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"123123123\";s:10:\"ip_address\";s:12:\"1.2.3.4\";s:10:\"user_agent\";s:123:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36\";s:13:\"last_activity\";i:123;}123","isDemo":1,"uid":"123"}]"""
account=PocketOption(ssid)
check_connect,message=account.connect()
import time
if check_connect:
asset="NZDUSD_otc"
list_size=10#this is setting how much Quote you want to save
account.start_candles_stream("NZDUSD_otc",list_size)
while True:
if len(account.get_realtime_candles("NZDUSD_otc"))==list_size:
break
print(account.get_realtime_candles("NZDUSD_otc"))
account.close()

#Get payment:

from pocketoptionapi.stable_api import PocketOption
ssid=r"""42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"123123123\";s:10:\"ip_address\";s:12:\"1.2.3.4\";s:10:\"user_agent\";s:123:\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36\";s:13:\"last_activity\";i:123;}123","isDemo":1,"uid":"123"}]"""
account=PocketOption(ssid)
check_connect,message=account.connect()
if check_connect:
all_data=account.get_payment()
for asset_name in all_data:
asset_data=all_data[asset_name]
print(asset_name,asset_data["payment"],asset_data["open"])
account.close()

#_Market_Data

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)

#_Market_Data_API: 3SZ0U8JIZ97IFMF8
