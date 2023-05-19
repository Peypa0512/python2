import timeit


'''def prueba_for(numero):
    lista=[]
    for num in range(1,numero +1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador =1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''


#para saber cual es más eficiente tanto de recursos como tiempos

# Caso 1:
# import time
# comparamos tiempos
'''
inicio = time.time()
prueba_for(1000000)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(1000000)
final = time.time()
print(final - inicio)
'''

declaracion = '''
prueba_for(10)
            '''

mi_setup= '''
def prueba_for(numero):
    lista=[]
    for num in range(1,numero +1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion,mi_setup,number =1000000)
print(duracion)

declaracion2 = '''
prueba_while(10)
            '''

mi_setup2= '''
def prueba_while(numero):
    lista = []
    contador =1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion2 = timeit.timeit(declaracion2,mi_setup2,number =1000000)
print(duracion2)