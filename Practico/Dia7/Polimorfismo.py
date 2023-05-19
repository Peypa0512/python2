class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre +" Muuuu")

class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre +" Beee")


mi_vaca =Vaca('Lola')
mi_oveja= Oveja('Claudia')

animales =[mi_vaca,mi_oveja]

for animal in animales:
    animal.hablar()# en una iteración se hace llamar al método hablar aunque sea de distintas clases

def animal_hablar(animal):
    animal.hablar()

animal_hablar(mi_vaca)
animal_hablar(mi_oveja)