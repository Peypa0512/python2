import os
import re
import math
import time
from pathlib import Path
import datetime

inicio = time.time()
ruta= 'C:\\Users\\Usuario\\Documents\\software\\Python\\Dia9\\proyecto9\\Mi_Gran_Directorio'
patron = r'N\w{3}-\d{5}'
hoy = datetime.date.today()
num_encontrado = []
archivos_encon = []

def buscador(archivo,patron):

   archivo_curso = open(archivo,'r')
   leer = archivo_curso.read()
   if re.search(patron,leer):
       return re.search(patron,leer)

   else:
       return '' # si no podemos una cadena vacia me va a devolver NONE


def crear_listado():

    for carpeta,subcarpeta,archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscador(Path(carpeta,a),patron)
            if resultado != '':
                num_encontrado.append(resultado.group())#   ---> me los agrupe y no coga todos los datos
                archivos_encon.append(a.title())    #   ---> nos cogerá el nombre del archivo



def salida():
    indice = 0
    print('-' * 50)
    print(f'Fecha Busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('\tArchivo \t\tNúmero de Serie')
    print('\t------- \t\t---------------')
    for n in archivos_encon:
        print(f'\t{n}\t\t{num_encontrado[indice]}')
        indice +=1
    print('\n')
    print(f'Números encontrados: {len(num_encontrado)}')
    final = time.time()
    tiempo = final-inicio
    print(f'Duración de la busqueda: {math.ceil(tiempo)} segundo/s')
    print('-' * 50)

crear_listado()
salida()