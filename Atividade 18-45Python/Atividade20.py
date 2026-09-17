import math

a = float(input("Digite A aqui: "))
b = float(input("Digite B aqui: "))
c = float(input("Digite C aqui: "))

if a == 0:
    print("Não é uma equação de segundo grau, pois A = 0")
else:
    delta = b**2 - 4 * a * c

    if delta < 0:
        print("Não existem raízes reais, pois Delta é menor que zero.")
    elif delta == 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        print("Raiz:", x1)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Raízes:", x1, x2)