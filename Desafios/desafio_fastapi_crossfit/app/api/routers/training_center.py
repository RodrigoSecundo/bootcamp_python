import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.models.training_center import TrainingCenter
from app.schemas.training_center import TrainingCenterCreate, TrainingCenterOut

router = APIRouter(prefix="/centros-treinamento", tags=["centros_treinamento"])


@router.post("", response_model=TrainingCenterOut, status_code=status.HTTP_201_CREATED)
async def create_training_center(payload: TrainingCenterCreate, db: AsyncSession = Depends(get_db)):
    obj = TrainingCenter(
        id=str(uuid.uuid4()),
        nome=payload.nome,
        endereco=payload.endereco,
        proprietario=payload.proprietario,
    )
    db.add(obj)
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Centro de treinamento já existe.")
    await db.refresh(obj)
    return obj


@router.get("", response_model=list[TrainingCenterOut])
async def list_training_centers(db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(TrainingCenter).order_by(TrainingCenter.pk_id))
    return list(res.scalars().all())
