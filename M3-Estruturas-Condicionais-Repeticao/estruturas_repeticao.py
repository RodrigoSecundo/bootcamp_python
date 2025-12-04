# As estruturas de repetição permitem que o programa execute um bloco de código várias vezes, com base em condições específicas.
# Em Python, as principais estruturas de repetição são: for e while.
# O for é indicado par quando sabemos o número de repetições, enquanto o while é usado quando não sabemos o número exato de repetições e dependemos de uma condição.
# Aqui estão alguns exemplos de como usar essas estruturas de repetição:

# Exemplo 1: Estrutura de repetição for
print("Exemplo 1: Estrutura de repetição for")
for i in range(5):
    print("Número:", i)
    if i % 2 == 0:
        print(i, "é um número par.")
    else:
        print(i, "é um número ímpar.")

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

