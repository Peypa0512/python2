i = 1
mayor = None
menor = None
while i <= 5:
    numero = int(input('Introduce un número > '))
    if mayor is None or numero > mayor:
        mayor = numero
    if menor is None or numero < menor:
        menor = numero
    i += 1
print('El número mayor es el', mayor)
print('El número menor es el', menor)
