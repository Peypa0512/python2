# 1. Solicitamos los números al usuario
n1 = int(input('Introduce el primer número > '))
n2 = int(input('Introduce el segundo número > '))
n3 = int(input('Introduce el tercer número > '))

# 2. Los números fueron introducidos en orden
# ascendente si n1 < n2 < n3
print(f'¿En orden ascendente? -> {n1 < n2 < n3}')
