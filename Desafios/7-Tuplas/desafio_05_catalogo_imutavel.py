# DESAFIO 05 — Catálogo imutável (Tuplas)
#
# Objetivo: treinar tuplas, tuplas aninhadas, métodos `.count()`/`.index()`, fatiamento e conversão tuple<->list.
#
# Cenário:
# Você recebeu um “catálogo” de produtos imutável representado por tupla de tuplas:
#
# catalogo = (
#     ("maçã", 2.50),
#     ("banana", 1.99),
#     ("laranja", 3.20),
#     ("banana", 1.99),
# )
#
# Requisitos:
# 1) Crie a tupla `catalogo` exatamente como acima.
# 2) Mostre:
#    - quantos itens existem no catálogo (`len`)
#    - quantas vezes aparece o produto "banana" (dica: você pode procurar pelo nome)
# 3) Encontre o índice da primeira ocorrência de ("banana", 1.99) usando `.index()`.
# 4) Mostre um “recorte” (fatiamento) do catálogo:
#    - os 2 primeiros itens
#    - os itens do meio (sem os extremos)
#    - a tupla invertida (`[::-1]`)
# 5) Gere uma lista ordenada por preço (crescente):
#    - dica: `sorted(catalogo, key=...)` retorna LISTA
#    - imprima o resultado
# 6) (Parte importante) Como tupla é imutável:
#    - converta o catálogo para lista
#    - adicione um novo item ("uva", 4.10)
#    - converta de volta para tupla
#    - imprima o novo catálogo
#
# Dicas:
# - Você já viu que `sorted(tupla)` retorna lista.
# - A tupla pode conter elementos repetidos.
# - Para contar "banana" por nome, você pode fazer um `for` e somar.

catalogo = (
    ("maçã", 2.50),
    ("banana", 1.99),
    ("laranja", 3.20),
    ("banana", 1.99),
)

contagem_tupla = len(catalogo)
print(f"Existem {contagem_tupla} itens no catálogo")

contagem_banana = 0

for produto_banana in catalogo:
    if produto_banana[0] == "banana":
        contagem_banana += 1

print(f"A quantidade de vezes que banana aparece no catélogo é: {contagem_banana}")

print(f"A primeira ocorrência de ('banana', 1.99) em catálogo é: {catalogo.index(("banana", 1.99))}")

print(f"Os 2 primeiros itens da tupla catálogo são: {catalogo[:2]}")

print(f"Os itens do meio da tupla catálogo são: {catalogo[1:3]}")

print(f"A tupla atual invertida seria: {catalogo[::-1]}")

tupla_nova = sorted(catalogo, key=lambda produto: produto[1])
print(f"A nova tupla usando sorted seria: {tupla_nova}")

catalogo = list(catalogo)
catalogo.append(("uva", 1.76))
print(f"Agora catálogo virou lista e foi adicionado mais dados a ele (repare nos [] na impressão): {catalogo}")
catalogo = tuple(catalogo)
print(f"Voltou a ser tupla e imutável, mas com o novo dado que foi adicionado enquanto ainda era lista: {catalogo}")