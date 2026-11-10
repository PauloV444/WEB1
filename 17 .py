num = int(input("Digite um número inteiro: "))
fatorial = 1

if num < 0:
    print("Não existe fatorial de número negativo.")
else:
    for i in range(1, num + 1):
        fatorial *= i
    print(f"O fatorial de {num} é {fatorial}")