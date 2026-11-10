while True:
    print("\n--- MENU DE CONVERSÃO ---")
    print("1. Converter número")
    print("2. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '2':
        print("Saindo do programa...")
        break
    elif opcao == '1':
        num = int(input("Digite um número inteiro: "))
        print(f"Binário: {bin(num)[2:]}")
        print(f"Octal: {oct(num)[2:]}")
        print(f"Hexadecimal: {hex(num)[2:].upper()}")
    else:
        print("Opção inválida!")