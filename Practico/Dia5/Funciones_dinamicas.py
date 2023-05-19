'''
def chequear_3_cifras(numero):
    return numero in range(100,1000)# al hacer in range el resultado va a ser booleano

suma = 586+402
resultado = chequear_3_cifras(suma)
print(resultado)

#verificamos si tiene 3 cifras de una lista
def chequear_3_cifras2(lista):
    for n in lista:
        if n in range(100,1000):
            return True #aparte de guardar en la variable si se da que es True se acaba la funcion
        else:
            pass
            #return False-->al ser una lista y el tener el tercer elemento un true si ponemos un False en primer lugar nos sacará del programa
resultado = chequear_3_cifras([55,99,500])
print (resultado)
print(type(resultado))

# que nos de los valores que cumplen la condicion
def chequear_3_cifras3(lista):
    lista_3_cifras=[]
    for n in lista:
        if n in range(100,1000):
            return True #aparte de guardar en la variable si se da que es True se acaba la funcion
            lista_3_cifras.append[n]
        else:
            pass
    return lista_3_cifras

'''
def todos_positivos(lista):
    numeros =[]
    for n in lista:
        if n in range(0,1000):
          numeros.append(n)
        elif len(numeros) != 0:
            return True
        else:
            return False


def todos_positivos(lista):

    for n in lista:
        if n > 0:

           continue
        else:

            return False
    return True


lista_numeros = todos_positivos([10, -6, 15, -9])
print(lista_numeros)



'''def suma_menos(lista):
    contador=0
    for n in lista:

        if n in range(1,1000):
            contador= contador+n

    print(contador)


lista_numeros=suma_menos([1,2,3,500])
#print(lista_numeros)'''


def suma_menores(lista):
    print(lista)
    suma = 0
    for n in lista:
        print (n)
        suma = suma + n

    print(suma)


suma_menores=([n for n in [1,50,500,750] if n in range(1,1000)])
print(suma_menores.index(1))

#print(lista_numeros)

def cantidad_pares(lista):
    pares = 0
    cuenta = 0
    for n in lista:
        if (n % 2 == 0):
            pares += 1
            cuenta = cuenta + n
        else:
            continue
    print(pares)
    print(cuenta)


lista_numeros = [1, 50, 502, 755, 34]
cantidad_pares(lista_numeros)