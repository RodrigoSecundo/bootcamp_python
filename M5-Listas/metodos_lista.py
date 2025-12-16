# Em Python, existem diversos métodos embutidos que facilitam a manipulação de listas. Abaixo estão alguns dos métodos mais comuns usados com listas:

# 1. .append(item): Adiciona um item ao final da lista.
# 2. .extend(iterável): Adiciona todos os itens de um iterável (como outra lista) ao final da lista.
# 3. .insert(index, item): Insere um item em uma posição específica.
# 4. .remove(item): Remove a primeira ocorrência de um item da lista, se existir. Não retorna nada.
# 5. .pop(): Remove e pode retornar o valor do que foi removido. Por padrão, remove o último item se não informar índice.
# 6. .clear(): Remove todos os itens da lista.
# 7. .index(item): Retorna o índice da primeira ocorrência de um item.
# 8. .count(item): Retorna o número de vezes que um item aparece na lista.
# 9. .sort(): Ordena os itens da lista em ordem crescente.
# 10. .reverse(): Inverte a ordem dos itens na lista.
# 11. .copy(): Retorna uma cópia rasa da lista.
# 12. .len(): Embora não seja um método de lista, a função len() é frequentemente usada para obter o tamanho da lista.
# 13. .sorted(reverse=True): Ordena os itens da lista em ordem decrescente.

# Exemplo de uso dos métodos de lista:
minha_lista = [5, 2, 9, 1, 5, 6]
print("Lista original:", minha_lista)

# 1. Adicionando um item
minha_lista.append(3)
print("Após append(3):", minha_lista)
# saída: [5, 2, 9, 1, 5, 6, 3]

# 2. Adicionando múltiplos itens, pode ser outra lista ou qualquer iterável
minha_lista.extend([8, 4])
print("Após extend([8, 4]):", minha_lista)
# saída: [5, 2, 9, 1, 5, 6, 3, 8, 4]


# 3. Inserindo um item na posição 2
minha_lista.insert(2, 7)
print("Após insert(2, 7):", minha_lista) #lembrando que toda lista começa no índice 0
# saída: [5, 2, 7, 9, 1, 5, 6, 3, 8, 4]

# 4. Removendo o primeiro 5
minha_lista.remove(5)
print("Após remove(5):", minha_lista)
# saída: [2, 7, 9, 1, 5, 6, 3, 8, 4]

# 5. Removendo o item na posição 3
removido = minha_lista.pop(3)
print("Após pop(3):", minha_lista) # saída: [2, 7, 9, 5, 6, 3, 8, 4]
print("Item removido:", removido) # saída: 1

# pop também serve como contrapartida ao append, removendo o último item se nenhum índice for especificado

# 6. Limpando a lista
minha_lista.clear()
print("Após clear():", minha_lista)
# saída: []

# Recriando a lista para os próximos exemplos
minha_lista = [5, 2, 9, 1, 5, 6]

# 7. Encontrando o índice do primeiro 5
indice = minha_lista.index(5)
print("Índice do primeiro 5:", indice)
# saída: 0

# 8. Contando quantos 5 existem na lista
contagem = minha_lista.count(5)
print("Contagem de 5 na lista:", contagem)
# saída: 2

# 9. Ordenando a lista
minha_lista.sort()
print("Após sort():", minha_lista)
# saída: [1, 2, 5, 5, 6, 9]

# 10. Invertendo a lista
minha_lista.reverse()
print("Após reverse():", minha_lista)
# saída: [9, 6, 5, 5, 2, 1]

# 11. Copiando a lista, muito útil para evitar alterações na lista original
copia_lista = minha_lista.copy()
print("Cópia da lista:", copia_lista)
# saída: [9, 6, 5, 5, 2, 1]

# 12. Tamanho da lista usando len()
tamanho = len(minha_lista)
print("Tamanho da lista:", tamanho)
# saída: 6

# 13. Ordenando em ordem decrescente usando sorted()
lista_ordenada_decrescente = sorted(minha_lista, reverse=True)
print("Lista ordenada em ordem decrescente:", lista_ordenada_decrescente)
# saída: [9, 6, 5, 5, 2, 1]

# a diferença de sorted() para sort() é que sorted() retorna uma nova lista ordenada, enquanto sort() modifica a lista original.

# Esses métodos tornam a manipulação de listas em Python simples e eficiente.
# OBS: Alguns métodos, como sort() e reverse(), modificam a lista original e não retornam uma nova lista.
# Portanto, ao usá-los, não é necessário atribuir o resultado a uma nova variável.