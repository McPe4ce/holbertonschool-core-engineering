#!/usr/bin/env python3

import asyncio
from websockets.asyncio.client import connect


async def connect_and_send():
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello WebSocket")
        message = await websocket.recv()
        print(message)


if __name__ == "__main__":
    asyncio.run(connect_and_send())
