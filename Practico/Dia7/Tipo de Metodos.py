class Pajaro:
    alas = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    #metodo de instancia que afecta al método self
    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print('Ahora el pajaro es {}'.format(self.color))

    #metodos de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} de huevos')
        cls.alas = False
        print(Pajaro.alas)

    # metodos estaticos

    @staticmethod
    def mirar():
        #self.color= 'rojo'
        print('El pajaro mira')



piolin = Pajaro('amarillo','canario')

#metodos de instancia
piolin.piar()
piolin.pintar_negro()
piolin.volar(50)
piolin.alas = False
print(piolin.alas)

#metodos de clase
Pajaro.poner_huevos(3) #hay que recordar que se hace la llamada a la clase no al objeto

#metodos estaticos
Pajaro.mirar()
