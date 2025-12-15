# A interpolação de variáveis em strings permite inserir valores de variáveis diretamente dentro de uma string.
# Existem várias maneiras de fazer isso em Python, incluindo o uso de f-strings, o método .format(), o método usando sinal de % e por fim a concatenação simples.
# A mais moderna e recomendada é o uso de f-strings, introduzido no Python 3.6.

nome = "Caleb"
idade = 4
# ---------------------------------------------
# Exemplo usando .format(), outra forma popular mas um pouco mais verbosa
mensagem_format = "Olá, meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem_format)

# pode-se também usar índices para maior controle
mensagem_format_ordem = "Olá, meu nome é {0} e eu tenho {1} anos. {0} gosta de dinossauros.".format(nome, idade)
print(mensagem_format_ordem)

# outra variação é nomear os parâmetros
mensagem_format_nomeado = "Olá, meu nome é {nome} e eu tenho {idade} anos.".format(nome=nome, idade=idade)
print(mensagem_format_nomeado)

# mas pode ser também por meio de dicionários
dicionario = {"nome": nome, "idade": idade}
mensagem_format_dicionario = "Olá, meu nome é {nome} e eu tenho {idade} anos.".format(**dicionario)
print(mensagem_format_dicionario)

# ---------------------------------------------
# Exemplo usando %, que é uma forma mais antiga
# sendo %s para strings e %d para inteiros e %f para floats
mensagem_percent = "Olá, meu nome é %s e eu tenho %d anos." % (nome, idade)
print(mensagem_percent)

# ---------------------------------------------
# Exemplo usando concatenação simples, menos recomendada por ser menos legível
mensagem_concat = "Olá, meu nome é " + nome + " e eu tenho " + str(idade) + " anos."
print(mensagem_concat)

# ---------------------------------------------
# Exemplo usando f-strings, mais simples, direto e recomendado
mensagem = f"Olá, meu nome é {nome} e eu tenho {idade} anos."
print(mensagem)

# ou diretamente na impressão
print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")

# também é possível fazer expressões dentro das chaves
print(f"Daqui a 5 anos, {nome} terá {idade + 5} anos.")

# e até mesmo formatar números
preco = 49
print(f"O preço do produto é R$ {preco:.2f}")  # Formata para 2 casas decimais

# podemos chamar funções dentro das chaves
print(f"O nome em maiúsculas é {nome.upper()}.")

# exemplo com função real
def saudacao(n):
    return f"Seja bem-vindo, {n}!"
print(f"{saudacao(nome)}")

# visto isso, podemos considerar que f-strings são a forma mais prática e eficiente de interpolar variáveis em strings no Python moderno.