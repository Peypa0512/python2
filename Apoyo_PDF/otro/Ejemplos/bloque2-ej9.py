# 1. Solicitamos el número al usuario.
# NOTA: Recuerda que hay que convertir la entrada
# por teclado a entero.

num = int(input('Introduce un número entero > '))

# 2. Calculamos si el número es divisible por 7
es_divisible = num % 7 == 0

# 3. Mostramos el resultado por pantalla
print(f'¿El número {num} es divisible por 7? {es_divisible}')

# ------ Otra alternativa

es_divisible = not num % 7
print(f'¿El número {num} es divisible por 7? {es_divisible}')
