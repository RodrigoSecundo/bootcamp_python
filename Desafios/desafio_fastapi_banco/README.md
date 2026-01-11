# Desafio FastAPI Banco (Async)

API bancária assíncrona com **FastAPI**, **SQLAlchemy Async (SQLite)** e **JWT**.

## Funcionalidades

- Autenticação com JWT (`/auth/register`, `/auth/login`)
- Contas correntes por usuário (1 conta por usuário neste desafio)
- Transações:
  - Depósito (`POST /accounts/deposit`)
  - Saque (`POST /accounts/withdraw`)
- Extrato/statement (`GET /accounts/statement`)
- Validações:
  - Não aceita valores negativos/zero
  - Saque não permite saldo insuficiente

## Requisitos

- Python 3.11+

## Instalação

```bash
cd Desafios/desafio_fastapi_banco
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na pasta do desafio (ou defina variáveis de ambiente) baseado no `.env.example`.

```bash
cp .env.example .env
```

## Rodando

```bash
uvicorn app.main:app --reload
```

A API estará em `http://127.0.0.1:8000`.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Uso rápido

1) Registrar usuário

```bash
curl -X POST http://127.0.0.1:8000/auth/register \
  -H 'Content-Type: application/json' \
  -d '{"email":"user@example.com","password":"123456"}'
```

2) Login

```bash
TOKEN=$(curl -s -X POST http://127.0.0.1:8000/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"email":"user@example.com","password":"123456"}' | python -c "import sys, json; print(json.load(sys.stdin)['access_token'])")
```

3) Depósito

```bash
curl -X POST http://127.0.0.1:8000/accounts/deposit \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"amount": 100.50}'
```

4) Saque

```bash
curl -X POST http://127.0.0.1:8000/accounts/withdraw \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"amount": 40}'
```

5) Extrato

```bash
curl http://127.0.0.1:8000/accounts/statement \
  -H "Authorization: Bearer $TOKEN"
```

## Observações de Modelagem

- Banco: SQLite (arquivo `./bank.db` por padrão)
- Transações são registradas com tipo `DEPOSIT`/`WITHDRAW`
- Saldo é mantido na tabela `accounts` e atualizado a cada transação dentro de uma transação atômica

## Estrutura

```
Desafios/desafio_fastapi_banco/
  app/
    core/
      config.py
      security.py
    routers/
      auth.py
      accounts.py
    db.py
    main.py
    models.py
    schemas.py
  requirements.txt
  .env.example
  README.md
```
