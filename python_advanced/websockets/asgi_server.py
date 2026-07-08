#!/usr/bin/env python3

from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import WebSocketRoute, Route
from starlette.websockets import WebSocketDisconnect


async def homepage(request):
    return FileResponse("index.html")


async def stylesheet(request):
    return FileResponse("style.css")


async def script(request):
    return FileResponse("client.js")


async def websocket_endpoint(websocket):
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            if not message:
                print("ERR: EMPTY")
                continue
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(debug=True, routes=[
    WebSocketRoute('/ws', websocket_endpoint),
    Route('/', homepage),
    Route('/style.css', stylesheet),
    Route('/client.js', script),
])
