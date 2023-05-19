archivo = open('prueba1.txt','w')
archivo.write('''Hola 
mundo,
aqui estoy yo
''')


archivo.writelines(['hola','mundo','aqui','estoy'])

lista=['hola','mundo','aqui','estoy']

#le pasamos un for y le damos el formato que deseemos

for p in lista:
    archivo.writelines( p + '\n')

archivo.close()


mi_archivo = open('prueba.txt','a')

nueva_linea = mi_archivo.write('\nBienvenido')

mi_archivo.close()

archivo = open('mi_archivo.txt','w')
linea = archivo.write('Nuevo texto')
archivo.close()

archivo1 = open('mi_archivo.txt','r')
leer = archivo1.readline()
#print(leer)
archivo1.close()

archivo2 = open('mi_archivo.txt','a')
escribe = archivo2.write('\nNuevo inicio de sesión')
archivo2.close()

archivo3 = open('mi_archivo.txt','r')
leido = archivo3.read()
print(leido)
archivo3.close()

registro = open('registro.txt','w')
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for elemento in registro_ultima_sesion:
    registro.writelines(elemento+"\t")
registro.close()

registro1 = open('registro.txt','r')
leido = registro1.read()
print(leido)
registro1.close()