# Strings de múltiplas linhas em Python podem ser criadas usando três aspas simples (''') ou três aspas duplas (""").
# Isso é útil para criar strings que se estendem por várias linhas, como documentos, mensagens ou blocos de texto formatados.

mensagem = """Olá,
Este é um exemplo de string
que se estende por várias linhas.
Você pode incluir quebras de linha, tabulações e outros caracteres especiais
sem a necessidade de usar caracteres de escape."""

print(mensagem)

mensagem2 = '''Outra forma de criar
strings de múltiplas linhas
é usando aspas simples triplas.'''

print(mensagem2)

# Você também pode usar strings de múltiplas linhas para criar docstrings, que são usadas para documentar funções, classes e módulos em Python.
def minha_funcao():
    """Esta função é um exemplo de docstring.
    
    Ela não faz nada, mas serve para ilustrar
    como usar strings de múltiplas linhas para documentação.
    """
    pass
print(minha_funcao.__doc__)

# Além disso, strings de múltiplas linhas preservam a formatação original, incluindo espaços em branco e quebras de linha.
texto_formatado = """Linha 1
    Linha 2 com indentação      
Linha 3 sem indentação"""
print(texto_formatado)

# Você também pode usar a barra invertida (\) no final de uma linha para continuar a string na linha seguinte sem adicionar uma nova linha.
texto_continuado = "Esta é uma string que continua na linha seguinte " \
                   "sem adicionar uma nova linha no meio."
print(texto_continuado)

# Strings de múltiplas linhas são especialmente úteis para criar mensagens longas, documentação e blocos de texto formatados de maneira clara e legível.