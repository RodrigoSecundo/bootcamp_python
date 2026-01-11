"""
Desafio 02 — Repetindo Texto

Entrada:
- um texto
- um inteiro n

Saída:
- o texto repetido n vezes (cada repetição em uma linha).
"""

from utils.io_helpers import read_int

texto = input("Digite um texto: ")
n = read_int("Digite um número inteiro (quantidade de repetições): ")

for _ in range(max(0, n)):
    print(texto)
