import numeros
from os import system


def preguntar():
    while True:
        system('cls')
        print("¡¡BIENVENIDO A LA FARMACIA LA HERIDA!!!")
        print('''
            *. Para pedir turno para el departamento de Perfumeria pulse 'P'
            *. Para pedir turno para el departamento de Farmacia pulse 'F'
            *. Para pedir turno para el departamento de Cosmetida pulse 'C'
           
        ''')
        try:
            opcion = input('Por favor elija una opción > ').lower()
            ['p','f','c'].index(opcion)

        except ValueError:
            print("Esa opción en incorrecta")

        else:
            print('Enseguida será atendido, espere un momento......')
            break

    numeros.decorar_ticket(opcion)


def inicio():

    while True:
        preguntar()
        try:
            mas_turno = input("¿Desea algún turno más? [S] [N]: ").lower()
            ["s","n"].index(mas_turno)
        except ValueError:
            print("Esa no es una Opción Valida")

        else:
            if mas_turno =='n':
                print("Gracias por su visita")
                break


inicio()