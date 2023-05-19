# 1. Solicitamos las horas al usuario
horas = int(input('Introduce el número de horas > '))

# 2. Calculamos los segundos y los mostramos por pantalla
print(f'{horas} hora(s) son {horas * 3600} segundos')

# ------ Otra alternativa

horas = int(input('Introduce el número de horas > '))
segundos = horas * 60 * 60
print(horas, 'hora(s) son', segundos, 'segundos')
