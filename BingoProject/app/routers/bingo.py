
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import random

router = APIRouter()

NUMERI = list(range(1,76))
rooms = {}

@router.get("/play", response_class=HTMLResponse)
async def play():
    return open("app/templates/index.html", encoding="utf-8").read()

@router.websocket("/ws/{room}")
async def ws(ws: WebSocket, room: str):
    await ws.accept()

    if room not in rooms:
        nums = NUMERI.copy()
        random.shuffle(nums)
        rooms[room] = {
            "nums": nums,
            "estratti": [],
            "clients": {},
            "winner": None
        }

    nickname = await ws.receive_text()

    if nickname in rooms[room]["clients"]:
        await ws.send_text("NICK_TAKEN")
        await ws.close()
        return

    rooms[room]["clients"][nickname] = ws

    for c in rooms[room]["clients"].values():
        await c.send_text(f"JOIN:{nickname}")

    try:
        while True:
            msg = await ws.receive_text()

            if msg == "READY" and rooms[room]["winner"] is None:
                if rooms[room]["nums"]:
                    n = rooms[room]["nums"].pop()
                    rooms[room]["estratti"].append(n)
                    for c in rooms[room]["clients"].values():
                        await c.send_text(f"NUM:{n}")

            if msg == "BINGO" and rooms[room]["winner"] is None:
                rooms[room]["winner"] = nickname
                for c in rooms[room]["clients"].values():
                    await c.send_text(f"WIN:{nickname}")

    except WebSocketDisconnect:
        rooms[room]["clients"].pop(nickname, None)
