import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')



#para ver lo que queremos ver, utilizaremos el beatifulsoup

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
print(sopa.select('title')[0].getText())
print(len(sopa.select('p')))
print('\n')

#otro ejemplo un parrafo en negrita
parrafo_especial= sopa.select('p')
print(parrafo_especial[3].getText())

#como capturar una clase

columna_lateral = sopa.select('.item-content div')
for p in columna_lateral:
    print(p.getText())



resultado1 = requests.get('https://www.escueladirecta.com/courses')

sopa = bs4.BeautifulSoup(resultado1.text, 'lxml')

imagenes = sopa.select('.course-box-image')[0]['src'] # esto nos dará la url donde está alojada la imagen

print(imagenes)

imagen_curso_1 = requests.get(imagenes)

f = open('mi_imagen.jpg','wb')
f.write(imagen_curso_1.content)
f.close()



