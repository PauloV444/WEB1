capital = float(input("Digite o capital inicial: R$ "))
taxa_mensal = float(input("Digite a taxa de juros mensal (%): ")) / 100
meses = int(input("Digite o número de meses: "))

saldo = capital

print("\nEvolução do investimento:")
for mes in range(1, meses + 1):
    saldo += saldo * taxa_mensal
    print(f"Mês {mes}: R$ {saldo:.2f}")

print(f"\nSaldo final acumulado: R$ {saldo:.2f}")