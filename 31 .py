PRECO_DOCE = 1.50
total_geral = 0.0

while True:
    qtd = int(input("Quantos doces deseja comprar? "))
    total_compra = qtd * PRECO_DOCE
    total_geral += total_compra
    print(f"Subtotal dessa compra: R$ {total_compra:.2f}")
    
    resp = input("Deseja continuar comprando? (sim/não): ").strip().lower()
    if resp == 'não' or resp == 'nao':
        break

print(f"Total final da compra: R$ {total_geral:.2f}")