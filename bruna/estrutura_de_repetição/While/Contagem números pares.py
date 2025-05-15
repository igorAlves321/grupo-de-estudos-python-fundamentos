contador = 1
quantidade_pares = 0

while contador <= 100:
    if contador % 2 == 0:
        quantidade_pares += 1
    contador += 1

print("Quantidade de números pares entre 1 e 100:", quantidade_pares)