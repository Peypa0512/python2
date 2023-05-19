from random import shuffle
from random import randint
"""
-Vamos a crear una lista inicial
-una funcion que mezcle los palitos
-pedir un intento de elección del usuario
- comprobar si has ganado o perdido

"""
# lista inicial
palitos=['-','--','---','----']

#funcion para mezclar
#necesitaremos el meto shuffle para mezclar la lista
def mezclar(lista):
    shuffle(lista)
    return lista
#para comprobar
#print(mezclar(palitos))

#función  para probar suerte
def probar_suerte():
    intento =''
    #tiene que ser una peticion del 1 al 4
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4> ")
    return int(intento)
#comprobamos
#print(probar_suerte())

#comprobramos si ha acertado o no
def chequear_intento(lista,intento):
    if lista[intento -1] == '-':
        print('Has perdido')
    else:
        print('Has ganado')
    print(f'Te ha tocado {lista[intento -1]}')

#vamos a ver como poder conectar todas las funciones
palitos_mezclados=(mezclar(palitos))
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)


#EJERCICIO1
'''
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

    La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

    Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente 
    los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada 
(es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- 
un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

    "La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

    "La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:

    "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

'''

def lanzar_dados():

    resultado1 = randint(1,6)
    resultado2 = randint(1,6)
    tupla =[(resultado1,resultado2)]
    return tupla

def evaluar_jugada(num1,num2):


        suma_dados = num1+num2

        if(suma_dados<= 6):
            return print(f"La suma de los dados es {suma_dados}. Lamentable")
        if(suma_dados > 6 and suma_dados < 10):
            return print(f"La suma de los dados es {suma_dados}. Tienes buena suerte")
        if (suma_dados >= 10):
            return print(f"La suma de los dados es {suma_dados}. Parece una jugada ganadora")

num1=0
num2=0
for a,b in lanzar_dados():
    num1 = a

    num2 = b



resultado= evaluar_jugada(num1,num2)