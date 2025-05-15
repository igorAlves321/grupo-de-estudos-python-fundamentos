ano_atual = int(input("Digite o ano atual: "))
maiores = 0
menores = 0
for i in range(7):
    nascimento = int(input("Digite o ano de nascimento: "))
    idade = ano_atual - nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f"Pessoas maiores de idade: {maiores}")
print(f"Pessoas menores de idade: {menores}")