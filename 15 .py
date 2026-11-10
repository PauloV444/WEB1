qtd = 0
while True:
    num = float(input("Digite um número (negativo para parar): "))
    if num < 0:
        break
    qtd += 1
print(f"Você digitou {qtd} números não negativos.")