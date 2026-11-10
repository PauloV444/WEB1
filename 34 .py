import random

numero_secreto = random.randint(1, 50)
palpite = 0

print("Adivinhe o número secreto entre 1 e 50!")

while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))
    if palpite < numero_secreto:
        print("O número secreto é maior!")
    elif palpite > numero_secreto:
        print("O número secreto é menor!")

print("Parabéns! Você acertou!")