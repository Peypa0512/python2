from os import system
from random import randint

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,cuenta,balance):
        super().__init__(nombre,apellido)
        self.cuenta = cuenta
        self.balance = balance

    def __str__(self):
        return f'{self.apellido}, {self.nombre} Nº Cuenta: {self.cuenta} con un saldo: {self.balance}€'

    def depositar(self, cantidad):
        self.cantidad = cantidad
        self.balance = self.balance + self.cantidad
        return f'En estos momento el saldo de la cuenta es de {self.balance} €'
    def retirar(self, cantidad):
        self.cantidad = cantidad
        self.balance = self.balance - self.cantidad
        if self.balance > 0:
            return f'En estos momentos el saldo de la cuenta es de {self.balance}€'
        else:
            return 'No se puede realizar esta operación, dinero insuficiente'

def crearCliente():
    nombre = input("¿Buenos días, me puede decir su Nombre? ")
    apellido = input("¿Y sus Apellidos? ")
    cuenta = randint(600, 1200)
    balance = int(input("¿Cuál va a ser la cantidad inicial que va a Ingresar? " ))
    cliente= Cliente(nombre,apellido,cuenta,balance)
    return cliente

def inicio():
    estado =False
    system('cls')
    print("BIENVENIDO AL BANCO PUTURRU DE FUA")
    print()
    print("BIENVENIDO AL MENU PRINCIPAL")
    print()
    cliente=crearCliente()
    print(cliente)


    while estado != True:

        opcion = int(input(f"{cliente.nombre}, que operacion desea realizar?, eliga una opción (1, 2, 3) "))
        match opcion:
                        case 1:
                            cantidad = int(input("¿Que cantidad desea Ingresar? "))
                            print(cliente.depositar(cantidad))

                        case 2:
                            cantidad = int(input("¿Qué cantidad desea retirar? "))
                            print(cliente.retirar(cantidad))
                        case 3:
                            print("Un placer haberle atendido, adios!!!")
                            estado = True




inicio()