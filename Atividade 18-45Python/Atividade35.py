valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    maior = valor1
    menor = valor2
else:
    maior = valor2
    menor = valor1

soma = 0

for i in range(menor, maior + 1):
    if i % 2 != 0:
        soma = soma + i

print("Soma dos ímpares =", soma)