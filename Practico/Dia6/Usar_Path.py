from pathlib import Path
# esta ruta es relativa, es decir, puede estar en varios directorios, habría que especificar en cual
guia = Path('Barcelona','Sagrada_Familia.txt')
#print(guia)

#podemos usar el método home() para obtener la ruta absoluta

base = Path.home()
#guia2 = Path('Madrid','Gran_Via.txt')
print(base)
#print(guia2)
guia21 = Path(base,'Madrid','Gran_Via.txt')
print(guia21)

#podemos concatear path dentro de otro path
guia22 = Path(base,'Europa','España',Path('Madrid','Gran_Via.txt'))
print(guia22)

#podemos crar un objeto nuevo apuntado de otro lado distinto

guia3 = guia21.with_name("La_Pedrera.txt")
print(guia3)

#parent devuelve el antecesor más inmediato de la ruta por cada vez que se agregue
#print(guia21.parent.parent)

# para enumerar todos los archivos txt de la carpeta que he creado Europa

guia4 = Path(Path.home(),"Europa")
print(guia4)
for txt in Path(guia4).glob("*.txt"):
    print(txt)

# para sacar todos los txt que haya

for txt2 in Path(guia4).glob("**/*.txt"):
    print(txt2)

# cuando se quiere recuperar parte de la ruta se utiliza el metodo relativeto()

guia5 = Path('Mundo','Europa','Peninsula_Iberica','España','Madrid','El_Escorial','Monasterio')


en_europa = guia5.relative_to(Path("Mundo"))
en_espana = guia5.relative_to(Path("Mundo","Europa"))
print(en_europa)
print(en_espana)