import glob
import os
from pathlib import Path
from os import system

# o así ruta = Path(Path.home(),"recetas")
ruta = Path('/Users/pedro/Desktop/Python/Dia6/Recetas')


def contarRecetas(ruta):
    contador = 0

    # contador de las recetas que tenemos
    for fichero in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador


def inicio():
    system('cls')
    print('     Bienvenido al Menú de Recetas')
    print('     -----------------------------')
    print()
    print(f'Las recetas se encuentran en {ruta}\nDisponemos de {contarRecetas(ruta)} recetas')

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print('''

            1.- Leer Recetas
            2.- Crear recetas nuevas
            3.- Crear categoria nueva
            4.- Eliminar recetas
            5.- Eliminar categoria
            6.- Salir

        ''')
        eleccion_menu = input("Elige la opcion deseada....>")
    return int(eleccion_menu)


def mostrarCategorias(ruta):
    # creamos la función para mostrar todas las carpetas

    print("Categorias: ")
    ruta_categoria = Path(ruta)
    lista_categoria = []
    contador = 1

    for carpeta in ruta_categoria.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'{contador} .- {carpeta_str}')
        lista_categoria.append(carpeta)
        contador += 1

    return lista_categoria


def elegirCategoria(lista):
    eleccion_correcta = 'x'

    # el range va desde el 1 hasta el final de la lista hay que recordar que el último no está incluido
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoria: ")

    return lista[int(eleccion_correcta) - 1]  # necesitamos restar 1 para que nos dé el indice correcto


def mostrarRecetas(ruta):
    # necesitamos imprimir las recetas, crear ruta
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob('**/*.txt'):
        receta_str = str(receta.name)
        print(f'{contador}.- {receta_str}')
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas


def elegirRecetas(lista):
    # llamamos a la lista de recetas y hacemos una elección que nos muestre todo

    seleccion_receta = 'x'

    while not seleccion_receta. or int(seleccion_receta) not in range(1, len(lista) + 1):
        seleccion_receta = input('\nElige una opcion  ')
    return lista[int(seleccion_receta) - 1]


def leerReceta(lista):
    print(Path.read_text(mi_receta))


def crearReceta(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de la nueva receta")
        nombre_receta = input().capitalize() + '.txt'
        print("Escribe la nueva receta")
        contenido_receta = input().capitalize()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} ha sido creada')
            existe = True
        else:
            print("Esa receta ya existe")


def crearCategoria(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de la nueva Categoria ")
        nombre_categoria = input().capitalize()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'La categoria  {nombre_categoria} ha sido creada')
            existe = True
        else:
            print("Esa carpeta ya existe")


def eliminarReceta(receta):
    Path(receta).unlink()  # con este metodo .unlink eliminamos el archivo
    print(f'La receta {receta.name} ha sido eliminado')


def eliminarCategoria(categoria):
    #para borrar la carpeta primero habrá que borrar lo que contenga
    ruta_eliminar=Path(ruta/categoria)
    for txt in ruta_eliminar.glob('**/*.txt'):
        os.remove(txt)
    # una vez borrado tod@ lo que contiene la carpeta
    Path(categoria).rmdir()  # Borra esa carpeta
    print(f'La categoria{categoria.name} ha sido eliminada')


def volverInicio():
    regreso = 'x'

    while regreso.lower() != 'v':
        regreso = input("'V' para volver al menú principal ")


# menu

finalizar_programa = False
while not finalizar_programa:
    system('cls')
    menu = inicio()
    match menu:
        case 1:
            mis_categorias = mostrarCategorias(ruta)  # Mostrar categorias
            mi_categoria = elegirCategoria(mis_categorias)  # elegir categorias
            mis_recetas = mostrarRecetas(mi_categoria)  # mostrar recetas
            mi_receta = elegirRecetas(mis_recetas)  # elegir recetas
            leerReceta(mi_receta)  # leer recetas
            if len(mis_recetas) < 1:
                print("no hay recetas en esta categoría.")
            else:
                mi_receta = elegirRecetas(mis_recetas)
                leerReceta(mi_receta)
            volverInicio()  # volver al inicio

        case 2:
            mis_categorias = mostrarCategorias(ruta)  # Mostrar categorias
            mi_categoria = elegirCategoria(mis_categorias)  # Elegir categoria
            crearReceta(mi_categoria)  # Crear receta nueva
            volverInicio()  # volver al inicio

        case 3:
            crearCategoria(ruta)  # Crear categoria
            volverInicio()  # volver al inicio

        case 4:
            mis_categorias = mostrarCategorias(ruta)  # Mostrar categorias
            mi_categoria = elegirCategoria(mis_categorias)  # elegir categorias
            mis_recetas = mostrarRecetas(mi_categoria)  # mostrar recetas
            mi_receta = elegirRecetas(mis_recetas)  # elegir recetas
            eliminarReceta(mi_receta)  # Eliminar recetas
            volverInicio()  # volver al inicio

        case 5:
            mis_categorias = mostrarCategorias(ruta)  # Mostrar categorias
            mi_categoria = elegirCategoria(mis_categorias)  # elegir categoria
            eliminarCategoria(mi_categoria)  # eliminar categoria
            volverInicio()  # volver al inicio

        case '6':
            finalizar_programa = True  # salir
