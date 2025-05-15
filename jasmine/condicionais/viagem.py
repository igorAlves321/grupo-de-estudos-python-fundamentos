distância = int(input("Qual será a distância, em quilômetros, da sua viagem?"))
if distância <= 200:
    print(f"Sua passagem custará {distância*0.50:.2f} reais.")
else:
    print(f"Sua passagem custará {distância*0.45:.2f} reais.")