# Exercício 7

# Entrada de dados
dia_hora = int(input("Horas: "))
dia_minuto = int(input("Minutos: "))
dia_segundos = int(input("Segundos: "))

# Calculo de minutos
total_minutos = (dia_hora * 60) + dia_minuto + (dia_segundos / 60)

# Calculo de segundos
total_segundos = (dia_hora * 3600) + (dia_minuto * 60) + dia_segundos

# Mostrar os valores em minutos e segundos
print("Total de minutos transcorridos: " + str(total_minutos) + " minutos")
print("Total de segundos transcorridos: " + str(total_segundos) + " segundos")
