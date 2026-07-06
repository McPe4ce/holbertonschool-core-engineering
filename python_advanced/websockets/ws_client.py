#!/usr/bin/env python3

import asyncio
from websockets.asyncio.client import connect


async def connect_and_send(uri, message):
    async with connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        print(response)


if __name__ == "__main__":
    asyncio.run(connect_and_send("ws://localhost:8765", "Hello WebSocket"))
