mes = 0

while mes < 1 or mes > 12:
    mes = int(input("Digite o número de um mês (1 a 12): "))
    if mes < 1 or mes > 12:
        print("Número inválido. Tente novamente.")

if mes == 1:
    nome = "Janeiro"
    estacao = "Verão"
elif mes == 2:
    nome = "Fevereiro"
    estacao = "Verão"
elif mes == 3:
    nome = "Março"
    estacao = "Outono"
elif mes == 4:
    nome = "Abril"
    estacao = "Outono"
elif mes == 5:
    nome = "Maio"
    estacao = "Outono"
elif mes == 6:
    nome = "Junho"
    estacao = "Inverno"
elif mes == 7:
    nome = "Julho"
    estacao = "Inverno"
elif mes == 8:
    nome = "Agosto"
    estacao = "Inverno"
elif mes == 9:
    nome = "Setembro"
    estacao = "Primavera"
elif mes == 10:
    nome = "Outubro"
    estacao = "Primavera"
elif mes == 11:
    nome = "Novembro"
    estacao = "Primavera"
else:  # mes == 12
    nome = "Dezembro"
    estacao = "Verão"

print("\nMês:", nome)
print("Estação do ano:", estacao)
