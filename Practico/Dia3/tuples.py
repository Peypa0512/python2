
mi_tuple =(1,2,3,4,5)
print(type(mi_tuple))

mi_tuple2 =1,2,3,4
print(type(mi_tuple))

t=(1,'hola',1,2,[10,20,'a'])
print(type(t))

# para imprimir
print(t[1])
print(t[-1])

# no se puede agregar ni modificar
#t[5]=3
#t[0]=5
#print(t)

#puedo guardarlo en una lista

t= list(t)
print(t)
print(type(t))

t = tuple(t)
print(t)
print(type(t))

#podemos hacer lo siguiente
m= 1,2,3
x,y,z = m
print(x,y,z)
# esto se puede hacer porque al tener la misma cantidad de valores que de variables se asignaron en
#un sencillo proceso

m= (1,2,3,2,3,6,3)
print(len(m))
print(m.count(3))
print(m.index(2))
