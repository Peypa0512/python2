import random
from random import choice

fallo =[]
vidas=6
fallado=0
lista= {}
pintado =""
a =""
aj=""
x=0
resta =0


def palabra():
    #elegimos una palabra de la lista aleatoriamente
        elegido = random.choice(('palabra','viento','miercoles','amarillo','america'))


        return elegido

def introducirLetra(letra):
    #introducimos la letra y comprobamos que sea un caracter
    x = False
    caracter =""
    while x == False:
        if letra.isalpha():
            if len(letra) > 1:
                print("Por favor introduce solo un caracter")
                letra = input("Por favor introduce una letra: ")
            else:
                caracter = letra
                x = True
        if letra.isdigit():
            print("Solo se puede introducir letras, gracias!!")
            letra = input("Por favor introduce una letra: ")

    return caracter

def comprobarLetra(letra,palabra,vidas):


# comprobamos si la letra está en la palabra
    vida = vidas + 0
    suma =0
    cuenta = 0
    posicion = 0
    for elemento in elegido:

        if (letra in elemento):

            conteo = elegido[posicion]
            lista[posicion] = conteo
            cuenta=1
        posicion += 1

    if(cuenta ==0):
        vidas =  vida - 1
        fallo.append(letra)



    return lista


def pintarPalabra(letra,palabra,vidas):
    # comprobamos si está en la palabra y mostramos en pantalla si es así y la posicion que ocupa
    fallos = 0
    vida = vidas
    suma=0
    cuenta = 0
    guion =0
    al=""
    for n in elegido:
        guion += 1
    if guion < 7:
        a = '------'

    elif guion < 8:
        a = '-------'

    elif guion < 9:
        a = '--------'

    elif guion < 10:
        a = '---------'

    if len(elegido) == len(a):

        for elemento in lista:
            comprobar = lista.values()


            if letra in elegido:
                cuenta =1
                if cuenta ==1:
                    for k, v in lista.items():
                        a1 = list(a)
                        a1[k] = (v)
                        a = "".join(a1)
                        aj = a

        if cuenta == 0:

            vidas = vidas - 1
            fallos +=1
            print(al)

    print(a)
    print(f'Aún te quedan {vidas}')
    print(f'Letras Falladas : {fallo}')

    print('¿Deseas resolver?')
    respuesta = input ("¿quieres resolver? 1.- SI 2.- No > ")

    while respuesta not in '12':
        print("Debes elegir 1.- SI o 2.- No")
        respuesta = input("¿quieres resolver? 1.- SI 2.- No > ")
    if respuesta == '1':
        print(a)
        intento = input("¿Que palabra he elegido? : ")
        if intento == elegido:
            print("¡ENHORABUENA! has adivinado la palabra")
            print(f'Te han sobrado {vidas} vidas')
            print(f'Las letras que has fallado son {fallo}')
            exit()
        else:
            print("Esa no es la palabra")
            vidas = vidas - 1
            print(f"Acabas de perder una vida te quedan {vidas} vidas")
    else:
        print(a)
    return a



elegido = palabra()
guion=0
intento =""

for n in elegido:
    guion += 1
if guion < 7:
    a = '------'
    print (a)
elif guion < 8:
    a = '-------'
    print(a)
elif guion < 9:
    a= '--------'
    print (a)
elif guion < 10:
    a = '---------'
    print(a)


print("Bienvenido al juego del ahorcado")
while x==0:

    letra = input("Por favor introduce solo un caracter ")
    recibo = introducirLetra(letra)
    comprobado = comprobarLetra(recibo,elegido,vidas)
    pintar =pintarPalabra(letra,comprobado,vidas)
    print(pintar)

    enviado_otra_vez = introducirLetra(letra)
    eliminar =0
    if len(lista)==0:
        eliminar +=1
        resta = resta + eliminar
        vidas = vidas - resta
        print(aj)
        print(f"Te quedan una {vidas} vidas")
        print(pintar)

    if vidas ==0:
            print(f'Fin de Juego..... La palabra elegida era {elegido}')
            x=1


