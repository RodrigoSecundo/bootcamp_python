"""
Desafio 01 — Concatenando Dados

Entrada:
- dois valores (podem ser texto, número, etc.)

Saída:
- uma string com os dois valores concatenados (com um espaço no meio).
"""

a = input("Digite o primeiro valor: ")
b = input("Digite o segundo valor: ")

resultado = f"{a}{b}"  # se quiser com espaço: f"{a} {b}"
print(resultado)
