
'''
En este modulo haremos los generadores de los distintos turnos de la farmacia en 3 areas
    - Perfumeria
    - Farmacia
    - Cosmetica
'''


def perfumeria():

    for n in range(1,10000):
        yield f'P{n}'


def farmacia():
    f = 0

    for n in range(1,10000):

        yield f'F{n}'



def cosmetica():
    for n in range(1,10000):
       yield f'C{n}'

f = farmacia()
c = cosmetica()
p = perfumeria()




def decorar_ticket(palabra):

    '''
        funcion decoradora
    '''
    print('\n'+'*'* 33)
    print("Su turno es :")
    if palabra =='p':
        print(next(p))
    elif palabra =='f':
        print(next(f))
    else:
        print(next(c))
    print("En breves momentos será atendido")
    print('\n'+'*'* 33)





