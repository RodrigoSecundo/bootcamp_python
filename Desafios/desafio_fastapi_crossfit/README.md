# Desafio Crossfit API (desafio_fastapi_crossfit)

API em **FastAPI (async)** com **PostgreSQL**, **SQLAlchemy 2.0 async**, **Alembic** e **paginação**.

## Requisitos

### 1) Python
Recomendado: **Python 3.11** (ou 3.12).

> Observação: você pode ter Python 3.13 instalado no PC, mas crie um ambiente virtual com 3.11/3.12 para evitar incompatibilidades com libs/driver async.

**Opções para instalar/usar Python 3.11:**
- `pyenv` (recomendado)
- `conda`
- instalador do Python.org (Windows)

### 2) Docker
Necessário para subir o PostgreSQL via `docker compose`.

Instale:
- Docker Desktop (Windows/Mac)
- Docker Engine + Docker Compose plugin (Linux)

## Como rodar o projeto

### 1) Entrar na pasta do desafio

```bash
cd Desafios/desafio_fastapi_crossfit
```

### 2) Criar `.env`
Copie o arquivo `.env.example` para `.env`:

```bash
cp .env.example .env
```

No Windows (PowerShell):
```powershell
Copy-Item .env.example .env
```

### 3) Criar ambiente virtual e instalar dependências

#### Opção A: venv (Linux/Mac)
```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Opção B: venv (Windows PowerShell)
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 4) Subir o banco (Postgres)
```bash
make run-docker
```

Se não tiver `make`, você pode rodar:
```bash
docker compose up -d
```

### 5) Rodar migrações (criar tabelas)
```bash
make run-migrations
```

### 6) Rodar a API
```bash
make run
```

Acesse:
- Docs Swagger: http://127.0.0.1:8000/docs

## Endpoints

### Categorias
- `POST /categorias`
- `GET /categorias`

### Centros de Treinamento
- `POST /centros-treinamento`
- `GET /centros-treinamento`

### Atletas
- `POST /atletas`
- `GET /atletas` (com paginação Limit/Offset e filtros por query params)
  - filtros:
    - `?nome=...` (contém)
    - `?cpf=...` (exato)
- `GET /atletas/{athlete_id}`

## Regras do desafio implementadas

- Query params no endpoint de atletas (`nome`, `cpf`)
- Response customizado no **get all** de atletas retornando:
  - `nome`
  - `categoria` (nome)
  - `centro_treinamento` (nome)
- Tratamento de `IntegrityError` para CPF duplicado:
  - mensagem: `já existe um atleta cadastrado com o cpf: X`
- Paginação usando `fastapi-pagination` (LimitOffset)

## Comandos úteis

- Subir banco: `make run-docker`
- Criar migration: `make create-migrations d="minha_migration"`
- Rodar migrations: `make run-migrations`
- Rodar API: `make run`
