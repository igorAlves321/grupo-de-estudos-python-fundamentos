velocidade = int (input("Digite a velocidade do carro"))
limite = 80
if velocidade > 80:
    multa = (velocidade - 80)*7
    print("O motorista será multado",multa)
else:
    print("O motorista não será multado")