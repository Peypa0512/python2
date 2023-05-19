lista =['a','b','c']

for letra in lista:
    #print('Letra: '+letra)
    #podemos ver su indice
    numero_letra = lista.index(letra)+1
    print(f'La letra{numero_letra}: {letra}')



lista2=['Pablo','Laura','Fede','Julia','Luis']

for nombre in lista2:
    if nombre.startswith('L'):
        print(nombre)
    else:
        print('Nombre que no empieza por L')

numeros=[0,1,2,3,4,5]
mi_valor = 0;

for n in numeros:
    mi_valor= mi_valor+n
    print(mi_valor) # no es igual tener el print en for que fuera de él
print("\n")
print(mi_valor)

for i in 'python':
    print(i)

lista3=[[1,2],[3,4],[5,6]]
for a,b in lista3:
    print(a)
    print(b)


dic={1:'a',2:'b',3:'c'}

for a,b in dic.items(): #se pueden llamar a las claves con dic.keys(), valores dic.values()
    print(a,b)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for n in lista_numeros:
    if(n%2 ==0):
        suma_pares = suma_pares+n
    else:
         suma_impares = suma_impares+n

print(suma_pares)
print(suma_impares)