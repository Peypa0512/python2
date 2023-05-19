# 1. Solicitamos las medidas del triángulo al usuario
base = float(input('Introduce la longitud de la base > '))
altura = float(input('Introduce la altura > '))

# 2. Calculamos el área
area = (base * altura) / 2

# 3. Mostramos la solución por pantalla
print(f'Área = {area:.2f}')
