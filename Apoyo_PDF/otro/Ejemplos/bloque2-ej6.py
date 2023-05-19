# 1. Solicitamos el número de segundos al usuario
total_segundos = int(input('Introduce el número de segundos > '))

# 2. Total de horas.
# Se tiene en cuenta solo la parte entera. El resto de la
# división son los segundos restantes.
horas = total_segundos // 3600
segundos = total_segundos % 3600

# 3. Total de minutos.
# Se tiene en cuenta solo la parte entera de los segundos
# restantes.
minutos = segundos // 60

# 4. Segundos restantes
segundos = segundos % 60

# 5. Mostramos el resultado por pantalla
print(f'{horas}:{minutos}:{segundos}')
