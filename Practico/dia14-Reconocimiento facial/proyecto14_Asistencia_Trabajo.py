from cv2 import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

#CREAMOS LA BASE DE DATOS

ruta = 'Empleados'
mis_imagenes = []
nombres_empleados =[]
lista_empleados = os.listdir(ruta)

#cargamos las imagaenes

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

#codificar imagenes

def codificar(imagenes):
    #creamos una lista nueva codificada
    lista_codificada =[]

    #pasar todas las imagenes a RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        #codificamos las imagenes
        codificado = fr.face_encodings(imagen)[0]

        # agregar a la lista
        lista_codificada.append(codificado)

    # retorna lista_codificada
    return lista_codificada

lista_empleados_codificada = codificar(mis_imagenes)

#función para guardar los ingresos al trabajo
def registrar_ingresos(persona):

    #creamos un fichero registro.csv
    f = open('registro.csv','r+')
    lista_datos = f.readlines()
    nombre_registro =[]

    # hacemos un for para
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombre_registro.append(ingreso[0])
    if persona not in nombre_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona},{string_ahora}')


# tomar una imagen  de camara web

captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#leer la imagen de la camara

exito, imagen = captura.read()

if not exito:
    print("No se ha podido obtener la captura")
else:

    #reconocer cara en la captura
    cara_captura= fr.face_locations(imagen)
    # codifica la cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)
    # buscar coincidencias
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)
        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        #mostrar coincidencias
        if distancias[indice_coincidencia] >6 :
            print('No coincide con ninguno de nuestros empleados')
        else:
            # buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]


            y1,x2,y2,x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0,255,0),2)
            cv2.rectangle(imagen,(x1, y2 -35), (x2, y2),(0,255,0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 -6),cv2.FONT_HERSHEY_DUPLEX,0.7,(255,255,255), 2)
            registrar_ingresos(nombre)

            # mostrar la imagen obtenida
            cv2.imshow('Imagen Web', imagen)

            # mantener ventana abierta
            cv2.waitKey(0)


