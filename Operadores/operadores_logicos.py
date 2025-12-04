# Os operadores lógicos em Python são usados para combinar expressões booleanas.
# Eles retornam valores booleanos (True ou False) com base nas condições avaliadas.
# Aqui estão os principais operadores lógicos em Python:

# Operador AND: and
a = True
b = False
resultado_and = a and b  # Retorna True se ambos a e b forem True
print("Operador AND (True and False):", resultado_and)  # False

# Operador OR: or
resultado_or = a or b  # Retorna True se pelo menos um de a ou b for True
print("Operador OR (True or False):", resultado_or)  # True

# Operador NOT: not
resultado_not = not a  # Retorna True se a for False, e vice-versa
print("Operador NOT (not True):", resultado_not)  # False

# Outro exemplo com expressão mais complexas
x = 5
y = 10

# Verifica se x é maior que 3 e y é menor que 15
condicao_and = (x > 3) and (y < 15)
print("Condição (x > 3 and y < 15):", condicao_and)  # True

# Verifica se x é menor que 3 ou y é maior que 15
condicao_or = (x < 3) or (y > 15)
print("Condição (x < 3 or y > 15):", condicao_or)  # False

# Inverte o valor booleano de uma expressão
condicao_not = not (x == 5)
print("Condição (not (x == 5)):", condicao_not)  # False

# Os parênteses podem ser usados para agrupar expressões e controlar a ordem de avaliação.
# Um exemplo de uso combinado dos operadores lógicos:
T = 10
L = 20
complexa = ((T > 5) and (L < 25)) or not (T == 10)
print("Condição complexa:", complexa)  # True