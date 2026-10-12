from fastapi import FastAPI

app = FastAPI()


@app.get("/async-hello")
async def async_hello():
    return {"message": "hello async"}


@app.get("/async-items/{item_id}")
async def async_get_item(item_id: int):
    return {"item_id": item_id}


@app.post("/async-echo")
async def async_echo(payload: dict):
    return payload
