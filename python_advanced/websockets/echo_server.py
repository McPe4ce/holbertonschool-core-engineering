#!/usr/bin/env python3

from websockets.asyncio.server import serve
import asyncio


async def connection_handler(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
