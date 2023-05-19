nombres = ['Juan', 'Rosa', 'Miriam', 'Luis']
profesiones = ['Abogado', 'Médico', 'Maestra', 'Médico']

# ----- Opción 1 (a mano)
trabajos = {}
for i in range(len(nombres)):
    profesion = profesiones[i]
    persona = nombres[i]
    if profesion not in trabajos:
        trabajos[profesion] = [persona]
    else:
        trabajos[profesion].append(persona)
print(trabajos)

# ----- Opción 2 (modo más pythónico)
# Usamos la función zip. A esta función
# se le puede pasar como argumentos un número
# indeterminado de iterables y devuelve un
# iterador de tuplas, en el que cada tupla está
# formada por un elemento de cada iterable en orden.
trabajos = {}
for profesion, persona in zip(profesiones, nombres):
    if profesion not in trabajos:
        trabajos[profesion] = [persona]
    else:
        trabajos[profesion].append(persona)
print(trabajos)
