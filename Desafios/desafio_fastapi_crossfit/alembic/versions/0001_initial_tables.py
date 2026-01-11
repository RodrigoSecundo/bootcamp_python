"""initial tables

Revision ID: 0001_initial
Revises: 
Create Date: 2026-01-11

"""
from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "categoria",
        sa.Column("pk_id", sa.Integer(), primary_key=True),
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("nome", sa.String(length=40), nullable=False),
    )
    op.create_index("ix_categoria_pk_id", "categoria", ["pk_id"])
    op.create_index("ix_categoria_id", "categoria", ["id"], unique=True)
    op.create_index("ix_categoria_nome", "categoria", ["nome"], unique=True)

    op.create_table(
        "centro_treinamento",
        sa.Column("pk_id", sa.Integer(), primary_key=True),
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("nome", sa.String(length=20), nullable=False),
        sa.Column("endereco", sa.String(length=60), nullable=False),
        sa.Column("proprietario", sa.String(length=30), nullable=False),
    )
    op.create_index("ix_centro_treinamento_pk_id", "centro_treinamento", ["pk_id"])
    op.create_index("ix_centro_treinamento_id", "centro_treinamento", ["id"], unique=True)
    op.create_index("ix_centro_treinamento_nome", "centro_treinamento", ["nome"], unique=True)

    op.create_table(
        "atleta",
        sa.Column("pk_id", sa.Integer(), primary_key=True),
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("nome", sa.String(length=50), nullable=False),
        sa.Column("cpf", sa.String(length=11), nullable=False),
        sa.Column("idade", sa.Integer(), nullable=False),
        sa.Column("peso", sa.Float(), nullable=False),
        sa.Column("altura", sa.Float(), nullable=False),
        sa.Column("sexo", sa.String(length=1), nullable=False),
        sa.Column("centro_treinamento_id", sa.Integer(), sa.ForeignKey("centro_treinamento.pk_id"), nullable=False),
        sa.Column("categoria_id", sa.Integer(), sa.ForeignKey("categoria.pk_id"), nullable=False),
    )
    op.create_index("ix_atleta_pk_id", "atleta", ["pk_id"])
    op.create_index("ix_atleta_id", "atleta", ["id"], unique=True)
    op.create_index("ix_atleta_cpf", "atleta", ["cpf"], unique=True)
    op.create_index("ix_atleta_nome", "atleta", ["nome"])


def downgrade() -> None:
    op.drop_index("ix_atleta_nome", table_name="atleta")
    op.drop_index("ix_atleta_cpf", table_name="atleta")
    op.drop_index("ix_atleta_id", table_name="atleta")
    op.drop_index("ix_atleta_pk_id", table_name="atleta")
    op.drop_table("atleta")

    op.drop_index("ix_centro_treinamento_nome", table_name="centro_treinamento")
    op.drop_index("ix_centro_treinamento_id", table_name="centro_treinamento")
    op.drop_index("ix_centro_treinamento_pk_id", table_name="centro_treinamento")
    op.drop_table("centro_treinamento")

    op.drop_index("ix_categoria_nome", table_name="categoria")
    op.drop_index("ix_categoria_id", table_name="categoria")
    op.drop_index("ix_categoria_pk_id", table_name="categoria")
    op.drop_table("categoria")
