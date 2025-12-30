# DESAFIO 06 — Análise de números (Listas)
#
# Objetivo: treinar listas, conversão de tipos, métodos de lista, filtros e ordenação.
# Conteúdos do módulo: append, clear, copy, sort/sorted, count, index, list comprehension, filter/lambda.
#
# Requisitos:
# 1) Peça ao usuário uma sequência de números separados por vírgula.
#    Ex: "10, 3, 3, 8, -2, 7"
# 2) Converta isso para uma lista de inteiros `numeros`.
#    - Dica: `split(',')`, `strip()`, `int()`.
# 3) Mostre um resumo:
#    - lista original
#    - quantidade de itens (len)
#    - soma (use `sum`)
#    - menor e maior (use `min` e `max`)
# 4) Crie e mostre listas derivadas:
#    - `pares` usando list comprehension
#    - `impares` usando `filter()` com `lambda`
# 5) Ordenação sem perder o original:
#    - crie `ordenada = sorted(numeros)` e imprima
#    - prove que `numeros` original não mudou
# 6) Duplicados:
#    - peça ao usuário um número X
#    - mostre quantas vezes X aparece (`count`)
#    - se aparecer pelo menos 1 vez, mostre o índice da primeira ocorrência (`index`)
# 7) (Treino de métodos) Remoção segura:
#    - se X estiver na lista, remova uma ocorrência com `.remove(X)`
#    - se não estiver, não faça nada (use `if X in numeros:`)
#    - imprima a lista final
#
# (Opcional) Desafio extra:
# - Crie uma lista "matriz" (lista aninhada) com 2 linhas:
#   linha1 = pares, linha2 = impares, e imprima em formato de tabela.
