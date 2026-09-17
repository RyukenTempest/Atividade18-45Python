valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))
valor4 = float(input("Digite o quarto valor: "))

if valor4 <= valor1:
    print(valor4, valor1, valor2, valor3)
elif valor4 <= valor2:
    print(valor1, valor4, valor2, valor3)
elif valor4 <= valor3:
    print(valor1, valor2, valor4, valor3)
else:
    print(valor1, valor2, valor3, valor4)