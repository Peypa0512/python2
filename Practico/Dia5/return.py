
def multiplicar(num1,num2):
    total= num1*num2
    return total

resultado = multiplicar(200,5)

print(resultado)


def potencia(num1,num2):
    return pow(num1,num2)

def usd_a_eur(num):
    return num*0.9

dolares = usd_a_eur(20)

def invertir_palabra(palabra):
   vuelta = palabra[::-1].upper()
   return vuelta

palabra = invertir_palabra('python')
print(palabra)