
mi_set =set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

mi_set2 =set((1,2,3,4,5,6))
print(type(mi_set2))
print(mi_set)

mi_set3 = {1,2,3,4,5,6,7}
print(type(mi_set3))
print(mi_set3)

#no tiene orden interno
#print(mi_set3[0])
#no se pueden modificar
#mi_set3[0]=5
#print(mi_set3)

#son elementos unicos
mi_set4 = {1,2,3,2,5,6,1}
print(type(mi_set4))
print(mi_set4)

#no puedo adjuntar listas
#mi_set5 = {1,2,3,4,5,6,[7,8,9]}
#print(type(mi_set5))
#print(mi_set5)

#pero si si puede un tuple, porque es inmutable como set
mi_set6 = {1,2,3,(4,5,6),7,2,5,8}
print(type(mi_set6))
print(mi_set6)

#pueden usar la funcion len
print(len(mi_set6))
#para ver si exite un elemento dentro
print(2 in mi_set6)

s1 ={1,2,3}
s2 ={3,4,5}
#para juntar sets
s3= s1.union(s2)
print(s3)

#agregar elementos

s1.add(6)
print(s1)

#eliminar elementos
s1.remove(2)
print(s1)
#descartamos
s1.discard(6)
print(s1)

#vaciar un elemento aleatorio
sorteo =s1.pop()
print(sorteo)

#limpiar el set
s1.clear()
print(s1)

