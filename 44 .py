numeros = []
for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)

print("Números em ordem inversa:")
for num in reversed(numeros):
    print(num)