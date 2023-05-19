# 1. Solicitamos el número al usuario.
# NOTA: Recuerda que hay que convertir la entrada
# por teclado a entero.
num = int(input('Introduce un número > '))

# 2. Comprobamos si el número es par y mayor que 100
par_mayor100 = (num % 2 == 0) and (num > 100)

# 3. Mostramos el resultado por pantalla
print(f'¿El número {num} es par y mayor que 100?', par_mayor100)
