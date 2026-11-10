soma_notas = 0
for i in range(1, 11):
    nota = float(input(f"Digite a nota do {i}º aluno: "))
    soma_notas += nota
media = soma_notas / 10
print(f"A média geral da turma é: {media:.2f}")