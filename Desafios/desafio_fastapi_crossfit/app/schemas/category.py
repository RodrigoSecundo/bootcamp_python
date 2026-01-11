from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    nome: str = Field(..., max_length=40)


class CategoryOut(BaseModel):
    id: str
    nome: str

    model_config = {"from_attributes": True}
