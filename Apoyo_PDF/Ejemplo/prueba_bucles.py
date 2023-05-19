#1
for i in [1,2,3]:
	print("hola")
#2
for i in ["primavera","verano","otoño","invierno"]:
	print("estamos en la estacion de: {}" .format(i))

#3

for i in [1,2,3]:
	print("hola", end =" ") #este argumento hará todo en una línea

#4
for i in "peypa0512@hotmail.com":
	print("hola", end="  ") # al recorrer todo el string 
							# habra tantos "hola" como caracteres haya

#5
"""email = False
for i in "peypa0512@hotmail.com":
	if(i == "@"):
		email = True

if email == True:

	print("El email es correcto")
else:

	print("el email no es correcto")"""

#6
"""email = False

miEmail=input("Introduce tu dirección de Email:   ")
print(miEmail)
for i in miEmail:

	if(i=="@"):
		email = True
		print("FIN")
if email :

	print("El email es correcto")
else:

	print("el email no es correcto")

#
contador=0

miEmail = input("Introduce tu dirección de Email:   ")

for i in miEmail:

	if(i == "@" or i == "."):
		
		contador=contador+1

if (contador == 2) :

	print("El email es correcto")
else:

	print("el email no es correcto")	"""
for i in range(5):
	print(i)

