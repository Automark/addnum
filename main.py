from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import json
import asyncio

app = FastAPI()

@app.post("/mcp")
async def mcp(request: Request):
    body = await request.json()
    a = body.get("a", 0)
    b = body.get("b", 0)
    result = a + b

    async def event_stream():
        yield f"data: {json.dumps({'result': result})}\n\n"
        await asyncio.sleep(0.1)

    return StreamingResponse(event_stream(), media_type="text/event-stream")
