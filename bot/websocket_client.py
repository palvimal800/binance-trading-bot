from binance import ThreadedWebsocketManager
import time

def start_socket():

    def handle_message(msg):
        print(msg)

    twm = ThreadedWebsocketManager()
    twm.start()

    twm.start_symbol_ticker_socket(
        callback=handle_message,
        symbol='BTCUSDT'
    )

    while True:
        time.sleep(1)