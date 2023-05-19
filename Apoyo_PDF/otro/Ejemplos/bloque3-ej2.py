num1 = int(input('Introduzca un número > '))
num2 = int(input('Introduzca otro número > '))

while True:
    print('Calculadora básica. ¿Qué operación desea realizar?')
    print('[1] Sumar')
    print('[2] Restar')
    print('[3] Multiplicar')
    print('[4] Dividir')
    print('[0] Salir')
    operacion = int(input('Operación > '))
    if operacion == 0:
        print('Saliendo...')
        break
    elif operacion == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacion == 2:
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operacion == 3:
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operacion == 4:
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print('Operación desconocida')
