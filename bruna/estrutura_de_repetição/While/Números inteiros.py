soma_pares = 0
contador = 0
while contador < 6:
    numero = int(input(f"Digite o {contador+1}º número inteiro: "))
    numero = int(input(f"Digite o {contador+2}º número inteiro: "))

    if numero % 2 == 0:
        soma_pares += numero
contador += 1
print(f"A soma dos números pares é: {soma_pares}")


