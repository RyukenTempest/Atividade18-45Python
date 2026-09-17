hora_inicio = int(input("Digite a hora de início: "))
minuto_inicio = int(input("Digite o minuto de início: "))

hora_final = int(input("Digite a hora final: "))
minuto_final = int(input("Digite o minuto final: "))

inicio = hora_inicio * 60 + minuto_inicio
final = hora_final * 60 + minuto_final

if final <= inicio:
    final = final + 24 * 60

duracao = final - inicio

horas = duracao // 60
minutos = duracao % 60

print("Duração:", horas, "hora(s) e", minutos, "minuto(s)")