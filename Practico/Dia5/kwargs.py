def suma(**kwargs):
    print(type(kwargs))


suma(x=3,y=5,z=2)


def suma(**kwargs):
    total =0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3, y=5, z=2))

#mezclar funciones

def prueba(num1, num2, *args, **kwargs):
#ese es el orden que debe de llevar
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')
    for arg in args:
        print(f'arg = {arg}')


    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


# los asteriscos * valen tambien para desesmpacar tuplas, diccionarios

args=[100,200,300,400]
kwargs ={'x':'uno','y':'dos','z':'tres'}

prueba(15,50, *args, **kwargs)



def cantidad_atributos(**kwargs):
    total=0
    for clave,valor in kwargs.items():
        total += valor
    return total


print(cantidad_atributos(a=2,y=5,z=8))

def cantidad_atributos(**kwargs):
    total=0
    for valor in kwargs.values():
       total += valor


    print(total)

cantidad_atributos(x=2,y=5,z=8)


def lista_atributos(**listar):
    list=[]

    for clave in listar.items():
        list.append(clave)

    return list
clave ={'uno':'1','dos':'2','tres':'3'}
print(lista_atributos(**clave))


def describir_persona(*args,**kwargs):
    for elemento in args:
        print(f' Nombre : {elemento}')
        for clave,valor in kwargs.items():
            print(f'{clave} : {valor}')


lista =['Pedro','Alejandro', 'Juanito']
dic ={'color pelo':'rubio','ojos':'marron','dientes':'saltones'}
describir_persona(*lista,**dic)