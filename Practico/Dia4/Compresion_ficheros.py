palabra ='PYTHON'

lista =[]
for letra in palabra:
    lista.append(letra)
print(lista)
#ocupa unas cuantas lineas de codigo
#podemos hacer lo siguiente
# le decimos a lista que cada elemento va a ser una letra de cada letra que haya en palabra
lista2 = [letra for letra in palabra]

print(lista2)

# también se puede hacer directamente
lista3 = [letra for letra in 'python']
print(lista3)

#también se puede hacer con numeros

lista4=[n for n in range(0,21,2)]
print(lista4)

#podemos modificar estos numeros
lista5=[n/2 for n in range(0,21,2)]
print(lista5)

#puedo incorporar también un if
lista6=[n for n in range(0,21,2) if n*2 >10 ]
print(lista6)

# y si quiero poner un else hay que ponerlo detras del primer 'n'
lista7=[n if n*2 >10 else 'no' for n in range(0,21,2) ]
print(lista7)

#supongamos que tenemos una lista con medidas en pies

pies =[10,20,30,40,50]
metros =[p *3.281 for p in pies]
print(metros)
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares=[n for n in valores if n%2==0]
print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
#C = (°F - 32) * (5/9)

grados_celsius= [round((n-32)*(5/9),2) for n in temperatura_fahrenheit]
print(grados_celsius)