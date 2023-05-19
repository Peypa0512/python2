
#vamos a usar cualquiera de los dos modulos
#utilizaré el paquete PEdro

from Pedro import Suma_Resta  # para importar funciones del paquete
from Pedro.Subpaquete import Saludo # para llamar a los subpaquetes

Suma_Resta.suma(15,2)
Suma_Resta.resta(20,3)

Saludo.hola()