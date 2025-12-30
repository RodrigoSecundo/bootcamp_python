# DESAFIO 05 — Formatador de texto (Strings)
#
# Objetivo: treinar fatiamento, métodos úteis de string e formatação (f-string / .format).
# Conteúdos do módulo: strip, upper/lower/title, replace, split, join, find, len, slicing.
#
# Requisitos:
# 1) Peça ao usuário uma frase (pode ter espaços extras e letras misturadas).
# 2) Crie uma versão "normalizada" da frase:
#    - Remova espaços do começo e do fim (`strip()`)
#    - Transforme em minúsculas (`lower()`)
# 3) Remova espaços duplos e espaços desnecessários usando .join
# 3) Exiba:
#    - a frase original
#    - a frase normalizada
#    - quantidade de caracteres (len) da normalizada
#    - quantidade de palavras (len do split)
# 4) Peça ao usuário uma palavra para buscar dentro da frase normalizada.
#    - Use `.find()` e imprima:
#      * se encontrou (índice >= 0)
#      * se não encontrou (índice == -1)
# 5) Mostre 3 recortes (fatiamento) da frase normalizada:
#    - os 5 primeiros caracteres
#    - os 5 últimos caracteres
#    - a frase invertida (`[::-1]`)
# 6) Monte um "cartão" final formatado usando f-string OU `.format()`.
#
# Exemplo de cartão (modelo):
# -------------------------
# Texto normalizado: "..."
# Palavras: 7 | Caracteres: 31
# Busca: "python" -> encontrado na posição 10
# -------------------------
#
# (Opcional) Desafio extra:
# - Transforme a frase em "Título" (`title()`) e exiba.
# - Substitua caracteres específicos (ex: troque "a" por "@") com `replace()`.

frase = input("Crie uma frase (pode ter espaços extras e letras misturadas): ")

frase_formatada = frase.lower().strip()
frase_formatada = " ".join(frase_formatada.split())

print(f"A frase original era: {frase}")
print(f"A frase formatada é: {frase_formatada}")
print(f"O tamanho da frase formatada é: {len(frase_formatada)}")
print(f"O tamanho da frase formatada é: {len(frase_formatada.split())}")

busca = input("Faça a pesquisa de alguma palavra em sua frase: ")

if busca in frase_formatada:
    print(f"A palavra que você pesquisou existe na frase e começa no índice: {frase_formatada.find(busca)}")
else:
    print(f"Essa palavra não existe na sua frase...")

print("Fatiando a frase: ")
print(f"Primeiros 5 índices: {frase_formatada[:5]}")
print(f"Os 5 últimos índices: {frase_formatada[-5::]}")
print(f"Frase invertida: {frase_formatada[::-1]}")

