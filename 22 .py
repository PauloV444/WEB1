idades = []
for i in range(1, 6):
    idade = int(input(f"Digite a {i}ª idade: "))
    idades.append(idade)

media = sum(idades) / len(idades)
print(f"Média das idades: {media:.2f}")
print("Idades acima da média:")
for idade in idades:
    if idade > media:
        print(idade)