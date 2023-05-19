cliente ={'nombre':'Federico',
           'edad' : 45,
           'profesion': 'Instructor'}

pelicula={'titulo':'Matrix','ficha_tecnica':{'protagonista':'Keanu Reeves','director':'Lana y Lilly Wachowski'}

elementos = [cliente, pelicula,'libro']

for e in elementos:
    match e:
        case{'nombre': nombre,
             'edad': edad,}
              'profesion': profesion}:
                print("es un cliente"
                print(nombre,edad,profesion

        case{'titulo':titulo,
             'ficha_tecnica': ficha_tecnica{'protagonista':protagonista, 'director':director}
                print("esto es una pelicula"
                print(titulo,protagonista, director
        case_:
            print("No se que es esto")