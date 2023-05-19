from collections import Counter
from collections import defaultdict
from collections import namedtuple

numeros =[8,9,6,5,4,4,5,5,5,8,7,4,4]

print(Counter(numeros))

print(Counter('mississipi'))

frase = 'al pan pan y al vivo vino'
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,2,2,2,2,2,3,3,3,3])
print(serie.most_common(2))
print(list(serie))


# difaultdic

mi_dic = defaultdict(lambda:'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['dos'])

print(mi_dic)


# namedtuple

Persona = namedtuple('Persona',['nombre', 'altura', 'peso'])
ariel = Persona('Ariel',176,79)

print(ariel.altura)
print(ariel.peso)

#si quiero acceder por indice

print(ariel[2])


# EJERCICIO 3

from collections import deque

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

lista_ciudades.appendleft("Alcorcón")

print(lista_ciudades)

