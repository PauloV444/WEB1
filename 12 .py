soma = 0
while True:
    num = float(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    soma += num
print(f"Soma total: {soma}")