# Entre os principais métodos úteis para manipulação de strings em Python, destacam-se:
# 1. .upper(): Converte todos os caracteres da string para maiúsculas.
# 2. .lower(): Converte todos os caracteres da string para minúsculas.
# 3. .title(): Converte a primeira letra de cada palavra para maiúscula.
# 4. .strip(): Remove espaços em branco no início e no final da string.
# 5. .center(width, fillchar): Centraliza a string em um campo de largura especificada, preenchendo com o caractere fornecido (padrão é espaço).
# 6. .join(iterable): Junta uma lista de strings em uma única string, usando a string original como separador.
# 7. .replace(old, new): Substitui todas as ocorrências de uma substring por outra.
# 8. .split(sep): Divide a string em uma lista de substrings com base em um separador.
# 9. .find(sub): Funciona para encontrar a posição da primeira ocorrência de uma substring dentro da string. Retorna -1 se não for encontrada.
# 10. .format(): Formata a string, permitindo a inserção de variáveis
# 11. f-strings (a partir do Python 3.6): Permite a inclusão direta de expressões dentro de strings.
# 12. len(): Retorna o comprimento (número de caracteres) da string. Não é um método da string, mas uma função embutida do Python que é amplamente usada com strings.

# Exemplos de uso dos métodos mencionados:
texto = "pYThOn é InCrÍvEl!"

# 1. .upper()
print(texto.upper())  # Saída: "PYTHON É INCRÍVEL!"

# 2. .lower()
print(texto.lower())  # Saída: "python é incrível!"

# 3. .title()
print(texto.title())  # Saída: "Python É Incrível!"

# 4. .strip()
texto_com_espacos = "   Olá, Mundo!   "
print(texto_com_espacos.strip())  # Saída: "Olá, Mundo!"

# 4.1 .lstrip() e .rstrip()
print(texto_com_espacos.lstrip())  # Saída: "Olá, Mundo!   "
print(texto_com_espacos.rstrip())  # Saída: "   Olá, Mundo!"

# 5. .center(width, fillchar) OBS: width é o número total de caracteres da nova string e fillchar é o caractere usado para preencher os espaços
print(texto.center(30, '-'))  # Saída: "--------pYThOn é InCrÍvEl!--------"
# lembrando que se o width for menor que o tamanho da string original, nada acontece:
print(texto.center(10, '-'))  # Saída: "pYThOn é InCrÍvEl!"

# 6. .join(iterable)
palavras = ["Python", "é", "incrível"]
print(" ".join(palavras))  # Saída: "Python é incrível"
# também 
print("-".join(texto))  # Saída: "p-Y-T-h-O-n- -é- -I-n-C-r-Í-v-E-l-!"

# 7. .replace(old, new)
print(texto.replace("InCrÍvEl", "fantástico"))  # Saída: "pYThOn é fantástico!"

# 8. .split(sep)
print(texto.split(" "))  # Saída: ['pYThOn', 'é', 'InCrÍvEl!']

# 9. .find(sub)
print(texto.find("InCrÍvEl"))  # Saída: 9
print(texto.find("Java"))      # Saída: -1

# 10. .format()
nome = "Clarice"
idade = "0 aninhos"
print("Meu nome é {} e eu tenho {} ainda.".format(nome, idade))
# Saída: "Meu nome é Clarice e eu tenho 0 aninhos ainda."

# 11. f-strings
print(f"Meu nome é {nome} e eu tenho {idade} ainda.")
# Saída: "Meu nome é Clarice e eu tenho 0 aninhos ainda."

# 12. len()
print(len(texto))  # Saída: 18

# Esses métodos são amplamente utilizados para manipulação e formatação de strings em Python, facilitando diversas operações comuns no dia a dia da programação.
