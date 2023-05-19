# 1. Solicitamos el número al usuario.
# NOTA: Recuerda que hay que convertir la entrada
# por teclado a entero.

num = int(input('Introduce un número > '))

# 2. Calculamos el número siguiente y lo
# mostramos por pantalla
num = num + 1
print('Siguiente: ', num)

# ---- Una alternativa al código anterior

num = int(input('Introduce un número > '))
num += 1
print('Siguiente: ', num)
