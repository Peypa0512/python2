import zipfile
import shutil
'''
mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()

zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','r')

zip_abierto.extractall()
'''

# permite de un modo más practico la compresion de todos los ficheros de una carpeta
'''
carpeta_origen = 'C:\\Users\\Usuario\\Documents\\software\\Python\\Dia9'

archivo_destino = 'todo_comprimido'
shutil.make_archive(archivo_destino,'zip',carpeta_origen)
'''
#shutil.unpack_archive('todo_comprimido.zip','Extraccion','zip')
shutil.unpack_archive('Proyecto+Dia+9.zip','proyecto9','zip')