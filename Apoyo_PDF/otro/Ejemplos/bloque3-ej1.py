edad = int(input('¿Cuál es tu edad? > '))

# Comprueba si el usuario es mayor de edad
# y guarda este valor en una variable.
# Dicho valor se puede utilizar posteriormente
# en otro punto del programa.
mayor_edad = edad >= 18

# Muestra si el usuario es mayor de edad o no
if mayor_edad:
    print('Eres mayor de edad')
else:
    print('No eres mayor de edad')

# ------ Otra alternativa

# Aquí simplemente se comprueba si el usuario
# es mayor de edad.
if edad >= 18:
    print('Eres mayor de edad')
else:
    print('No eres mayor de edad')

# ------ NO HAGAS ESTO
# No es necesario asignar a una variable booleana
# los valores True/False directamente en función de
# la condición.
# La expresión en sí ya devuelve un valor booleano.
# Como ves, en los ejemplos anteriores el código
# es más claro y más simple.
if edad >= 18:
    mayor_edad = True
else:
    mayor_edad = False
    
if mayor_edad:
    print('Eres mayor de edad')
else:
    print('No eres mayor de edad')
