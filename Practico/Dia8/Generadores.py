#hacemos una funcion para que nos devuelva el nº 4

def mi_funcion():
    return 4 # ya nos da el resultado


def mi_generador():
    yield 4 #hasta que no se le haga la llamada no se genera

print(mi_funcion())
print(mi_generador())

#para imprimir mi_generador()

g = mi_generador()
print(next(g))# con esto nos dará el número que se ha generado y si vuelvo a hacer next sacaría el siguiente



def mi_funciones():
    lista =[]

    for x in range(1,5):
        lista.append(x*10)
    return lista

def mis_generadores():

    for x in range(1,5):
        yield x*10

print(mi_funciones())
print(mis_generadores())

g = mis_generadores()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


def otro_generador():

    # return en el momento que ve el primero se para la función y sale, yield no

    x = 1
    yield x

    x +=1
    yield x

    x +=1
    yield x

g = otro_generador()
print(next(g))
print(next(g))
print(next(g))







