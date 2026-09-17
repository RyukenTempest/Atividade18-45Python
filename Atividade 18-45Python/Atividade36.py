n = int(input("Digite N: "))

soma = 1
fatorial = 1

for i in range(1, n + 1):
    fatorial = fatorial * i
    soma = soma + (1 / fatorial)

print("Soma =", soma)