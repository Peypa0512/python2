#1
for i in range(5):
	print(i)

#2
for i in range(5):
	print(f"el valor de la variable {i}") #adjuntas un terxto con la variable
										#unimos texto con variables
#3
for i in range(5,30,3): #cuenta desde el 5 al 30 de 3 en 3
	print(f"el valor de la variable {i}") #adjuntas un terxto con la variable
										#unimos texto con variables
#4
"""valido=False

email=input("introduce tu email: ")

for i in range(len(email)):
	if (email[i] == '@'):

		valido == True
if email:
	print("email correcto")
else:
	print("email incorrecto") """

#5
edad=int(input("Introduce tu edad: "))

while edad<5 or edad>100:
  print("Tu edad es inexacta")
  edad=int(input("Introduce tu edad: "))

print("gracias por tu edad, puedes pasar")
print("Tu edad es: " + str(edad))