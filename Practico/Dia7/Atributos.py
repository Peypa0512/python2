class Pajaro:
    # atributos de clase
    alas = True


    def __init__(self,color,especie): #metodo constructor, con un parametro self(obligatorio) y otro que es color
        self.color = color # self. instancia del objeto que se va a crear
        self.especie = especie

mi_pajaro= Pajaro('negro','tucan')# se necesita que pases el parametro color

print(mi_pajaro.color) # al hacer el objeto ten dremos los atributos de la clase en este caso color
print(f'Mi pajaro es un {mi_pajaro.especie} y es de color{mi_pajaro.color}')

# para imprimir un atributo de clase no pasan por __init__ por lo que puedo llamarlo directamente
print(Pajaro.alas)
#o mediante el objeto
print(mi_pajaro.alas)