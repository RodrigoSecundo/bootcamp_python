# DESAFIO 03 — Avaliação de aluno (Condicionais)
#
# Objetivo: treinar `if/elif/else`, condições com `and/or/not` e entradas convertidas.
#
# Regras:
# Você vai decidir o status de um aluno baseado em nota e faltas.
#
# Requisitos:
# 1) Peça ao usuário:
#    - nome
#    - nota (0 a 10) (float)
#    - faltas (int)
# 2) Validação simples:
#    - Se nota < 0 ou nota > 10, imprima "Nota inválida".
# 3) Caso a nota seja válida, determine o status:
#    - Se faltas > 10: "REPROVADO POR FALTAS"
#    - Senão, se nota >= 7: "APROVADO"
#    - Senão, se nota >= 5 e nota < 7: "RECUPERAÇÃO"
#    - Senão: "REPROVADO"
# 4) Imprima uma mensagem final usando f-string, por exemplo:
#    "Aluno(a) X: nota Y, faltas Z → STATUS"
# 5) Use pelo menos uma condição com `and` e uma com `or` (mesmo que seja na validação).
#
# Dicas:
# - Lembre: ordem das regras importa.
# - Você pode usar uma variável `status` e depois imprimir.
# - Pode usar condicional ternária para uma mensagem curta (opcional).
#
# (Opcional) Desafio extra:
# - Se o nome digitado estiver vazio ("" depois de `.strip()`), peça novamente.

print("Desafio 3:")

nome = input("Digite o nome do aluno: ")
nota = input("Digite a nota do aluno, com casas decimais se houver (0-10): ")
faltas = input("Digite a quantidade de faltas do aluno em questão: ")

nota = nota.replace(",", ".")
nota = float(nota)
faltas = int(faltas)

if nota < 0 or nota > 10:
    print("Essa nota é inválida...")
elif faltas > 10:
    print(f"""
          Aluno(a): {nome}
          Nota: {nota:.1f}
          Faltas: {faltas}
          Status: O aluno está reprovado por faltas!""")
elif nota >= 7:
    print(f"""
          Aluno(a): {nome}
          Nota: {nota:.1f}
          Faltas: {faltas}
          Status: O aluno está aprovado!""")
elif nota >= 5 and nota < 7:
    print(f"""
          Aluno(a): {nome}
          Nota: {nota:.1f}
          Faltas: {faltas}
          Status: O aluno irá para a recuperação!""")
else:
    print(f"""
          Aluno(a): {nome}
          Nota: {nota:.1f}
          Faltas: {faltas}
          Status: O aluno está reprovado por nota!""")