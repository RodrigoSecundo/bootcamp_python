# Os operadores de identidade em Python são usados para comparar a identidade de dois objetos, ou seja, para verificar se ambos os operandos referenciam o mesmo objeto na memória.
# Os principais operadores de identidade em Python são "is" e "is not".

# Operador de identidade "is"
a = [1, 2, 3]
b = a  # b referencia o mesmo objeto que a
c = [1, 2, 3]  # c é um novo objeto com o mesmo conteúdo que a

print("Operador 'is':")
print("a is b:", a is b)  # True, pois ambos referenciam o mesmo objeto
print("a is c:", a is c)  # False, pois são objetos diferentes, apesar de terem o mesmo conteúdo

# Operador de identidade "is not"
print("\nOperador 'is not':")
print("a is not b:", a is not b)  # False, pois ambos referenciam o mesmo objeto
print("a is not c:", a is not c)  # True, pois são objetos diferentes

# Exemplo adicional com tipos imutáveis
x = 1000
y = 1000
print("\nExemplo com tipos imutáveis:")
print("x is y:", x is y)  # Pode ser True ou False dependendo da implementação do Python
print("x is not y:", x is not y)  # Pode ser False ou True dependendo da implementação do Python

# Nota: Para pequenos inteiros e strings, o Python pode reutilizar objetos, então "is" pode retornar True para valores iguais. No entanto, isso não deve ser usado para comparar valores; use "==" para comparar valores.