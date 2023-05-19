#verificamos si lo hemos hecho bien

import unittest
import cambia_texto

class ProbarCambiarTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'hola, buenos días'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado,"HOLA, BUENOS DÍAS") #compara si es igual a lo que debería dar


if __name__ ==   '__main__': # esta es la función principal
   unittest.main()
