numero = int(input("Digite o número de um mês (1 a 12): "))
while numero < 1 or numero > 12:
    print("Número inválido. Tente novamente.")
    numero = int(input("Digite o número de um mês (1 a 12): "))
if numero == 1:
    mes = "Janeiro"
    estacao = "Verão"
elif numero == 2:
    mes = "Fevereiro"
    estacao = "Verão"
elif numero == 3:
    mes = "Março"
    estacao = "Outono"
elif numero == 4:
    mes = "Abril"
    estacao = "Outono"
elif numero == 5:
    mes = "Maio"
    estacao = "Outono"
elif numero == 6:
    mes = "Junho"
    estacao = "Inverno"
elif numero == 7:
    mes = "Julho"
    estacao = "Inverno"
elif numero == 8:
    mes = "Agosto"
    estacao = "Inverno"
elif numero == 9:
    mes = "Setembro"
    estacao = "Primavera"
elif numero == 10:
    mes = "Outubro"
    estacao = "Primavera"
elif numero == 11:
    mes = "Novembro"
    estacao = "Primavera"
else:
    mes = "Dezembro"
    estacao = "Verão"

print(f"Mês: {mes}")
print(f"Estação: {estacao}")