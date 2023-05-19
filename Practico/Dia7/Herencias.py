class Animal:

    def __init__(self,edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal): #hereda de animal
    pass

print(Pajaro.__bases__)
print(Animal.__subclasses__())

piolin = Pajaro(2,'amarillo')
piolin.nacer()
print(piolin.color)


class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass

