import config
import websocket, json

#{"action": "auth", "key": "AK1VLWTAQFR4UTRVIHXG", "secret": "pKuQa5YMgocDq5kepdXcWVr3eNN7jeYTXBC3cyze"}

def open_ws(ws):
    # set up authenticate data
    print("opened")
    auth_data = {"action": "auth", "key": "AK1VLWTAQFR4UTRVIHXG", "secret": "pKuQa5YMgocDq5kepdXcWVr3eNN7jeYTXBC3cyze"}
    ws.send(json.dumps(auth_data))

    socket_message = {"action": "listen", "data": {"streams": ["T.SPY"]}}
    ws.send(json.dumps(socket_message))

def on_message(ws, message):
    print("received a message")
    print(message)


def on_close(ws):
    print("closed connection")

socket = "wss://stream.data.alpaca.markets/v2/iex"

# create ws object
ws = websocket.WebSocketApp(socket, on_open=open_ws, on_message=on_message, on_close=on_close)

ws.run_forever()
