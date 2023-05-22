import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro microfono audio en texto
def transformar_audio_en_texto():
    # almacenamos el reconocedor en una variable
    r = sr.Recognizer()

    # configuramos el microfono
    with sr.Microphone() as origen:

        # tiempo de espera que necesita el microfono
        r.pause_threshold = 0.8

        # informamos si comenzó a grabar
        print('Se esta grabando')

        # guardar lo que escuche
        audio = r.listen(origen)

        # si hay errores
        try:
            #buscar en google lo que ha escuchado
            pedido = r.recognize_google(audio, language="es-es")

            # imprimir en pantalla para ver que ha grabado
            print('Dijiste: '+pedido)

            # devolver a pedido
            return pedido
        # en caso que no comprenda
        except sr.UnknownValueError:
            print('No comprendió el audio')
            #devuelve el error
            return 'sigo esperando'
        #en caso de no devolver el pedido
        except sr.RequestError:
            # prueba que no comprendio el audio
            print('UPS, no he entendido nada')
            return 'sigo esperando'

        #error inexperado
        except:
            #prueba de que no comprende el audio
            print('Algo ha salido mal')
            return 'sigo todavia esperando'


#vamos a crear una base de datos para las diferentes fuentes que tengo ...

id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# funcion para que el asistente pueda ser escuchado

def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Informar dia
def pedir_dia():

    #crear la variable de datos de hoy
    dia = datetime.date.today()
    fecha = datetime.date.today().day
    mes = datetime.date.today().month
    anyo = datetime.date.today().year
    dia_semana = dia.weekday()


    # diccionario del dia de la semana
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sabado',
                  6: 'Domingo'}


    # diccionario de los meses
    mes_calendario = {
                  1: 'Enero',
                  2: 'Febrero',
                  3: 'Marzo',
                  4: 'Abril',
                  5: 'Mayo',
                  6: 'Junio',
                  7: 'Julio',
                  8: 'Agosto',
                  9: 'Septiembre',
                  10: 'Octubre',
                  11: 'Noviembre',
                  12: 'Diciembre'

    }

    #decir el día de la semana
    hablar(f'Hoy es {calendario[dia_semana]},{fecha} de {mes_calendario[mes]} de {anyo}')

    print(f'{calendario[dia_semana]},{dia}')

# Informar hora
def pedir_hora():
    #pedir hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} , con {hora.minute} minutos y {hora.second} segundos'

    # voy a decir la hora
    hablar(hora)

# Saludo Inicial
def saludo_inicial():
    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'




    #decir el saludo
    hablar(f'{momento}, soy Eloisa, tu asistente personal, en que puedo ayudarte?')


#FUNCION CENTRAL DEL ASISTENTE
def pedir_cosas():
    # lo primero es que haga el saludo inicial
    saludo_inicial()

    #hacemos un while para que esté funcionando y esperando a que digamos algo
    #variable de corte
    comenzar = True
    while comenzar:
        # activamos el micro y guardar el pedido en un String
        pedido = transformar_audio_en_texto().lower()

        # vemos que tiene y que quiere que haga
        if 'abrir youtube' in pedido:
            hablar('Abriendo Youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Estoy abriendo el navegador')
            webbrowser.open('https://www.google.com')
            continue
        elif 'hola' in pedido:
            hablar('Hola Pedro')
            continue
        elif 'qué día es hoy' in pedido:
            print("dia")
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            print("hora")
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando información')
            pedido = pedido.replace('wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido,sentences=1)
            hablar('Wikipedia dice lo siguiente...')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Estoy en ello')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Empiezo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'cuéntame un chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'mensaje' in pedido:
            mensaje = pywhatkit.sendwhatmsg('telefono','mensaje',time_hour=datetime.now,time_min=1,wait_time=15)
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon':'AMZN',
                        'google': 'GOOGL'
                        }
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'el precio de la accion de {accion} es {precio_actual}')
                continue

            except:
                hablar('Parece ser que no he podido encontrarla')

        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break






pedir_dia()
pedir_cosas()
