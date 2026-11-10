v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

inicio = min(v1, v2)
fim = max(v1, v2)

soma_impares = 0
for i in range(inicio + 1, fim):
    if i % 2 != 0:
        soma_impares += i

print(f"A soma dos números ímpares entre {inicio} e {fim} é: {soma_impares}")