#!/usr/bin/env python3

import asyncio
from websockets.asyncio.client import connect
import os
import sys


async def connect_and_send(uri, message):
    async with connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response


if __name__ == "__main__":
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    message = sys.argv[1] if len(sys.argv) > 1 else "demo"
    websocks = asyncio.run(connect_and_send(uri, message))
    sys.stdout.write(websocks)
