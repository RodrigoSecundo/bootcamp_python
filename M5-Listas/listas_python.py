# As listas em Python são coleções ordenadas e mutáveis que permitem armazenar múltiplos itens em uma única variável. Elas são definidas usando colchetes [] e os itens são separados por vírgulas.
# Listas podem conter elementos de diferentes tipos de dados, incluindo outras listas.
# Uma lista pode ter mais de um tipo de dado, como números inteiros, strings, floats, etc.
# Exemplos de criação de listas:

# Lista de inteiros
lista_inteiros = [1, 2, 3, 4, 5]
print("Lista de inteiros:", lista_inteiros)

# Lista de strings
lista_strings = ["maçã", "banana", "laranja"]
print("Lista de strings:", lista_strings)

# Lista mista
lista_mista = [1, "dois", 3.0, True, [5, 6, 7]]
print("Lista mista:", lista_mista)

# Acessando elementos da lista
print("Primeiro elemento da lista de strings:", lista_strings[0])  # Saída: maçã
print("Último elemento da lista mista:", lista_mista[-1])  # Saída: [5, 6, 7]

# Modificando elementos da lista
lista_inteiros[0] = 10
print("Lista de inteiros após modificação:", lista_inteiros)  # Saída: [10, 2, 3, 4, 5]

# Adicionando elementos à lista
lista_strings.append("uva")
print("Lista de strings após adicionar 'uva':", lista_strings)  # Saída: ['maçã', 'banana', 'laranja', 'uva']

# Inserindo elemento em uma posição específica
lista_inteiros.insert(1, 15)
print("Lista de inteiros após inserção de 15 na posição 1:", lista_inteiros)  # Saída: [10, 15, 2, 3, 4, 5]

# Removendo elementos da lista
lista_strings.remove("banana")
print("Lista de strings após remover 'banana':", lista_strings)  # Saída: ['maçã', 'laranja', 'uva']

# Removendo o último elemento da lista
ultimo_elemento = lista_inteiros.pop()
print("Elemento removido da lista de inteiros:", ultimo_elemento)  # Saída: 5
print("Lista de inteiros após remoção do último elemento:", lista_inteiros)  # Saída: [10, 15, 2, 3, 4]

# Tamanho da lista
print("Tamanho da lista mista:", len(lista_mista))  # Saída: 5

# Iterando sobre uma lista
for fruta in lista_strings:
    print("Fruta na lista:", fruta)
# Saída:
# Fruta na lista: maçã
# Fruta na lista: laranja

# Verificando se um elemento está na lista
if "laranja" in lista_strings:
    print("Laranja está na lista de strings.")
else:
    print("Laranja não está na lista de strings.")
# Saída: Laranja está na lista de strings.

# Copiando uma lista
copia_lista = lista_inteiros.copy()
print("Cópia da lista de inteiros:", copia_lista)  # Saída: [10, 15, 2, 3, 4]

# Limpando uma lista
lista_mista.clear()
print("Lista mista após limpeza:", lista_mista)  # Saída: []