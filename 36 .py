votos = {"A": 0, "B": 0, "C": 0}

while True:
    voto = input("Vote no candidato (A, B, C) ou digite 'fim' para encerrar: ").strip().upper()
    if voto == 'FIM':
        break
    if voto in votos:
        votos[voto] += 1
    else:
        print("Candidato inválido! Tente novamente.")

print("\n--- Resultado da Votação ---")
for cand, total in votos.items():
    print(f"Candidato {cand}: {total} voto(s)")

maior_voto = max(votos.values())
if list(votos.values()).count(maior_voto) > 1 and maior_voto > 0:
    print("Houve um empate!")
elif maior_voto == 0:
    print("Nenhum voto foi registrado.")
else:
    vencedor = max(votos, key=votos.get)
    print(f"Vencedor: Candidato {vencedor}")