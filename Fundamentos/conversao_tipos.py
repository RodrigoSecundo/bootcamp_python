nota = 8
nome = "Rodrigo"
media = 7.5

#print normal
print("Nome:", nome)
print("Nota:", nota)
print("Média:", media)

#usando f-strings
texto = f"{nome} tem nota {nota} e a média é {media}"
print(texto)

#ou podemos fazer direto no print
print(f"{nome} tem nota {nota} e a média é {media}")

numero1 = 8
numero2 = 2.5
numero3 = 10.10
numero4 = "15"

print(type(numero1))  # verifica o tipo da variável
print(type(numero2))  # verifica o tipo da variável

# funciona porque é possível converter um número inteiro em decimal,
print(float(numero1))

# funciona porque é possível converter um número decimal em inteiro (perde a parte decimal, não importa a quantidade de casas)
print(int(numero2))

# responde 10.1 pois o 0 à direita não altera o valor do número
print(float(numero3))

#funciona porque é possível converter uma string que representa um número em inteiro ou decimal
print(int(numero4))  # converte string para inteiro
print(float(numero4))  # converte string para decimal

# não funciona porque não é possível converter uma string não numérica em número
# print(int(nome))

print(float("1,24".replace(",", ".")))  # substitui o ponto por vírgula e converte para decimal

# funciona porque é possível converter um número em string
print(str(numero1))

print(type(str(numero1)))  # verifica o tipo da variável após a conversão
print(type(float(numero4)))  # verifica o tipo da variável após a conversão

numero5 = 10.000

print(numero5 / 2)  # divisão normal
print(numero5 // 2)  # divisão inteira
print(numero5 % 3)  # resto da divisão
print(numero5 ** 2)  # exponenciação
print(numero5 ** (1/2))  # raiz quadrada
print(numero5 ** (1/3))  # raiz cúbica