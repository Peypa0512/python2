# 1. Solicitamos los números al usuario.
# NOTA: Recuerda que hay que convertir la entrada
# por teclado a entero.

print('Operaciones aritméticas sobre números\n')
num1 = int(input('Introduce un número > '))
num2 = int(input('Introduce otro número > '))

# num1 y num2 referencian a dos números.
# Ahora podemos realizar operaciones aritméticas
# con dichas variables (nombres).

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1 / num2

# Ejemplo de print
print('num1 + num2 = ', suma)
# Ejemplo de print con concatenación
print('num1 - num2 = ' + str(resta))
# Ejemplo de print con formateo de cadenas
print('num1 * num2 = {}'.format(producto))
# Ejemplo de print con f-Strings
print(f'num1/num2 = {division}')
