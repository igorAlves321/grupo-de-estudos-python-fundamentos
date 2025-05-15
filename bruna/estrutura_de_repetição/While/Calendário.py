while True:
    numero = int(input("Digite o número do mês de 1 a 12"))
    if 1 <= numero <=12:
        nome_mes = meses[numero]
        if numero in [12, 1, 2[:
            estacao = "Verão"
        elif numero in [3, 4, 5]:
            estacao = "Outono"
    elif numero in [6, 7, 8]:
        estacao = "Inverno"
    else:
        estacao = "Primavera"
        print(f"\nMês: {nome_mes}")
        print(f"Estação: {estacao}")
        break


    ]]