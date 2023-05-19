"""
Este código es solo un ejemplo de cómo se puede resolver
el ejercicio.
En programación es frecuente que un problema se pueda
resolver de diferentes maneras.
"""

expresion = input('Introduce una expresión (Ej: 1 + 3 - 2 + 9) > ')

if (expresion.startswith('+ ') or expresion.startswith('- ') or
        expresion.endswith('+') or expresion.endswith('-') or
        expresion.endswith(' ')):
    # Comprobamos si la expresión no comienza o no termina
    # con un número. En ese caso, mostramos un mensaje de error.
    print('Expresión no válida')
else:
    resultado = 0  # Variable que acumula el resultado
    elementos = expresion.split()  # Lista que contiene los operandos y operadores
    op = None  # Último operador que se leyó
    for elem in elementos:
        if elem == '+':
            op = '+'
        elif elem == '-':
            op = '-'
        else:
            num = int(elem)
            if op is None:
                resultado = num
            elif op == '+':
                resultado += num
            else:
                resultado -= num
    print(resultado)
