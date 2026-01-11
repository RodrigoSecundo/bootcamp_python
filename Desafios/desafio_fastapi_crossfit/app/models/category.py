from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Category(Base):
    __tablename__ = "categoria"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    id: Mapped[str] = mapped_column(String(36), unique=True, index=True)  # uuid as string
    nome: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)

    atletas = relationship("Athlete", back_populates="categoria")
