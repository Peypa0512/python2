# 1. Solicitamos el número de animales
# de cada clase al usuario.
# NOTA: Recuerda que hay que convertir la entrada
# por teclado a entero.

gallinas = int(input('Introduce el número de gallinas > '))
cerdos = int(input('Introduce el número de cerdos > '))
vacas = int(input('Introduce el número de vacas > '))

# 2. Calculamos el número de patas
patas = 2 * gallinas + 4 * (cerdos + vacas)

# 3. Mostramos el resultado por pantalla
print('El número total de patas es', patas)

# ------ Otra alternativa

patas_gallinas = 2 * gallinas
patas_cerdos = 4 * cerdos
patas_vacas = 4 * vacas
patas_totales = patas_gallinas + patas_cerdos + patas_vacas
print('El número total de patas es', patas_totales)
