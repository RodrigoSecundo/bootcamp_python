from pydantic import BaseModel, Field


class AthleteCreate(BaseModel):
    nome: str = Field(..., max_length=50)
    cpf: str = Field(..., min_length=11, max_length=11)
    idade: int = Field(..., ge=0, le=130)
    peso: float = Field(..., gt=0)
    altura: float = Field(..., gt=0)
    sexo: str = Field(..., min_length=1, max_length=1)

    centro_treinamento_id: int
    categoria_id: int


class AthleteOut(BaseModel):
    id: str
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    centro_treinamento_id: int
    categoria_id: int

    model_config = {"from_attributes": True}


class AthleteGetAllOut(BaseModel):
    id: str
    nome: str
    categoria: str
    centro_treinamento: str
