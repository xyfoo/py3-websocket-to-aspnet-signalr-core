import websocket
import json

# https://github.com/aspnet/SignalR/blob/release/2.2/specs/HubProtocol.md

ws = None

def encode_json(obj):
    # All JSON messages must be terminated by the ASCII character 0x1E (record separator).
    # Reference: https://github.com/aspnet/SignalR/blob/release/2.2/specs/HubProtocol.md#json-encoding
    return json.dumps(obj) + chr(0x1E)

def ws_on_message(ws, message: str):
    ignore_list = ['{"type":6}', '{}']
    # Split using record seperator, as records can be received as one message
    for msg in message.split(chr(0x1E)):
        if msg and msg not in ignore_list:
            # Everything else not on ignore list
            print(f"From server: {msg}")
            # TODO: Perform your own handling here

def ws_on_error(ws, error):
    print(error)

def ws_on_close(ws):
    print("### Disconnected from SignalR Server ###")

def ws_on_open(ws):
    print("### Connected to SignalR Server via WebSocket ###")
    
    # Do a handshake request
    print("### Performing handshake request ###")
    ws.send(encode_json({
        "protocol": "json",
        "version": 1
    }))

    # Handshake completed
    print("### Handshake request completed ###")

    # Call chathub's send message method
    # Reference: https://github.com/aspnet/SignalR/blob/release/2.2/specs/HubProtocol.md#invocation-message-encoding
    ws.send(encode_json({
        "type": 1,
        "target": "SendMessage",
        "arguments": ["Python websocket", "Hello world!"]
    }))

    print("### Hello world message sent to ChatHub ###")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:5000/chathub",
                              on_message = ws_on_message,
                              on_error = ws_on_error,
                              on_close = ws_on_close)
    ws.on_open = ws_on_open
    ws.run_forever()
