from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timeing_middleware
app = FastAPI()

app.middleware("http")(timeing_middleware)

app.include_router(issues_router)








"""""

First example data teaching how to get data from a list of dictionaries
and also how to add new data to the list. using FastAPI endpoints.
and more specifically showing how to create a health check endpoint,
a get all items endpoint, a get item by id endpoint, and a create item endpoint.
using Get and Post methods.


items = [
        {"id": 1, "name": "Item One"}, 
        {"id": 2, "name": "Item Two"},
        {"id": 3, "name": "Item Three"}
]




@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/items/")

def get_items():
    return items


@app.get("/items/{item_id}")

def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items/")
def create_item(item:dict):
    items.append(item)
    return item

"""
