"""
Desafio 04 — Par ou Ímpar

Entrada:
- um número inteiro

Saída:
- "par" se for par, senão "ímpar"
"""

from utils.io_helpers import read_int

n = read_int("Digite um número inteiro: ")

print("par" if n % 2 == 0 else "ímpar")
