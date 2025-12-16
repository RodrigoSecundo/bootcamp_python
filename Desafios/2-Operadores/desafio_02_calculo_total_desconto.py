# DESAFIO 02 — Total + desconto (Operadores)
#
# Objetivo: treinar operadores aritméticos, comparação, lógicos, atribuição e precedência.
#
# Cenário:
# Você vai calcular o total de uma compra com desconto e frete.
#
# Requisitos:
# 1) Peça ao usuário:
#    - preço do produto (float)
#    - quantidade (int)
#    - porcentagem de desconto (float) (ex: 10 para 10%)
#    - frete (float)
# 2) Calcule:
#    - subtotal = preço * quantidade
#    - desconto_em_reais = subtotal * (desconto / 100)
#    - total = subtotal - desconto_em_reais + frete
# 3) Mostre os 3 valores (subtotal, desconto, total) com 2 casas decimais.
# 4) Use pelo menos 2 operadores de atribuição (ex: `+=`, `-=`) em algum momento.
# 5) Crie uma variável booleana `compra_grande` que seja True quando:
#    - total >= 200 OR quantidade >= 5
#    e imprima o valor dela.
# 6) Faça uma segunda versão do cálculo do total usando parênteses para deixar a precedência explícita.
#
# Dicas:
# - Precedência importa: `*` e `/` vêm antes de `+` e `-`.
# - Faça `desconto / 100` para virar fator.
# - Use `float(preco_str.replace(",", "."))` se quiser aceitar vírgula.
#
# (Opcional) Desafio extra:
# - Se o desconto for maior que 50%, avise: "Desconto muito alto, conferir".

print("Desafio 2:")

preco_inicial = input("Digite o valor do produto: ")
quantidade = input("Quantas unidades vai comprar? ")
desconto = input("Qual será a porcentagem de desconto? (ex. 10 para 10%) ")
frete = input("Qual o valor combinado para frete? ")

preco_inicial = preco_inicial.replace(",", ".")
desconto = desconto.replace(",", ".")
frete = frete.replace(",", ".")
preco_inicial = float(preco_inicial)
quantidade = int(quantidade)
desconto = float(desconto)
frete = float(frete)

subtotal = preco_inicial * quantidade
desconto_total = subtotal * (desconto / 100)
total_pedido = subtotal
total_pedido -= desconto_total
total_pedido += frete


print(f"""
Tabela de Compra
Subtotal: {subtotal:.2f}
Desconto aplicado: {desconto_total:.2f}
Frete: {frete:.2f}
Preço final: {total_pedido:.2f}
""")

compra_grande = False

if total_pedido >= 200 or quantidade >= 5:
    compra_grande = True
    print(f"A compra é grande? {compra_grande}")
else:
    compra_grande = False
    print(f"A compra é grande? {compra_grande}")

print("Outra versão da conta: ")

conta_rapida = (preco_inicial * quantidade) - ((preco_inicial * quantidade) * (desconto / 100)) + frete
print(f"{conta_rapida:.2f}")

