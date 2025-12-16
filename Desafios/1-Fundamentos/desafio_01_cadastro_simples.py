# DESAFIO 01 — Cadastro simples (Fundamentos)
#
# Objetivo: treinar input/output, variáveis, tipos e conversão.
#
# Requisitos:
# 1) Peça ao usuário:
#    - nome (texto)
#    - idade (inteiro)
#    - altura (float)
#    - cidade (texto)
# 2) Garanta que idade vire int e altura vire float.
#    - Extra: permita o usuário digitar altura com vírgula (ex: "1,75").
# 3) Imprima um "cartão" de cadastro bem formatado usando f-string.
#    - Mostre a idade + 1 (como inteiro) e a altura com 2 casas decimais.
# 4) Use pelo menos 1 vez o parâmetro `sep` ou `end` em um print.
# 5) Mostre o tipo final (type) de idade e altura.
#
# Saída esperada (exemplo):
# -------------------------
# Cadastro
# Nome: Rodrigo
# Cidade: São Paulo
# Idade: 25 (ano que vem: 26)
# Altura: 1.75 m
# -------------------------
#
# Dicas:
# - `input()` sempre retorna str.
# - Para altura com vírgula: `altura_str.replace(",", ".")`.
# - Para formatar float: `{altura:.2f}`.
#
# (Opcional) Desafio extra:
# - Se idade for menor que 0, exiba "idade inválida" e não mostre o cartão.

print("Desafio 1")

nome = input(("Informe seu nome: "))
idade = input(("Agora digite sua idade: "))
altura = input(("Muito bem! Agora informe sua altura em metros (ex: 1,75):  "))
cidade = input(("Qual cidade você mora? "))

idade = int(idade)
altura = altura.replace(",", ".")
altura = float(altura)

if idade < 0:
    print("Essa idade é inválida")
else:
    print ("-------------------------", sep= "-")
    print(f"""    Cadastro
    Nome = {nome}
    Idade = {idade} (ano que vem: {idade + 1})
    Altura = {altura:.2f}
    Cidade = {cidade}""")
    print ("-------------------------", sep= "-")
    print(f"O tipo de dado em idade é: {type(idade)}")
    print(f"O tipo de dado em altura é: {type(altura)}")