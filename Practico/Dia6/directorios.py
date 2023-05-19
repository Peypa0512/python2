import os
from usar_pathlib import Path

ruta= os.getcwd()

ruta1 = os.chdir('C:\\Users\\pedro\\Documents\\PYTHON\\curso\\dia6')
archivo = open('Prueba.txt')
print(archivo.read( ))
archivo.close()

#crear = os.makedirs('C:\\Users\\pedro\\Documents\\PYTHON\\curso\\dia6\\otra')

#basename

ruta2 = 'C:\\Users\\pedro\\Documents\\PYTHON\\curso\\dia6\\prueba.txt'

elemento = os.path.basename(ruta2)
print(elemento)

#dirname

ruta3 = 'C:\\Users\\pedro\\Documents\\PYTHON\\curso\\dia6\Prueba.txt'

elemento = os.path.dirname(ruta2)
print(elemento)

# si queremos los elementos por separado
ruta24 = 'C:\\Users\\pedro\\Documents\\PYTHON\\curso\\dia6\Prueba.txt'

elemento = os.path.split(ruta2)
print(elemento)

#os.rmdir('C:\\Users\\pedro\\Documents\\PYTHON\\curso\\dia6\\otra')


#importamos la libreria from pathlib import Path

carpeta = Path('C:/Users/pedro/Documents/PYTHON/curso/dia6')
archivo = carpeta / 'Prueba.txt'

mi_archivo5 = open(archivo)
print(mi_archivo5.read())