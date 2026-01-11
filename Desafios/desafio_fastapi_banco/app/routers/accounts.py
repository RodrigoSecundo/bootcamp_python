from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Account, Transaction, TransactionType, User
from app.routers.auth import get_current_user
from app.schemas import AmountIn, BalanceOut, StatementOut, TransactionOut

router = APIRouter(prefix="/accounts", tags=["accounts"])


async def _get_account_for_user(session: AsyncSession, user: User) -> Account:
    account = await session.scalar(select(Account).where(Account.user_id == user.id))
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account


@router.post("/deposit", response_model=BalanceOut, status_code=status.HTTP_201_CREATED)
async def deposit(
    payload: AmountIn,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> BalanceOut:
    account = await _get_account_for_user(session, user)

    amount = payload.amount
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be > 0")

    async with session.begin():
        account.balance = (Decimal(str(account.balance)) + amount)  # type: ignore[arg-type]
        tx = Transaction(account_id=account.id, type=TransactionType.DEPOSIT, amount=amount)
        session.add(tx)

    await session.refresh(account)
    return BalanceOut(balance=Decimal(str(account.balance)))


@router.post("/withdraw", response_model=BalanceOut, status_code=status.HTTP_201_CREATED)
async def withdraw(
    payload: AmountIn,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> BalanceOut:
    account = await _get_account_for_user(session, user)

    amount = payload.amount
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be > 0")

    current_balance = Decimal(str(account.balance))
    if amount > current_balance:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient funds")

    async with session.begin():
        account.balance = (Decimal(str(account.balance)) - amount)  # type: ignore[arg-type]
        tx = Transaction(account_id=account.id, type=TransactionType.WITHDRAW, amount=amount)
        session.add(tx)

    await session.refresh(account)
    return BalanceOut(balance=Decimal(str(account.balance)))


@router.get("/statement", response_model=StatementOut)
async def statement(
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
) -> StatementOut:
    account = await _get_account_for_user(session, user)

    txs = (await session.scalars(select(Transaction).where(Transaction.account_id == account.id).order_by(Transaction.created_at.desc()))).all()

    return StatementOut(
        balance=Decimal(str(account.balance)),
        transactions=[
            TransactionOut(id=t.id, type=t.type.value, amount=Decimal(str(t.amount)), created_at=t.created_at)
            for t in txs
        ],
    )
