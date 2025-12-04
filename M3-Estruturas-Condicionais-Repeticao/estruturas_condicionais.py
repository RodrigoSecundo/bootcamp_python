# As estruturas condicionais permitem que o programa tome decisões com base em condições específicas.
# Em Python, as principais estruturas condicionais são: if, elif e else.
# Aqui estão alguns exemplos de como usar essas estruturas condicionais:

# Exemplo 1: Estrutura condicional simples
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Exemplo 2: Estrutura condicional com múltiplas condições
nota = 85
if nota >= 90:
    print("Você recebeu um A.")
elif nota >= 80:
    print("Você recebeu um B.")
elif nota >= 70:
    print("Você recebeu um C.")
elif nota >= 60:
    print("Você recebeu um D.")
else:
    print("Você recebeu um F.")

# Exemplo 3: Estrutura condicional aninhada
numero = 10
if numero > 0:
    print("O número é positivo.")
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
else:
    print("O número é negativo ou zero.")

# Exemplo 4: Estrtrutura condicional ternária
idade = 20
status = "maior de idade" if idade >= 18 else "menor de idade"
print("Você é", status + ".")

# Esses exemplos ilustram como usar estruturas condicionais em Python para controlar o fluxo do programa com base em diferentes condições.