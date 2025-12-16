# Tuplas tem muito menos métodos embutidos do que listas, devido à sua imutabilidade.

# Aqui estão alguns dos métodos mais comuns que podem ser usados com tuplas:
# 1. .count(item): Retorna o número de vezes que um item aparece na tupla.
# 2. .index(item): Retorna o índice da primeira ocorrência de um item na tupla.
# 3. .len(): Embora não seja um método de tupla, a função len() é frequentemente usada para obter o tamanho da tupla.
# 4. .sorted(): Retorna uma nova lista contendo todos os itens da tupla em ordem crescente. A tupla original permanece inalterada.
# 5. .tuple(): Converte outros tipos de dados iteráveis (como listas) em tuplas.

# Exemplo de uso dos métodos de tupla:
minha_tupla = (5, 2, 9, 1, 5, 6)
print("Tupla original:", minha_tupla)

# 1. Contando quantas vezes o número 5 aparece na tupla
contagem = minha_tupla.count(5)
print("Contagem de 5 na tupla:", contagem)

# 2. Encontrando o índice do primeiro 5
indice = minha_tupla.index(5)
print("Índice do primeiro 5:", indice)

# 3. Obtendo o tamanho da tupla
tamanho = len(minha_tupla)
print("Tamanho da tupla:", tamanho)

# 4. Ordenando a tupla (retorna uma lista)
tupla_ordenada = sorted(minha_tupla)
print("Tupla ordenada (como lista):", tupla_ordenada)

# 5. Convertendo uma lista em tupla
lista = [1, 2, 3, 4]
tupla_de_lista = tuple(lista)

print("Tupla criada a partir de uma lista:", tupla_de_lista)

# Note que, devido à imutabilidade das tuplas, não existem métodos para adicionar, remover ou modificar elementos diretamente.
# Por exemplo, os métodos append(), remove() ou pop() não estão disponíveis para tuplas.

# Uma curiosidade é que listas podem ser convertidas em tuplas e vice-versa, permitindo alguma flexibilidade na manipulação de dados.
# Usando o método list seria possível converter uma tupla em uma lista para modificá-la, e depois convertê-la de volta para uma tupla se necessário.
