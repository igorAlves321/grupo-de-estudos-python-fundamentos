velocidade = int(input("Qual a velocidade do carro?"))
limite = 80
valor_multa = 7.00
excesso = velocidade - limite
multa = excesso * valor_multa
if velocidade > limite:
    print(f"Você estava {excesso} KM acima do limite de velocidade! Sua multa será de {multa} reais.")
else:
    print(f"Você estava dentro do limite de velocidade, parabéns.")