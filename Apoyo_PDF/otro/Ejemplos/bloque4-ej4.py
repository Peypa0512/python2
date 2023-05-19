numero = input('Introduce un número de tarjeta > ')
# Quitamos espacios si los hay
numero = numero.replace(' ', '')
oculto = numero[-4:].rjust(len(numero),'*')
print(oculto)
