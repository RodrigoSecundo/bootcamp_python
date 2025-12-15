# Listas aninhadas são listas que contêm outras listas como elementos.
# Elas são úteis para representar estruturas de dados mais complexas, como matrizes ou tabelas.
# Exemplo de criação de uma lista aninhada (matriz 3x3):

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz 3x3:")

for linha in matriz:
    print(linha)
# Acessando elementos em uma lista aninhada
print("Elemento na posição [1][2]:", matriz[1][2])  # Saída: 6
print("Elemento na posição [0][0]:", matriz[0][0])  # Saída: 1

#Exemplo de tabela de notas de alunos
notas_alunos = [
    ["Alice", 85, 90, 78],
    ["Bob", 92, 88, 95],
    ["Charlie", 70, 75, 80]
]

print("\nNotas dos alunos:")
for aluno in notas_alunos:
    nome = aluno[0] # Nome do aluno
    notas = aluno[1:] # Notas do aluno, tem que pegar a partir do índice 1 até o final
    media = sum(notas) / len(notas) # Cálculo da média
    print(f"{nome}: Notas = {notas}, Média = {media:.2f}")