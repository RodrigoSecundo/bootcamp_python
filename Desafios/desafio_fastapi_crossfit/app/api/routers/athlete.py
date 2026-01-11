import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi_pagination import LimitOffsetPage, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import Select, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.api.deps import get_db
from app.models.athlete import Athlete
from app.models.category import Category
from app.models.training_center import TrainingCenter
from app.schemas.athlete import AthleteCreate, AthleteGetAllOut, AthleteOut

router = APIRouter(prefix="/atletas", tags=["atletas"])


@router.post("", response_model=AthleteOut, status_code=status.HTTP_201_CREATED)
async def create_athlete(payload: AthleteCreate, db: AsyncSession = Depends(get_db)):
    # valida FK simples (mensagens claras)
    cat = await db.scalar(select(Category).where(Category.pk_id == payload.categoria_id))
    if not cat:
        raise HTTPException(status_code=400, detail="categoria_id inválido.")

    ct = await db.scalar(select(TrainingCenter).where(TrainingCenter.pk_id == payload.centro_treinamento_id))
    if not ct:
        raise HTTPException(status_code=400, detail="centro_treinamento_id inválido.")

    obj = Athlete(
        id=str(uuid.uuid4()),
        nome=payload.nome,
        cpf=payload.cpf,
        idade=payload.idade,
        peso=payload.peso,
        altura=payload.altura,
        sexo=payload.sexo,
        centro_treinamento_id=payload.centro_treinamento_id,
        categoria_id=payload.categoria_id,
    )

    db.add(obj)
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        # Desafio: mensagem específica do cpf duplicado
        raise HTTPException(
            status_code=400,
            detail=f"já existe um atleta cadastrado com o cpf: {payload.cpf}",
        )
    await db.refresh(obj)
    return obj


@router.get("", response_model=LimitOffsetPage[AthleteGetAllOut])
async def list_athletes(
    db: AsyncSession = Depends(get_db),
    nome: Annotated[str | None, Query(None, description="Filtrar por nome (contém)")] = None,
    cpf: Annotated[str | None, Query(None, description="Filtrar por cpf (exato)")] = None,
):
    # Desafio: query params (nome e cpf)
    stmt: Select = (
        select(Athlete)
        .options(joinedload(Athlete.categoria), joinedload(Athlete.centro_treinamento))
        .order_by(Athlete.pk_id)
    )

    if nome:
        stmt = stmt.where(Athlete.nome.ilike(f"%{nome}%"))
    if cpf:
        stmt = stmt.where(Athlete.cpf == cpf)

    page = await paginate(db, stmt)

    # Desafio: customizar response do get all
    page.items = [
        AthleteGetAllOut(
            id=a.id,
            nome=a.nome,
            categoria=a.categoria.nome if a.categoria else "",
            centro_treinamento=a.centro_treinamento.nome if a.centro_treinamento else "",
        )
        for a in page.items
    ]
    return page


@router.get("/{athlete_id}", response_model=AthleteOut)
async def get_athlete(athlete_id: str, db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(Athlete).where(Athlete.id == athlete_id))
    obj = res.scalar_one_or_none()
    if not obj:
        raise HTTPException(status_code=404, detail="Atleta não encontrado.")
    return obj


# paginação
add_pagination(router)
