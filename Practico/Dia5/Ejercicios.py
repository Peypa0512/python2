# Ejercicio 1

'''def devolver_distintos(**kwargs):
    suma =0
    lista=[]

    for valor in kwargs.values():
        suma += valor
        lista.append(valor)
    if suma > 15:
        print(max(lista))
    elif suma < 10:
        print(min(lista))
    else :
        lista.sort()
        print(lista[1])

devolver_distintos(a=4,b=7,c=2)



#Ejercicio 2

def deletreo (palabra):
    d=0
    mi_set = set()
    listado=[]
    for c in palabra:
        mi_set.add(c)

    lista= list(mi_set)
    lista.sort()
    print(lista)

deletreo("paraguas")


#Ejercicio 3

def cero_vecinos(*args):

    contador = 0
    for n in args:
        if contador+1 == len(args):
            return False
        elif args[contador]==0 and args[contador+1]==0:
            return True
        else:
            contador = contador +1
    return False

print(cero_vecinos(1,2,3,0,4,50,5,7,8,0))

#Ejercicio 4

def primos(num1,num2):

    while num1 <= num2:
        x = 0
        contador = 1
        while contador <= num1:

            if num1 % contador == 0:
               x=x+1

            contador += 1
        if x == 2:
            print(num1)
        

        num1 +=1


num1 = int(input("Introduce un numero inicial: "))
num2 = int(input("Introduce un numero final: "))
primos(num1,num2)'''

# variante 2

def contar_primo(numero):
    primo = [2]
    iteracion = 3
    print(numero)

    if numero < 2:
        return 0

    while iteracion <= numero:

        # el rango que ponemos es desde 3 como minimo hasta iteracion y que avance de 2 en 2
        # hay que recordar que todos los numeros pares no son primos
        print('x')
        for n in range(3,iteracion,2):
            print('hola')
            # si el resto de iteracion es 0 no lo adjuntamos a la lista de primo
            if iteracion % n ==0:
                iteracion +=2
                break
            else:
                primo.append(iteracion)
                iteracion +=2
    print(primo)
    return len(primo)

print(contar_primo(19))
