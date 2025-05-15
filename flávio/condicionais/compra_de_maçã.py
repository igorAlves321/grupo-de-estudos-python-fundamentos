quantidade = int(input("Digite a quantidade de maçãs a serem compradas"))

if quantidade < 12:
    preco_por_maca = 1.30
else:
    preco_por_maca = 1.00


custo_total = quantidade * preco_por_maca
print(f"O custo total da compra é: R$ {custo_total:.2f}")