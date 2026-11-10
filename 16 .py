primeiro = float(input("Digite o 1º número: "))
maior = primeiro
menor = primeiro

for i in range(2, 11):
    num = float(input(f"Digite o {i}º número: "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")