if len(lista) < 2:
    print('No se puede encontrar el segundo mayor')
else:
    maximo = max(lista[0], lista[1])
    segundomax = min(lista[0], lista[1])
    n = len(lista)
    for i in range(2, n):
        if lista[i] > maximo:
            segundomax = maximo
            maximo = lista[i]
        elif (lista[i] > segundomax) and (maximo != lista[i]):
            segundomax = lista[i]
    print('El segundo mayor es:', segundomax)
