from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Athlete(Base):
    __tablename__ = "atleta"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    id: Mapped[str] = mapped_column(String(36), unique=True, index=True)  # uuid as string

    nome: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False, index=True)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)

    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)

    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey("centro_treinamento.pk_id"), nullable=False)
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categoria.pk_id"), nullable=False)

    centro_treinamento = relationship("TrainingCenter", back_populates="atletas")
    categoria = relationship("Category", back_populates="atletas")
