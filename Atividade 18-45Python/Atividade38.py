maior = 0
menor = 0

for i in range(100):
    numero = int(input("Digite um número positivo: "))

    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

print("Maior =", maior)
print("Menor =", menor)