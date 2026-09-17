voltas = float(input("Digite o número de voltas: "))
extensao = float(input("Digite a extensão do circuito em metros: "))
tempo = float(input("Digite o tempo em minutos: "))

distancia = (voltas * extensao) / 1000
horas = tempo / 60

velocidade = distancia / horas

print("Velocidade média:", velocidade, "km/h")