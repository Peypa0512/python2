"""Hay que crear un programa en el cual el usuario introduzca un texto.
   Una vez introducido le tiene que pedir 3 caracteres.

   COSAS A REALIZAR
   ----------------
   1.- Tiene que decir por pantalla :
    - de cada caracter cuantas veces se repiten.

   2.- Tiene que contar cuantas palabras hay en el texto y que lo refleje en pantalla.

   3.- Tiene que mostrar en pantalla cual es el primer y último caracter del texto introducido.

   4.- Tiene que verse como sería el texto al reves.

   5.- Que muestre por pantalla si contiene la palabra 'Python' aparece en el texto

"""



letra1=0
letra2=0
letra3=0
texto =input("introduce un texto, por favor > ")
lista=[]
x=0
while (x !=3):
    letra = input("introduce una letra, por favor > ").lower()
    lista.append(letra)
    x=x+1
#1
texto =texto.lower()

print("\n")
print("CONTADOR DE LETRAS")
print("------------------")

letra1=texto.count(lista[0])
print(f'Hay letras {lista[0]}: {letra1}')
letra2=texto.count(lista[1])
print(f'Hay letras {lista[1]}: {letra2}')
letra3=texto.count(lista[2])
print(f'Hay letras {lista[2]}: {letra3}')

#2
print("\n")
print("CONTADOR DE PALABRAS")
print("--------------------")

lista =texto.split(" ")
print('El texto tiene',len(lista),'palabras')

#3
print("\n")
print("PRIMER Y ULTIMO CARACTER")
print("------------------------")

print(f'la primera lentra empieza por {texto[0]} y la última letra es {texto[-1]}')

#4
print("\n")
print("TEXTO AL REVES")
print("--------------")

#String al reves
texto2 = texto[::-1]
print("Tu texto al reves sería así:")
print(texto2)

#lista al reves
lista.reverse()
print("Tu texto al reves por palabras sería así:")
texto1 = " ".join(lista)
print(texto1)

#5
print("\n")
print("¿ ESTA 'PYTHON' DENTRO DEL TEXTO?")
print("---------------------------------")

comprobar = 'python'  in texto
comprobado={True:"si",False:"no"}
print(f"¿La palabra Pyhton esta en el texto?---> la Respuesta es {comprobado[comprobar]}")