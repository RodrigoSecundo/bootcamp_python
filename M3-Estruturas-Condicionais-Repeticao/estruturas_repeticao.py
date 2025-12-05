# As estruturas de repetição permitem que o programa execute um bloco de código várias vezes, com base em condições específicas.
# Em Python, as principais estruturas de repetição são: for e while.
# O for é indicado par quando sabemos o número de repetições, enquanto o while é usado quando não sabemos o número exato de repetições e dependemos de uma condição.
# Aqui estão alguns exemplos de como usar essas estruturas de repetição:

# Exemplo 1: Estrutura de repetição for
print("Exemplo 1: Estrutura de repetição for")
for i in range(5): #range(5) gera os números de 0 a 4, pois range começa do 0 por padrão
    print("Número:", i)
    if i % 2 == 0:
        print(i, "é um número par.")
    else:
        print(i, "é um número ímpar.")

# range(start, stop, step) também pode ser usado para definir o início, fim e passo da contagem
print("\nExemplo adicional: Uso de range com start, stop e step")
print("São números ímpares:")
for j in range(1, 11, 2): # Começa em 1, vai até 10 (11 não incluso), pulando de 2 em 2
    print(j, end=" ") #end=" " mantém os números na mesma linha separados por espaço
print()

# Exemplo 2: Estrutura de repetição while
print("\nExemplo 2: Estrutura de repetição while")
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1  # Incrementa o contador para evitar loop infinito
    if contador % 2 == 0:
        print(contador, "é um número par.")
    else:
        print(contador, "é um número ímpar.")

# Exemplo 3: Uso de break e continue em loops
print("\nExemplo 3: Uso de break e continue em loops")
for numero in range(10):
    if numero == 5:
        print("Número 5 encontrado, saindo do loop.")
        break  # Sai do loop quando o número é 5
    if numero % 2 == 0:
        continue  # Pula os números pares
    print("Número ímpar:", numero)

# Esses exemplos ilustram como usar estruturas de repetição em Python para executar blocos de código múltiplas vezes com base em diferentes condições.

loucura = 0
while loucura < 1000000000000000000:
    loucura += 1
    print("Nível de loucura:", loucura) # Cuidado para não entrar em loop infinito! (no caso, é finito, mas muito grande)
    if loucura == 1000000000000000000:
        print("Parabéns guerreiro. Nível máximo de loucura atingido!")
    break

# Podemos também usar for para iteráveis como listas e strings

frutas = ["maçã", "banana", "laranja"]
print("\nExemplo 4: Uso de for com listas")
for fruta in frutas:
    print("Fruta:", fruta)
    if fruta == "maçã":
        print("Maçã é a fruta do amor!")
    else:
        print(fruta, "é uma fruta deliciosa!")

print() # linha em branco
print("Exemplo 5: Uso de for com strings")
nome = "Rodrigo"
vogais = "aeiou"

for letra in nome:
    print("Letra:", letra)
    if letra in vogais:
        print(letra, "é uma vogal.")
    else:
        print(letra, "é uma consoante.")
print("\nFim dos exemplos de estruturas de repetição.")

# DESAFIO 1:

infinito = 0
while infinito != 1:
    print("Esse loop é infinito!")
    break # Para evitar o loop infinito, usamos break aqui.

# DESAFIO 2:

numero = 0

while numero % 2 == 0:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Você digitou um número par. Tente novamente.")
    else:
        print("Você digitou um número ímpar. Parabéns!")

# ou

numero = 0

while True:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Você digitou um número par. Tente novamente.")
    else:
        print("Você digitou um número ímpar. Parabéns!")
        break

# ou, muito menos eficiente e não recomendado:

numero = 0

for numero in range(10**10):  # um laço enorme
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Você digitou um número par. Tente novamente.")
    else:
        print("Você digitou um número ímpar. Parabéns!")
        break

# for não é recomendado para esse desafio, pois não sabemos quantas tentativas o usuário fará antes de digitar um número ímpar.

# break é usado para sair do loop quando a condição desejada é atendida.
# outro uso de break seria para sair de loops infinitos criados com while True.
# continue pode ser usado para pular para a próxima iteração do loop, ignorando o código restante na iteração atual.

continue_exemplo = 0
for continue_exemplo in range(10):
    if continue_exemplo % 2 == 0:
        continue  # pula os números pares
    print("Número ímpar (usando continue):", continue_exemplo)

# Nesse exemplo, os números pares são ignorados e apenas os ímpares são impressos.

#DESAFIO 3:

while True:
    abc = int(input("Digite um número: "))

    if abc % 2 == 0:
        continue

    if abc == 10:
        break

    print(abc)

# Nesse desafio, o loop continua pedindo números até que o usuário digite 10.
# Mas como 10 é par, o continue faz com que o break nunca seja alcançado, resultando em um loop infinito.