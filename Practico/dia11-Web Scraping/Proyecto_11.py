import bs4
import requests

# creamos una url sin número de páginas
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

#creamos una lista vacia que va a contener 4 0 5 estrellas

titulos_rating_alto =[]

#   vamos a iterar las páginas

for pagina in range(1,51):
    # en cada iteración va a crear una página distinta
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # vamos a crear una variable con  la selección de los libros
    libros= sopa.select('.product_pod')

    #vamos a iterar en los libros

    for libro in libros:
        # chequea si tiene 4 0 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # guardamos el titulo en la variable
            titulo_libro = libro.select('a')[1]['title']

            #agregamos el libro a la lista
            titulos_rating_alto.append(titulo_libro)

#ver libro 4  o 5  estrellas en consola

for t in titulos_rating_alto:
    print(t)