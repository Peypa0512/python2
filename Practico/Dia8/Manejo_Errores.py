def suma():
    print(10+10)
    print('Gracias por sumar')

suma()

def suman():
    n1 = int(input("Numero 1 > "))
    n2 = int(input("Numero 2 > "))
    print(n1+n2)


try:
    #codigo a probar
    suman()
except TypeError:
    #codigo por si hay un error
    print("No se puede intentar dos tipos de datos")
except ValueError:
    print("debe ser un valor numerico")

else:
    #codigo a ejecutar si no hay un error
    print("Gracias por sumar...")
finally:
    #codigo que se va a ejecutar de todos modos
    print("Esto es todo")



def pedirNumero():
    while True:
        try:
            numero = int(input("dame un número: "))
        except:
            print("Ese no es un número")
        else:
            print(f'Ingresaste el número {numero}')
            break
    print('Gracias')

pedirNumero()