# las llaves no se pueden repetir, los valores si
diccionario={'c1':'valor 1','c2':'valor 2'}
print(type(diccionario))
print(diccionario)
# busqueda
resultado =diccionario['c1']
print(resultado)

cliente ={'nombre':'Juan','apellido':'Fuentes','peso':73.5,'altura':1.75}
buscar =cliente['apellido']
buscar1 =cliente['peso']
print (buscar)
print (buscar1)

dictado = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
# le pido la clave 2 y el resultado 1 de la lista
buscar = dictado['c2'][1]
print(buscar)
#lo mismo en caso de un diccionario
buscar = dictado['c3']['s2']
print(buscar)

dic={'c1':['a','b','c'],'c2':['d','e','f']}
# imprimimos el indice en mayúsculas
print(dic['c2'][1].upper())


dict={'a':1,'b':2}

#agregamos
dict['c']=3
print(dict)

#sobreescribir
dict['b']= 234
print(dict)

#imprimir las llaves
print(dict.keys())

#impimir los valores
print(dict.values())

#imprimir todo
print(dict.items())

mi_dic={'nombre':'miKaren','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}
print(mi_dic)