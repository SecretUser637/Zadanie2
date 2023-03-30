from fastapi import FastAPI, HTTPException
import pydantic_models
from typing import List

app = FastAPI()


categories_db = []

articals_db = []


@app.delete('/articles/{id}')
def articlesdelete(id: int):
    k = 0
    for c in articals_db:
        if c.id == id:
            del articals_db[k]
            return 'ok'
        k += 1
    raise HTTPException(status_code=404, detail="Artical not found")


@app.post('/articles', response_model=pydantic_models.Artical)
def article_create(art: pydantic_models.Artical):
    articals_db.append(art)
    return art


@app.put('/articles/{id}', response_model=pydantic_models.Artical)
def articles_edit(id: int, art: pydantic_models.Artical):
    k = 0
    for c in articals_db:
        if c.id == id:
            articals_db[k] = art
            return art
        k += 1
    raise HTTPException(status_code=404, detail="Artical not found")


@app.get('/articles', response_model=List[pydantic_models.Artical])
def articles_get():
    return articals_db


@app.get('/articles/{id}', response_model=pydantic_models.Artical)
def artical_get_id(id: int):
    for c in articals_db:
        if c.id == id:
            return c
    raise HTTPException(status_code=404, detail="Artical not found")


@app.get('/articles/', response_model=pydantic_models.Artical)
def artical_get_q(query: str):
    for c in articals_db:
        if c.name == query or c.description == query:
            return c
        for cat in categories_db:
            if cat.id == c.category_id and cat.name == query:
                return c
    raise HTTPException(status_code=404, detail="Artical not found")


@app.post('/categories', response_model=pydantic_models.Category)
def category_create(cat: pydantic_models.Category):
    categories_db.append(cat)
    return cat


@app.put('/categories/{id}', response_model=pydantic_models.Category)
def category_edit(id: int, cat: pydantic_models.Category):
    k = 0
    for c in categories_db:
        if c.id == id:
            categories_db[k] = cat
            return cat
        k += 1
    raise HTTPException(status_code=404, detail="category not found")


@app.delete('/categories/{id}')
def category_delete(id: int):
    k = 0
    for c in categories_db:
        if c.id == id:
            del categories_db[k]
            return 'ok'
        k += 1
    raise HTTPException(status_code=404, detail="category not found")


@app.get('/categories', response_model=List[pydantic_models.Category])
def category_get():
    return categories_db


@app.get('/categories/{id}', response_model=pydantic_models.Category)
def category_get_id(id: int):
    for c in categories_db:
        if c.id == id:
            return c
    raise HTTPException(status_code=404, detail="category not found")


@app.get('/categories/', response_model=pydantic_models.Category)
def category_get_q(query: str):
    for c in categories_db:
        if c.name == query or c.description == query:
            return c
    raise HTTPException(status_code=404, detail="category not found")
