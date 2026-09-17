valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    maior = valor1
    menor = valor2
else:
    maior = valor2
    menor = valor1

if maior % menor == 0:
    print("O maior número é múltiplo do menor.")
else:
    print("O maior número não é múltiplo do menor.")