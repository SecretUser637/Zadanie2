from pydantic import BaseModel, Field


class Category(BaseModel):
    id: int = Field(..., example=1)
    parent_id: int = Field(..., example=1)
    name: str = Field(..., example="Кино")
    description: str = Field(None, example="Информация о кино")


class Artical(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Вышел фильм")
    description: str = Field(None, example="оценки положительные")
    category_id: int = Field(..., example=1)
