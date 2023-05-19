import re


texto = "Si nececesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de la ayuda online"
#patron ='nada'
patron = 'ayuda'

busqueda = re.findall(patron,texto)
print(busqueda)

palabra = 'ayuda' in texto
print(palabra)

for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())

ayuda = "llama al 564-525-6588 ya mismo"

# patron = r'\d\d\d-\d\d\d-\d\d\d\d'

patron = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron,ayuda)

print(resultado.group())

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron,ayuda)
print(resultado.group(2))


'''clave = input("Clave: ")

patron = r'\D{1}\w{7}'

chequear = re.search(patron,clave)
print(chequear) 
'''

frase ='No atendemos los lunes por la tarde'

busqueda = re.search(r'....demos....',frase)
print(busqueda)

busqueda1 = re.search(r'^\D',frase)
print(busqueda1)

busqueda2 = re.search(r'\D$',frase)
print(busqueda2)

busqueda3 = re.findall(r'[^\s]+',frase)
print(busqueda3)

print(''.join(busqueda3))

def verificar_email(email):

    if '@' in email:
        if '.com' in email:
            print("Ok")
        else:
            print("La dirección de email es incorrecta")
    else:
        print("La dirección de email es incorrecta")


verificar_email('pepe@pepe.com')

def verificar_email2(email):


        patron = r'@\w+\.com'

        busqueda = re.search(patron, email)

        if busqueda:
            print("Ok")
        else:
            print("La dirección de email es incorrecta")

verificar_email2('pepe@pepe.com')

def verificar_email3(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron,email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

verificar_email3('pepe@pepe.es')