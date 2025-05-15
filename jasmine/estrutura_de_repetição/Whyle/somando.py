soma = 0
entrada = input("Digite um número, ou fim para sair.")
while entrada != "fim":
    soma += int(entrada)
    entrada = input("Digite outro número, ou fim para sair.")
print(f"O total é {soma}")