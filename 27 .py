palavra = input("Digite uma palavra: ").lower()
vogais = "aeiouáéíóúâêîôûãõ"
contador = 0

for letra in palavra:
    if letra in vogais:
        contador += 1

print(f"A palavra contém {contador} vogal(is).")