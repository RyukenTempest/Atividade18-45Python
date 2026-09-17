soma = 0

for i in range(1, 16):
    termo = i / (i ** 2)

    if i % 2 == 0:
        soma = soma - termo
    else:
        soma = soma + termo

print("Soma =", soma)