"""
Desafio 06 — Palíndromo

Entrada:
- uma palavra ou frase

Saída:
- "sim" se for palíndromo (ignorando espaços e caixa), senão "não"
"""

texto = input("Digite uma palavra ou frase: ")

normalizado = "".join(ch.lower() for ch in texto if ch.isalnum())
eh_palindromo = normalizado == normalizado[::-1]

print("sim" if eh_palindromo else "não")
