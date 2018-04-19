import asyncio
import random
import websockets

async def sendMessage(websocket, path):
    while True:
        r = lambda: random.randint(0,255)
        color = '#%02X%02X%02X' % (r(),r(),r())

        await websocket.send(color)
        print("Color: ", color)
        await asyncio.sleep(5)


start_server = websockets.serve(sendMessage, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
