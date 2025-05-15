quantidade = int(input("Quantas maçãs você deseja comprar?"))
if quantidade < 12:
    preco = 1.30
else:
    preco = 1.0
custo = quantidade*preco
print(f"O valor de sua compra será R${custo:.2f}.")