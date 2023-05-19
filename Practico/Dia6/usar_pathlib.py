from pathlib import Path, PureWindowsPath

carpeta =Path('/Users/pedro/Documents/PYTHON/curso/dia6/Prueba.txt')
# read_text() nos imprime lo que tenga el archivo
print(carpeta.read_text())

#name nos devuelve el nombre del archivo
print(carpeta.name)

#suffix es una función como name ya que no tiene parentesis y nos dará el subfijo del archivo la extension
print(carpeta.suffix)

#la función stem nos dará sin la terminación
print(carpeta.stem)

#hay un metodo que te permita si existe .exists() es booleano

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Existe, genial!! ')

#PureWindowsPath transforma la ruta a windows

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)