from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return {"Hola": "Mundo"}

@app.get("/items/{item_id}/{m}")
def read_item(item_id: int, m: str = None):
    return {"item_id": item_id, "m": m}
