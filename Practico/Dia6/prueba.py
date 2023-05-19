from pathlib import Path
import os

ruta = Path('/Users/pedro/Desktop/Python/Dia6/recetas')

def categoria(ruta):




    print('Bienvenido a la pantalla de Categoria')
    print('')
    print('''
            1.- Mostrar todas las categorias
            2.- Crear una nueva categoria
            3.- Eliminar una categoria
            ''')
    numero= input("Elige la opción que deseas realizar> ")

    while numero not in '123':
        print("Debes elegir entre estas opciones")
        opcion = input("Elige la opción deseada> ")

    match numero:
        case '1':
            cuenta = 1
            for x in ruta.iterdir():
                print(f'{cuenta}.- {x.stem}')
                cuenta += 1


        case '2':
            cuenta = 1

            for x in ruta.iterdir():
                print(f'{cuenta}.- {x.stem}')
                cuenta += 1

            crear = input('¿Como se va a llamar la nueva categoria?... ').capitalize()
            while crear not in ruta:
                if crear in ruta:
                    print("Por favor vuelve a introducir otra categoria")
                    crear = input('¿Como se va a llamar la nueva categoria?... ').capitalize()
            carpeta = ruta / crear
            nueva = os.mkdir(carpeta)

            if os.path.isdir(carpeta):
                print(f"Se ha creado la carpeta {crear}")
            else:
                print(f"No se ha creado la carpeta {crear}")

        case '3':
            cuenta = 1



            for x in ruta.iterdir():
                print(f'{cuenta}.- {x.stem}')
                cuenta += 1
            eliminar = input('¿Qué categoria quieres eliminar?> ').capitalize()

            carpeta = ruta / eliminar
            os.rmdir(carpeta)
            if os.path.isdir(carpeta):
                print(f"existe la carpeta {eliminar}")
            else:
                print(f" Ya no existe la carpeta {eliminar}")
            print()
            descon = 1
            for x in ruta.iterdir():
                print(f'{descon}.- {x.stem}')
                descon += 1

    return ruta




#menu
menu=0

match menu:
    case 1:
        # Mostrar categorias
        # elegir categorias
        # mostrar recetas
        # elegir recetas
        # leer recetas
        # volver al inicio
        pass
    case 2:
        # Mostrar categorias
        # Elegir categoria
        # Crear receta nueva
        # volver al inicio
        pass
    case 3:
        # Crear categoria
        # volver al inicio
        pass
    case 4:
        # Mostrar categorias
        # elegir categorias
        # mostrar recetas
        # elegir recetas
        # Eliminar recetas
        # volver al inicio
        pass
    case 5:
        # Mostrar categorias
        # elegir categoria
        # eliminar categoria
        # volver al inicio
        pass
    case 6:
        # salir
        pass