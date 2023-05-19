# 1. Solicitamos la base y la altura al usuario.
# NOTA: Recuerda que hay que convertir la entrada
# por teclado a float.

base = float(input('Introduce la longitud de la base > '))
altura = float(input('Introduce la altura > '))

# 2. Calculamos el perímetro y mostramos el resultado
# por pantalla

perimetro = 2 * (base + altura)
print(f'Perímetro = {perimetro:.3f}')

# ---- Una alternativa al código anterior

perimetro = 2 * base + 2 * altura
print(f'Perímetro = {perimetro:.3f}')
