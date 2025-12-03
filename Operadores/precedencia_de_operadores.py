# A procedência dos operadores em Python determina a ordem em que as operações são avaliadas em uma expressão.
# A precedência dos operadores em Python, do mais alto para o mais baixo, é a seguinte:
# 1. Parênteses: ()
# 2. Exponenciação: **
# 3. Multiplicação, Divisão, Divisão Inteira e Resto da Divisão: *, /, //, %
# 4. Adição e Subtração: +, -
# 5. Operadores de comparação: ==, !=, >, <, >=, <=
# 6. Operadores lógicos: not, and, or

# Exemplos para ilustrar a precedência dos operadores:

# Exemplo 1: Uso de parênteses para alterar a precedência
resultado1 = (2 + 3) * 4  # Parênteses alteram a ordem de avaliação
print("Resultado 1:", resultado1)  # Saída: 20
resultado2 = 2 + 3 * 4  # Multiplicação tem precedência sobre adição
print("Resultado 2:", resultado2)  # Saída: 14

# Exemplo 2: Exponenciação
resultado3 = 2 ** 3 ** 2  # Avaliado como 2 ** (3 ** 2)
print("Resultado 3:", resultado3)  # Saída: 512
resultado4 = (2 ** 3) ** 2  # Parênteses alteram a ordem de avaliação
print("Resultado 4:", resultado4)  # Saída: 64

# Exemplo 3: Combinação de operadores
resultado5 = 10 + 5 * 2 - 3 / 1  # Multiplicação e divisão têm precedência sobre adição e subtração
print("Resultado 5:", resultado5)  # Saída: 16.0
resultado6 = (10 + 5) * (2 - 3) / 1  # Parênteses alteram a ordem de avaliação
print("Resultado 6:", resultado6)  # Saída: -15.0

# Exemplo 4: Operadores de comparação e lógicos
a = 5
b = 10
resultado7 = a < b and b > 0  # Comparações são avaliadas antes dos operadores lógicos
print("Resultado 7:", resultado7)  # Saída: True
resultado8 = not (a > b) or (b == 10)  # Parênteses alteram a ordem de avaliação
print("Resultado 8:", resultado8)  # Saída: True
# Esses exemplos ilustram como a precedência dos operadores em Python afeta a avaliação das expressões.