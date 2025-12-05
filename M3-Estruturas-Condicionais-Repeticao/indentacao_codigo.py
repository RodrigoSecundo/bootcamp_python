# A identação correta do código em Python é crucial para definir blocos de código e garantir que o programa funcione conforme esperado.
# Além disso, a identação melhora a legibilidade do código, facilitando a compreensão da estrutura lógica do programa.
# Em Python, a identação é geralmente feita com 4 espaços por nível de indentação. Evite misturar espaços e tabulações para evitar erros.

# Exemplo de estrutura condicional com identação correta
idade = 20
if idade >= 18:
    print("Você é maior de idade.")
    if idade >= 65:
        print("Você é um idoso.")
    else:
        print("Você é um adulto.")
else:
    print("Você é menor de idade.")

# Exemplo de loop com identação correta
for i in range(5):
    print("Número:", i)
    if i % 2 == 0:
        print(i, "é um número par.")
    else:
        print(i, "é um número ímpar.")

# Exemplo de função com identação correta
def saudacao():
    nome = input("Digite seu nome: ")
    if nome == "Clarice":
        print("Bem-vinda de volta, Clarice!")
    else:
        print("Prazer em conhecê-lo(a)!", nome)

saudacao()

# Lembre-se de que a identação incorreta resultará em erros de sintaxe ou comportamento inesperado do programa.
# Exemplo de identação incorreta (descomente para ver o erro)
# if idade >= 18:
# print("Você é maior de idade.")  # Erro de identação
#     print("Você é um adulto.")