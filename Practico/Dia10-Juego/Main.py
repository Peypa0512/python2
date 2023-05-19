import pygame
import random
import math
from pygame import mixer

pygame.init() # para inicializarlo

#vamos a definir tamaño de pantalla

pantalla = pygame.display.set_mode((800,600))  # altura y anchura en una tupla

# para que la pantalla se siga viendo hay que seguir metiendo codigo

#Titulo e Icono

pygame.display.set_caption("Juego de Ovnis")
icono = pygame.image.load('ovnis.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo2.png")

# agregar Musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)  # volumen
mixer.music.play(-1)    # significa que sonará cuando termine

#puntaje
puntaje = 0
fuente = pygame.font.Font('halfelven.ttf', 32)
texto_x = 10
texto_y = 10

# VARIABLES FINAL_JUEGO
fuente_final = pygame.font.Font('Zanzabar Demo.otf',40)

# VARIABLES JUGADOR
img_jugador = pygame.image.load('nave-espacial.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# VARIABLES ENEMIGO
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos =8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('ovni.png'))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)


# VARIABLE DE LA BALA
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

#funcion de Final de juego

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO",True,(255,255,255))
    pantalla.blit(mi_fuente_final,(60,200)) #centro de la pantalla

# FUNCION JUGADOR
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))

# FUNCION Enemigo
def enemigo(x,y, ene):
    pantalla.blit(img_enemigo[ene], (x,y))

# FUNCION BALA
def disparar_bala(x,y):
    global bala_visible # para poder acceder a la funcion bala visible (global)
    bala_visible = True
    pantalla.blit(img_bala, (x+16, y+16)) # para que aparezca la bala en el centro de la nave

# Funcion Detectar Colisiones
def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1-x_2,2)+math.pow(y_2-y_1,2)) # esto dará un nº de pixel de distancia

    if distancia < 27:
        return True
    else:
        return False

#Función de Puntuación
def puntuacion(x,y):
    texto = fuente.render(f'Puntuación : {puntaje}',True,(255,255,255))
    pantalla.blit(texto,(x,y))




se_ejecuta = True
#LOOP de la pantalla
while se_ejecuta:
    # cambiamos el color de la pantalla
    pantalla.blit(fondo,(0,0))


    # habrá que poner cualquier evento y que va a suceder con cada uno de ellos
    # pygame.event.get por cada evento que haya en el juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # si cada tipo de evento = QUIT(la X de salida de la ventana)
            se_ejecuta = False

        # vamos a ver si movemos alguna tecla
        if evento.type == pygame.KEYDOWN:
            print('Una tecla ha sido presionada')
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
                print('Flecha izquierda presionada')
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = +1
                print('Flecha derecha presionada')

            #evento para disparar bala
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not bala_visible :
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # CUANDO LEVANTAMOS EL DEDO DE LA TECLA
        if evento.type == pygame.KEYUP:

            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
                print("La tecla se soltó")

    # llamamos a la funcion jugador Y modificar ubicación
    jugador_x += jugador_x_cambio

    #mantener dentro de los bordes
    if jugador_x <= 2:
        jugador_x = 2

    if jugador_x >= 734:
        jugador_x = 734

    #mantener dentro de los bordes al enemigo
    for e in range(cantidad_enemigos):

        # PARA VERIFICAR SI ALGUNO HA LLEGADO ABAJO A LA ALTURA DE LA NAVE

        if enemigo_y[e] > 500:
            for k in range (cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break


        enemigo_x[e] += enemigo_x_cambio[e]

    # mantener dentro de los bordes
        if enemigo_x[e] <= 2:
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]

        if enemigo_x[e] >= 734:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]
            # verificacion de colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1

            enemigo_x[e] = random.randint(0, 736)  # cuando damos a la nave, se vuelve a reiniciar
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)
    # movimiento de Bala
    if bala_y <= -32:       #tamaño de la bala
        bala_y = 500
        bala_visible= False

    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio



    jugador(jugador_x, jugador_y)
    puntuacion(texto_x,texto_y)

    # Actualizar el desarrollo
    pygame.display.update()
