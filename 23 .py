valor = int(input("Digite o valor do saque: R$ "))
cedulas = [100, 50, 20, 10, 5]

print("Notas entregues:")
for cedula in cedulas:
    qtd = valor // cedula
    if qtd > 0:
        print(f"{qtd} nota(s) de R$ {cedula}")
        valor %= cedula

if valor > 0:
    print(f"Sobrou R$ {valor} que não pôde ser sacado com as notas disponíveis.")