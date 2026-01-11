from pydantic import BaseModel, Field


class TrainingCenterCreate(BaseModel):
    nome: str = Field(..., max_length=20)
    endereco: str = Field(..., max_length=60)
    proprietario: str = Field(..., max_length=30)


class TrainingCenterOut(BaseModel):
    id: str
    nome: str
    endereco: str
    proprietario: str

    model_config = {"from_attributes": True}
