soma_notas_pesos = 0
soma_pesos = 0

for i in range(1, 4):
    nota = float(input(f"Digite a {i}ª nota: "))
    peso = float(input(f"Digite o peso da {i}ª nota: "))
    soma_notas_pesos += nota * peso
    soma_pesos += peso

media_ponderada = soma_notas_pesos / soma_pesos
print(f"Média ponderada: {media_ponderada:.2f}")