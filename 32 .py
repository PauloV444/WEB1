SENHA_CORRETA = "python123"

while True:
    senha = input("Digite a senha: ")
    if senha == SENHA_CORRETA:
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta! Tente novamente.")