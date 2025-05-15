soma = 0
for i in range(6):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        soma += numero
print(f"Soma dos números pares: {soma}")