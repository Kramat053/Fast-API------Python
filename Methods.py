#Different HTTP methods:

#GET → retrieve data
#POST → create data
#PUT → update data
#DELETE → remove data

from fastapi import FastAPI

app = FastAPI()

# CREATE
@app.post("/items")
def create_item():
    return {"action": "create"}

# READ
@app.get("/items")
def read_items():
    return {"action": "read"}

# UPDATE
@app.put("/items/{id}")
def update_item(id: int):
    return {"action": "update"}

# DELETE
@app.delete("/items/{id}")
def delete_item(id: int):
    return {"action": "delete"}