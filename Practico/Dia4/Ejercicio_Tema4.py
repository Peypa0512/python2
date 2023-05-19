from random import randint

nombre =input("Hola, ¿me puedes decir tu nombre? ")
print("Vamos a jugar a adivinar un número del 1 al 100")
numAleatorio = randint(1,100)
contador =8
n=1
while(contador>0):
    vez = int(input("Por favor introduce un número del 1 al 100> "))
    if vez >0 and vez<100:

        if vez == numAleatorio:
            print(f"¡¡¡ENHORABUENA!!!, acabas de adivinar el número {numAleatorio} en {n} intentos")
            break
        elif vez > numAleatorio:
            print("El número que has introducido es mayor que el número elegido")
        else:
            print("el número que has introducido es menor que el número elegido")
        n +=1
        contador -=1
    else:
        print("El numero introducido es menor que 0 y mayor que 100")
        continue

else:
    print(f"Has sobrepaso el limite de intentos, el numero elegido era {numAleatorio}")