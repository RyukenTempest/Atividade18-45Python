n = int(input("Digite N: "))

soma = 0

for i in range(1, n + 1):
    soma = soma + (1 / i)

print("Soma =", soma)