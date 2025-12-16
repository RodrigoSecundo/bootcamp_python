# DESAFIO 04 — Menu + acumulador (Repetição)
#
# Objetivo: treinar `while`, `for`, `break`, `continue`, acumulação e contagem.
#
# Cenário:
# Faça um programinha com menu repetindo até o usuário escolher sair.
#
# Requisitos:
# 1) Crie uma lista vazia `numeros = []`.
# 2) Mostre o menu em loop (while True):
#    [1] Adicionar número
#    [2] Mostrar resumo
#    [3] Limpar lista
#    [0] Sair
# 3) Regras do menu:
#    - Opção 1: pedir um número inteiro e adicionar na lista.
#      * Se o usuário digitar um valor inválido (não número), ignore e volte ao menu.
#    - Opção 2: mostrar:
#      * quantidade de números
#      * soma
#      * média (se tiver pelo menos 1)
#      * maior e menor (se tiver pelo menos 1)
#      * quantos são pares e quantos ímpares (use `for`)
#    - Opção 3: limpar a lista (use `.clear()`)
#    - Opção 0: sair do loop (use `break`)
# 4) Use `continue` pelo menos 1 vez (ex: quando a opção for inválida).
#
# Dicas:
# - Converta entrada com `int()` dentro de um `try/except ValueError`.
# - Para média: `soma / quantidade`.
# - Para paridade: `n % 2 == 0`.
#
# (Opcional) Desafio extra:
# - Mostre os números digitados em ordem inversa usando fatiamento `numeros[::-1]`.

numeros = []

while True:
    print("""
[1] Adicionar número
[2] Mostrar resumo
[3] Limpar lista
[0] Sair
""")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        try:
            numero = int(input("Digite um número inteiro: "))
            numeros.append(numero)
        except ValueError:
            print("Valor inválido! Tente novamente.")
            continue

    elif opcao == '2':
        if len(numeros) == 0:
            print("A lista está vazia.")
        else:
            quantidade = len(numeros)
            soma = sum(numeros)
            media = soma / quantidade
            maior = max(numeros)
            menor = min(numeros)
            pares = sum(1 for n in numeros if n % 2 == 0)
            impares = quantidade - pares

            print(f"Quantidade de números: {quantidade}")
            print(f"Soma: {soma}")
            print(f"Média: {media:.2f}")
            print(f"Maior: {maior}")
            print(f"Menor: {menor}")
            print(f"Pares: {pares}")
            print(f"Ímpares: {impares}")
            print(f"Números em ordem inversa: {numeros[::-1]}")

    elif opcao == '3':
        numeros.clear()
        print("Lista limpa.")

    elif opcao == '0':
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida! Tente novamente.")
        continue