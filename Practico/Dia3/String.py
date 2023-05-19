
mi_texto ="Esta es mi prueba"

resultado = mi_texto[-4]
print(resultado)

resultado1 = mi_texto.index("a")
print(resultado1)
resultado1 = mi_texto.rindex("a")
print(resultado1)

texto ="ABCDEFGHIJKLM"

fragmento = texto[2]
print(fragmento)

fragmento = texto[2:5]
print(fragmento)

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[8::3])


texto1 ="este es el texto de ejemplo"
resultado1=texto1.upper()
print(resultado1)
resultado1=texto1[2].upper()
print(resultado1)

resultado1=texto1.lower()
print(resultado1)

resultado1=texto1.split()
print(resultado1)

resultado1=texto1.split('t')
print(resultado1)


a ="aprender"
b ="Python"
c ="es"
d="genial"
e=" ".join([a,b,c,d])
print(e)

resultado1= texto1.find("z")
print(resultado1)

texto ="este es el texto de ejemplo"

resultado = texto.replace("ejemplo","Pedro")
print(resultado)

lista_palabras = ["La","legibilidad","cuenta."]
resultado =" ".join(lista_palabras)
print(resultado)

texto="Si la implementación es difícil de explicar, puede que sea una mala idea."
texto =texto.replace("difícil","fácil")
texto = texto.replace("mala","buena")
print(texto)

nombre =""" Mil pequeños peces  blancos 
        como si hirviera el color del agua"""

print(nombre)

print( "agua" in nombre)

print( "agua" not in nombre)

print(len(nombre))
