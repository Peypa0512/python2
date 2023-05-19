'''

Ejercicio de prueba de pylint
'''


def sumar(numero1, numero2):
    '''
    definimos los parametros siguientes:
    :param numero1:
    :param numero2:
    :print numero1 + numero2
    '''

    resultado = numero1+numero2
    return resultado


# primer numero
num1 = int(input("Dime un numero: "))
# segundo numero
num2 = int(input("Dime otro numero: "))

valor = sumar(num1, num2)
print(f"El resultado de la suma de número 1 = {num1} y número 2 = {num2} es {valor}")

