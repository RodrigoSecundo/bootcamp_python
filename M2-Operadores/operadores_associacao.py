# Os operadores de associação em Python são usados para verificar se um valor está presente em uma sequência (como listas, tuplas, strings, etc.) ou em um conjunto de valores.
# Os principais operadores de associação em Python são "in" e "not in".

# Operador de associação "in"
frutas = ['maçã', 'banana', 'laranja']
print("Operador 'in':")
print("'banana' in frutas:", 'banana' in frutas)  # True, pois 'banana' está na lista
print("'uva' in frutas:", 'uva' in frutas)        # False, pois 'uva' não está na lista

# Operador de associação "not in"
print("\nOperador 'not in':")
print("'banana' not in frutas:", 'banana' not in frutas)  # False, pois 'banana' está na lista
print("'uva' not in frutas:", 'uva' not in frutas)        # True, pois 'uva' não está na lista

# Exemplo adicional com strings
texto = "Olá, mundo!"
print("\nExemplo com strings:")
print("'mundo' in texto:", 'mundo' in texto)            # True, pois 'mundo' está na string
print("'Python' not in texto:", 'Python' not in texto)  # True, pois 'Python' não está na string

# operador de associação com tuplas
tupla_numeros = (1, 2, 3, 4, 5)
print("\nExemplo com tuplas:")
print("3 in tupla_numeros:", 3 in tupla_numeros)          # True, pois 3 está na tupla
print("6 not in tupla_numeros:", 6 not in tupla_numeros)  # True, pois 6 não está na tupla

# É importante lembrar que os operadores de associação são case-sensitive quando usados com strings.
# Por exemplo:
print("\nExemplo case-sensitive:")
print("'Mundo' in texto:", 'Mundo' in texto)  # False, pois 'Mundo' com 'M' maiúsculo não está na string

# Esses operadores são úteis para verificar a presença ou ausência de elementos em coleções e sequências em Python.