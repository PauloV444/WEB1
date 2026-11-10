NUMERO_SECRETO = 7
tentativas = 3

for i in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {i} de {tentativas}. Digite um número: "))
    if palpite == NUMERO_SECRETO:
        print("Parabéns! Você adivinhou o número secreto!")
        break
else:
    print("Você esgotou suas tentativas. Derrota!")