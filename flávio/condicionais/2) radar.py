velocidade_veiculo = int(input("Informe a velocidade do veículo: "))
if velocidade_veiculo > 80:
    excesso_velocidade = velocidade_veiculo - 80
    valor_multa = excesso_velocidade * 7
    print(f"Alerta! Você ultrapassou o limite! Sua multa será no valor de: {valor_multa}")
else:
    print("Sem novidades.")