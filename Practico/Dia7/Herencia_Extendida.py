class Animal:

    def __init__(self,edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal): #hereda de animal

    #puede tener atributos propios (2 maneras), 1º
    def __init__ (self,edad,color,altura_vuelo):
        #self.edad = edad # 1º metodo
        #self.color = color 1º método
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    # tenemos este método
    def hablar(self):
        print('pio')
    def volar(self,metros):
        print(f'El pajaro vuela {metros} metros')



print(Pajaro.__bases__)
print(Animal.__subclasses__())

# objeto clase hija
piolin =Pajaro(3,'amarillo',40)

#objeto clase Padre
mi_animal = Animal(5,'negro')

#métodos heredados
piolin.nacer()
piolin.hablar() #metodo sobreescrito por hablar de la clase Pajaro()
#método propio
piolin.volar(50)


#Herencia Multiple

class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('JAJAJA')

    def hablar(self):
        print('¿que tal?')

class Hijo(Padre,Madre): # se hereda 1º izquierda y luego derecha
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.reir()
mi_nieto.hablar()

print(Nieto.__mro__) #orden de resolución de métodos


