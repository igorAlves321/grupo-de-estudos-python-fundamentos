a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a > b and a > c:
    print("a é o maior número.")
elif b > a and b > c:
    print("b é o maior número.")
elif c > a and c > b:
    print("c é o maior número.")
else:
    print("Existe uma igualdade entre os números.")