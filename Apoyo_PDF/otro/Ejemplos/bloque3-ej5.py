i = 1
pares = 0
impares = 0
while i <= 10:
    numero = int(input('Introduce un número > '))
    if numero % 2 == 0 and numero > 20:
        pares += 1
    if numero % 2 == 1 and numero > 50:
        impares += 1
    i += 1
print('Números pares mayores que 20', pares)
print('Números impares mayores que 50', impares)
