"""
Desafio 03 — Operações Matemáticas Simples

Entrada:
- número a
- número b
- operador: +, -, *, /

Saída:
- resultado da operação (com tratamento básico de divisão por zero)
"""

from utils.io_helpers import read_float

a = read_float("Digite o primeiro número: ")
b = read_float("Digite o segundo número: ")
op = input("Digite a operação (+, -, *, /): ").strip()

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Não é possível dividir por zero.")
    else:
        print(a / b)
else:
    print("Operação inválida. Use +, -, * ou /.")
