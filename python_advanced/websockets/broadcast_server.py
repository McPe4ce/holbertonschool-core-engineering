#!/usr/bin/env python3

from websockets.asyncio.server import serve, broadcast
from websockets.exceptions import ConnectionClosed
import asyncio


CONNECTIONS = set()


async def connection_handler(websocket):
    try:
        CONNECTIONS.add(websocket)

        async for message in websocket:
            if not message.strip():
                print("ERR:EMPTY")
                continue
            broadcast(connections=CONNECTIONS, message="B:" + message,
                      raise_exceptions=False)
    except ConnectionClosed:
        pass
    finally:
        CONNECTIONS.discard(websocket)


async def main():
    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
