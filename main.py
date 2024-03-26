"26.03.24==================Fastapi=================="
from fastapi import FastAPI

app = FastAPI()

@app.post('/create')
def create_product():
    return {"message":"Продукт успешно создался"}

@app.get('/')
def get_products():
    return {"message":"Вот ваши продукты"}

@app.delete("/delete")
def delete_product():
    return {"message":"Продукт удален"}

