numero_atual = 1
numero_par = 0
while numero_atual <= 100:
    if numero_atual%2 == 0:
     numero_par += 1
    numero_atual +=1
    print(f"Existem {numero_par} números pares. ")