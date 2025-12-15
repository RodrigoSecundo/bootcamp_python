# O fatiamento de strings em Python permite extrair partes específicas de uma string usando a notação de colchetes [] com índices.
# A sintaxe básica para fatiamento é: string[início:fim:passo]

texto = "Python é uma maravilha"

# 1. Extraindo uma substring do índice 0 ao 5 (exclusivo)
print(texto[0:6])  # Saída: "Python"

# 2. Extraindo do índice 10 até o final
print(texto[10:])  # Saída: "uma maravilha"

# 3. Extraindo do início até o índice 5 (exclusivo)
print(texto[:6])  # Saída: "Python"

# 4. Extraindo com passo (pula de 2 em 2)
print(texto[0:20:2])  # Saída: "Pto u aai"

# 5. Extraindo a string inteira com passo (inverte a string)
print(texto[::-1])  # Saída: "ahlivaram amu é nohtyP"

# 6. Extraindo os últimos 7 caracteres
print(texto[-7:])  # Saída: "maravilha"

# 7. Extraindo do início até o índice -8 (exclusivo)
print(texto[:-8])  # Saída: "Python é uma "

# 8. Extraindo do índice -7 até o índice -1 (exclusivo)
print(texto[-7:-1])  # Saída: "maravil"

# 9. Extraindo com passo negativo (inverte a string)
print(texto[20:0:-1])  # Saída: "ahlivaram amu é nohty"

# 10. Extraindo caracteres específicos
print(texto[::3])  # Saída: "Ph u ai"