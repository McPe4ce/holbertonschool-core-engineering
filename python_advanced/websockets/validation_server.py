#!/usr/bin/env python3

#!/usr/bin/env python3

from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed
import asyncio


async def connection_handler(websocket):
    try:
        async for message in websocket:
            if not message.strip():
                print("ERR:EMPTY")
                await websocket.send("ERR:EMPTY")
                continue
            await websocket.send("OK:" + message)
    except ConnectionClosed:
        pass


async def main():
    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
