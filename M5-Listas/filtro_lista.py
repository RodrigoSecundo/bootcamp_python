# Os filtros de listas em Python permitem selecionar elementos específicos de uma lista com base em uma condição.
# Isso é feito usando a função filter() ou compreensões de listas (list comprehensions).

# Exemplo usando a função filter():
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filtrar números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros)) #lambda é uma função anônima que retorna True para números pares
print("Números pares usando filter():", numeros_pares)  # Saída: [2, 4, 6, 8, 10]

# Exemplo usando compreensões de listas:
# Filtrar números pares
numeros_pares_comp = [x for x in numeros if x % 2 == 0]
print("Números pares usando list comprehension:", numeros_pares_comp)  # Saída: [2, 4, 6, 8, 10]

# ou usando for

numeros_pares_for = []

for x in numeros:
    if x % 2 == 0:
        numeros_pares_for.append(x)
print("Números pares usando for:", numeros_pares_for)  # Saída: [2, 4, 6, 8, 10]


