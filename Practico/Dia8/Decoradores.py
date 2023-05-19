def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())


print('Hola')
#mayusculas('que tal?')
minusculas('YO MUY BIEN')
print('adios')


# la solución de este problema es...

# hay que pensar que todo es un objeto, por lo que la función es también un objeto, se puede asignar una función a una
#variable

mi_funcion = mayusculas
mi_funcion('python')

# se puede pasar también como argumento de una función

def una_funcion (funcion):
    return funcion

una_funcion(mayusculas('probando'))


#tambien se puede definir funciones dentro de otras funciones

def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula

operacion = cambiar_letras("may")

operacion('palabra')


#queremos construir un decorador para nuestras funciones que nos permita agregar o no los saludos dependiendo de cuando
#queramos

def decorar_saludo(funcion):

    def otra_funcion(palabra):

        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion
# con esta función lo que hace es imprimir texto a mayusculas

@decorar_saludo  # esto hace cuando se vaya a ejecutar envuelvela la función entre la funcion decorar_saludo()

def mayuscula(texto):
    print(texto.upper())


@decorar_saludo
def minusculas(texto):
    print(texto.lower())

minusculas('Python')
#mayuscula('amigos')

# para usar la funcion de may y min sin el decorador

mayuscula_decorada = decorar_saludo(mayuscula)

mayuscula('fede') # puedo activar o no el decorador
mayuscula_decorada('fede') # así activo el decorador





