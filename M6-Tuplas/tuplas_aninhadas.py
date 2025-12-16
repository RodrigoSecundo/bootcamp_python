# Tuplas aninhadas são tuplas que contêm outras tuplas como elementos. Elas permitem criar estruturas de dados mais complexas e hierárquicas.

# Exemplo de criação de uma tupla aninhada:
tupla_aninhada = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Tupla aninhada:")

for linha in tupla_aninhada:
    print(linha)

# Acessando elementos em uma tupla aninhada
print("Elemento na posição [1][2]:", tupla_aninhada[1][2]) # Saída: 6
print("Elemento na posição [0][0]:", tupla_aninhada[0][0]) # Saída: 1
