# O fatiamento de tuplas em Python permite extrair partes específicas de uma tupla usando a notação de colchetes [] com índices.
# A sintaxe básica para fatiamento é: tupla[início:fim:passo]

tupla = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# 1. Extraindo uma subtupla do índice 0 ao 5 (exclusivo)
print(tupla[0:6])  # Saída: (10, 20, 30, 40, 50, 60)

# 2. Extraindo do índice 4 até o final
print(tupla[4:])  # Saída: (50, 60, 70, 80, 90, 100)

# 3. Extraindo do início até o índice 5 (exclusivo)
print(tupla[:6])  # Saída: (10, 20, 30, 40, 50, 60)

# 4. Extraindo com passo (pula de 2 em 2)
print(tupla[0:10:2])  # Saída: (10, 30, 50, 70, 90)

# 5. Extraindo a tupla inteira com passo (inverte a tupla)
print(tupla[::-1])  # Saída: (100, 90, 80, 70, 60, 50, 40, 30, 20, 10)

# Funciona basicamente da mesma forma que em strings e listas, mas como tuplas são imutáveis, o fatiamento retorna uma nova tupla.