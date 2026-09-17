valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    maior = valor1
    menor = valor2
else:
    maior = valor2
    menor = valor1

for numero in range(menor, maior + 1):
    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores = divisores + 1

    if divisores == 2:
        print(numero)