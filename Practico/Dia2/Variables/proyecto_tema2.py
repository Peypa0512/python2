"""Tenemos una empresa
en la que hay una serie de vendedores, tenemos que
pedir su nombre y cuanto han vendido, sabiendo que
de su venta tienen una comisión del 13%
"""

nombre = input("Introduce tu nombre > ")
ventas = float(input("Introduce las ventas que ha tenido> "))
resultado = round(ventas*0.13,2)
print(f"El empleado {nombre} ha percibido una comisión por sus ventas de {resultado}€")