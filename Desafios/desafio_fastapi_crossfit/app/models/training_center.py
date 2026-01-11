from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class TrainingCenter(Base):
    __tablename__ = "centro_treinamento"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    id: Mapped[str] = mapped_column(String(36), unique=True, index=True)  # uuid as string
    nome: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)

    atletas = relationship("Athlete", back_populates="centro_treinamento")
