from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import HTMLResponse

app=FastAPI()
app.title = "Nutrition API with FastAPI"

class Food(BaseModel): #serializer
    id:int
    name:str
    description:str
    category:str
    healthful: bool

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Welcome to Nutrition Platform</h1>')

@app.get('/greet/{name}', tags=['food'])
def greet_name(name:str):
    return {"greeting": f"Hello {name}"}


@app.get('/food')
def great_optional_name(name:Optional[str]="user"):
    return {"Message": f"Hello {name}"} 

@app.put('/food/{food_id}', tags=['food'])
def update_item(item_id:int, food:Food):
    return{'name': food.name,
            'description': food.description,
            'category': food.category,
            'healthful': food.healthful
            }