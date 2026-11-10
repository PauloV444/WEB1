num = input("Digite um número inteiro: ").strip()
if num.startswith('-'):
    num = num[1:]
print(f"O número possui {len(num)} dígitos.")