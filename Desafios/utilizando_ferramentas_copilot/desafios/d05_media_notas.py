"""
Desafio 05 — Média de Notas

Entrada:
- três notas (float)

Saída:
- média aritmética simples
"""

from utils.io_helpers import read_float

n1 = read_float("Nota 1: ")
n2 = read_float("Nota 2: ")
n3 = read_float("Nota 3: ")

media = (n1 + n2 + n3) / 3
print(f"{media:.2f}")
