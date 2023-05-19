import os
import send2trash


# para saber en que directorio estamos

print(os.getcwd()) #cwd directorio trabajo actual

# para crear un archivo

archivo = open('curso.txt','w')
archivo.write('texto de prueba')
archivo.close()

# para ver desde aqui

print(os.listdir())


'''
 eliminar archivo:

        os.unlink()  #elimina archivo y ruta que le pongas
        os.rmdir() ---> elimina carpeta vacia
        


'''
#end2trash.send2trash('C:\\Users\\Usuario\\Documents\\software\\Python\\Dia8\\curso.txt')

ruta = 'C:\\Users\\Usuario\\Documents\\software\\Python'

for carpeta,subcarpeta,archivo in os.walk(ruta):
    print(f"La ruta es {carpeta}")
    print('las subcarpetas son: ')
    for sub in subcarpeta:
        print(f"\t {sub}")
    print('Los archivos son:')
    for arch in archivo:
        if arch.startswith('Apuntes'.upper()):
            print(f'\t {arch}')
    print('\n')


