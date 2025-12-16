# As tuplas em Python são coleções ordenadas e imutáveis que permitem armazenar múltiplos itens em uma única variável. Elas são definidas usando parênteses () e os itens são separados por vírgulas.
# Diferente das listas, as tuplas não podem ser modificadas após a sua criação (imutabilidade).
# Ela é útil para armazenar dados que não devem ser alterados, como coordenadas, cores RGB, etc.
# Mas é bem menos comum que listas, devido à sua mutabilidade e flexibilidade.

# Exemplos de criação de tuplas:

# Tupla de inteiros
tupla_inteiros = (1, 2, 3, 4, 5,) # Note que a vírgula final é opcional, mas recomendada por ser uma boa prática.
print("Tupla de inteiros:", tupla_inteiros)

# Tupla de strings
tupla_strings = ("maçã", "banana", "laranja",)
print("Tupla de strings:", tupla_strings)

# Tupla mista
tupla_mista = (1, "dois", 3.0, True, (5, 6, 7),)
print("Tupla mista:", tupla_mista)

# Também existe o método tuple() que converte outros tipos de dados em tuplas
tupla_de_lista = tuple([1, 2, 3]) #transforma a lista ( [] ) em tupla ( () )
print("Tupla criada a partir de uma lista:", tupla_de_lista)

# Para acessar elementos da tupla, usamos índices semelhantes aos das listas
print("Primeiro elemento da tupla de strings:", tupla_strings[0])  # Saída: maçã
print("Último elemento da tupla mista:", tupla_mista[-1])  # Saída: (5, 6, 7)

# Tuplas são imutáveis, então não podemos modificar seus elementos diretamente
# tupla_inteiros[0] = 10  # Isso geraria um erro: TypeError
# Por isso tupla é indicada para dados que não devem ser alterados. Pode ser visto como uma garantia de que os dados permanecerão constantes, na maioria das vezes.
# No entanto, se uma tupla contiver um objeto mutável, como uma lista, os elementos dessa lista podem ser modificados
tupla_com_lista = (1, 2, [3, 4], 5,)
tupla_com_lista[2].append(6)  # Modificando a lista dentro da tupla
print("Tupla com lista modificada:", tupla_com_lista)  # Saída: (1, 2, [3, 4, 6], 5)