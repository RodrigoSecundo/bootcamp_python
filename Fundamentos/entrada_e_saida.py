#input sempre vai retornar uma string
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")
print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Tipo da variável nome:", type(nome))
print("Tipo da variável idade:", type(idade))
print("Tipo da variável altura:", type(altura))

# input pode receber APENAS 1 argumento: prompt
# print pode receber SEP, END, FILE e FLUSH

# prompt: texto exibido antes da entrada
idade2 = input("Digite sua idade: ")
print("Idade:", idade2)

# sep: separador entre os valores dentro do print
altura2 = input("Digite sua altura: ")
escala = "metros"
print("Altura:", altura2, escala, sep=" -> ")

# end: final da linha (substitui o \n)
peso = input("Digite seu peso: ")
print("Peso:", peso, end=" kg\n")

# file: arquivo para onde o print escreve (padrão é sys.stdout)
cidade = input("Digite sua cidade: ")
print("Cidade:", cidade, file=None)

# flush: força escrita imediata
pais = input("Digite seu país: ")
print("País:", pais, flush=True)
