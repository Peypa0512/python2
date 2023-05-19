mi_lista =[1,1,1,1,1,1]
print(len(mi_lista))

class Objeto():
  pass

mi_objeto = Objeto()
print(mi_objeto)

class CD:
    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self): # este metodo especial hace que ayuda a definir en que se manifieste un str cuando un metodo
                       #lo necesite
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado el cd") # cuando se utilice el método del saldrá por pantalla esto.

mi_cd = CD('pink floyd','walk',24)

print(mi_cd)# normalmente si hago esta llamada me saldrá... <__main__.Objeto object at 0x00000202A02B4150>
print(len(mi_cd)) # dará este error TypeError: object of type 'CD' has no len()

# hay otro metodo que se llama del

del  mi_cd #borrará el objeto mi_cd, pero no sabemos si lo ha hecho o no