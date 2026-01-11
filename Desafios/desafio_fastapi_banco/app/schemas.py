from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class Message(BaseModel):
    message: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AmountIn(BaseModel):
    amount: Decimal = Field(gt=0, description="Valor deve ser maior que zero")


class BalanceOut(BaseModel):
    balance: Decimal


class TransactionOut(BaseModel):
    id: int
    type: Literal["DEPOSIT", "WITHDRAW"]
    amount: Decimal
    created_at: datetime


class StatementOut(BaseModel):
    balance: Decimal
    transactions: list[TransactionOut]
