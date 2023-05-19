mi_lista =['a','b','c']
print(type(mi_lista))
resultado = len(mi_lista)
print(resultado)
resultado = mi_lista[0]
print (resultado)
resultado = mi_lista[0:2]
print (resultado)
resultado = mi_lista[0:]
print (resultado)
mi_lista2=['d','e','f']
resultado =mi_lista+mi_lista2
print(resultado)
mi_lista3= mi_lista+mi_lista2
print(mi_lista3)

mi_lista3[0]='alfa'
print(mi_lista3)
#agregar elementos
mi_lista3.append('g')
print(mi_lista3)
#eliminar, si no se especifica dentro del parentesis borrará el último
mi_lista3.pop()
print(mi_lista3)
eliminar = mi_lista.pop(0)
print(mi_lista3)
print(eliminar)

mi_lista4= ['g','b','z','m','w']
#ordena los elementos
mi_lista4.sort()
print(mi_lista4)

#no se puede hacer esto
nueva_lista = mi_lista4.sort()
print(type(nueva_lista))
#se debería hacer así
nueva_lista2 = mi_lista4
print(nueva_lista2)

#para hacer al reves
nueva_lista2.reverse()
print(nueva_lista2)