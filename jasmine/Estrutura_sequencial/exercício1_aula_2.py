n1 = float(input("Por favor, digite um número."))
n2 = float(input("Digite outro número."))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
print(f"A soma dos números é {soma}.")
print(f"A subtração dos números é {subtracao}.")
print(f"A multiplicação dos números é {multiplicacao}.")
if n2 !=0:
    divisao = n1 / n2
    print(f"A divisão dos números é {divisao}")
else:
    print("Não é possível dividir por 0.")
