import datetime
from tkinter import *
import random
from tkinter import filedialog,messagebox

#creamos esta variable para definir los botones
operador = ''

#vamos a crear 3 variables con los precios
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94]






def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0,resultado)
    operador = ''

def revisar_check():
    # va a llamar a esta función cada vez que se activa un checkbutton
    x= 0
    for c in cuadros_comida:
        if variable_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x +=1

    x = 0
    for c in cuadros_bebida:
        if variable_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x +=1

    x = 0
    for c in cuadros_postre:
        if variable_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0,END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x +=1

def total():
    #cuando pulse tendrá que sumar todo lo que haya
    subtotal_comida =0
    p =0
    for cantidad in texto_comida:
        subtotal_comida= subtotal_comida+(float(cantidad.get())*precios_comida[p])
        p+=1


    subtotal_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebida= subtotal_bebida+(float(cantidad.get())*precios_bebida[p])
        p+=1


    subtotal_postre = 0
    p = 0
    for cantidad in texto_postre:
        subtotal_postre= subtotal_postre+(float(cantidad.get())*precios_postres[p])
        p+=1

    subtotal = subtotal_comida+subtotal_bebida+subtotal_postre
    impuestos = subtotal*0.07
    total = subtotal+impuestos

    var_coste_comida.set(f'{round(subtotal_comida,2)} €')
    var_coste_bebida.set(f'{round(subtotal_bebida, 2)} €')
    var_coste_postre.set(f'{round(subtotal_postre, 2)} €')
    var_Subtotal.set(f'{round(subtotal, 2)} €')
    var_Impuesto.set(f'{round(impuestos, 2)} €')
    var_Total.set(f'{round(total, 2)} €')

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year}--{fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}  \t{fecha_recibo}\n')
    texto_recibo.insert(END,f'*'*49+'\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCoste Items \n')
    texto_recibo.insert(END,f'-'*63+'\n')

    #ahora tenemos que ver que ha consumido, cantidad y precio de cada plato
   #para comidas
    x =0
    for comida in texto_comida:
        if comida.get() !='0':
            texto_recibo.insert(END,f'{lista_comida[x]}\t\t{comida.get()}\t{int(comida.get())*precios_comida[x]} €\n')
        x +=1
    #para bebidas
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END,f'{lista_bebida[x]}\t\t{bebida.get()}\t{int(bebida.get()) * precios_bebida[x]} €\n')
        x += 1
    # para postres
    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END,f'{lista_postres[x]}\t\t{postre.get()}'
            f'\t{round(int(postre.get()) * precios_postres[x],2)} €\n')
        x += 1

    texto_recibo.insert(END, f'-' * 63 + '\n')
    texto_recibo.insert(END, f'Precio de la Comida:\t\t  {var_coste_comida.get()}\n')
    texto_recibo.insert(END, f'Precio de la Bebida:\t\t    {var_coste_bebida.get()}\n')
    texto_recibo.insert(END, f'Precio de los Postres:\t\t{var_coste_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 63 + '\n')
    texto_recibo.insert(END, f'Subtotal:\t\t{var_Subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos:\t\t {var_Impuesto.get()}\n')
    texto_recibo.insert(END, f'Total:\t\t{var_Total.get()}\n')
    texto_recibo.insert(END, f'-' * 63 + '\n')
    texto_recibo.insert(END,'Gracias por su visita\n')
    texto_recibo.insert(END, '\n')
    texto_recibo.insert(END, f'*' * 53 + '\n')


def guardar():

    # toma la informacion del recibo y lo mete en una variable
    info_recibo = texto_recibo.get(1.0,END)
    archivo = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información','Su recibo ha sido guardado')

def resetear():
    # texto recibo
    texto_recibo.delete(0.1,END)
    # cantidades de platos
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')
    # desabilitar checkbox
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)
    # desabilitar variables( guarda el valor 0 0 1 del checkbuton

    for v in variable_comida:
        v.set(0)
    for v in variable_bebida:
        v.set(0)
    for v in variable_postre:
        v.set(0)

    # limpiar el cuadro de los subtotales

    var_coste_comida.set('')
    var_coste_bebida.set('')
    var_coste_postre.set('')
    var_Subtotal.set('')
    var_Impuesto.set('')
    var_Total.set('')

# vamos a iniciar a tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1120x540+0+0')

#evitar maximizar
aplicacion.resizable(0,0)

#Titulo de la ventana
aplicacion.title('Restaurante la Maruja - SISTEMA DE FACTURACION')

#COLOR DE FONDO
aplicacion.config(bg='burlywood1')

# Panel Superior
panel_superior= Frame(aplicacion,bd=1, relief = RIDGE)
panel_superior.pack(side=TOP)

#Titulo del panel superior

etiqueta_titulo = Label(panel_superior, text='Sistema de facturación', fg = 'azure', font=('Dosis', 54),
                        bg ='burlywood3', width = 27)
etiqueta_titulo.grid(row=0, column=0)


# panel Izquierdo

panel_izquierdo = Frame(aplicacion,bd=1, relief= RIDGE)
panel_izquierdo.pack(side=LEFT)

#Panel subtotal
panel_costos = Frame(panel_izquierdo, bd=1, relief=RIDGE, bg='azure4', padx=120)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo,text="Comida", font=('Dosis',12,'bold'), bd=1,relief=RIDGE, fg='azure4')
panel_comidas.pack(side=LEFT)

#panel bebidas

panel_bebidas = LabelFrame(panel_izquierdo,text="Bebidas", font=('Dosis',12,'bold'), bd=1,relief=RIDGE, fg='azure4')
panel_bebidas.pack(side=LEFT)

#panel postres

panel_postres = LabelFrame(panel_izquierdo,text="Postres", font=('Dosis',12,'bold'), bd=1,relief=RIDGE, fg='azure4')
panel_postres.pack(side=LEFT)


# PANEL DERECHA
panel_derecha = Frame(aplicacion, bd=1, relief= RIDGE)
panel_derecha.pack(side=RIGHT)

#panel calculadora

panel_calculadora = Frame(panel_derecha,bd=1, relief=RIDGE, bg='burlywood')
panel_calculadora.pack()

#panel Recibo

panel_recibo = Frame(panel_derecha,bd=1, relief=RIDGE, bg='burlywood')
panel_recibo.pack()

#panel Botones

panel_botones = Frame(panel_derecha,bd=1, relief=RIDGE, bg='burlywood')
panel_botones.pack()

# Lista de productos
lista_comida=['Pollo','Cordero','Salmón','Merluza','Kebap','Durum','Pizza']
lista_bebida=['Agua Mineral','Cerveza','Refrescos','Zumos','Vinos Blancos','Vinos Tintos','Vinos Rosados']
lista_postres=['Tartas','Bollerias','Helados','Frutas','Turrones','Mazapanes','Roscón']

# ahora tendremos que cargar todo ello mediante un loop
# para ello utilizaremos un checkButton
#Generar variable items comida
variable_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comida:

    #crear checkbutton
    variable_comida.append('')
    variable_comida[contador]= IntVar()
    comida= Checkbutton(panel_comidas,text=comida.title(), font=('Dosis',16,'bold'), onvalue=1, offvalue= 0,
                        variable= variable_comida[contador], command=revisar_check)

    comida.grid(row = contador, column = 0, sticky=W)


    # visualizar los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Dosis', 18,'bold'), bd=1,width=6, state=DISABLED,
                                     textvariable = texto_comida[contador])
    cuadros_comida[contador].grid(row= contador, column=1)
    contador += 1

#Generar variable items bebida
variable_bebida=[]
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebida:
    # crear checkbutton
    variable_bebida.append('')
    variable_bebida[contador]= IntVar()
    bebida= Checkbutton(panel_bebidas,text=bebida.title(), font=('Dosis',16,'bold'), onvalue=1, offvalue= 0,
                        variable= variable_bebida[contador], command=revisar_check)

    bebida.grid(row = contador, column = 0, sticky=W)

    # visualizar los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador += 1



#Generar variable items postres
variable_postre=[]
cuadros_postre = []
texto_postre = []
contador= 0
for postre in lista_postres:
    # crear checkbutton
    variable_postre.append('')
    variable_postre[contador]= IntVar()
    postre= Checkbutton(panel_postres,text=postre.title(), font=('Dosis',16,'bold'), onvalue=1, offvalue= 0,
                        variable = variable_postre[contador], command=revisar_check)

    postre.grid(row = contador, column = 0, sticky=W)

    # visualizar los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1)
    contador += 1


# PANEL DE SUBTOTALES
#creamos la variables que necesitamos comida
var_coste_comida = StringVar()
var_coste_bebida = StringVar()
var_coste_postre = StringVar()
var_Subtotal = StringVar()
var_Impuesto = StringVar()
var_Total = StringVar()

#etiqueta de Comida
etiqueta_coste_comida = Label(panel_costos, text='Coste Comida', font=('Dosis', 12, 'bold'),
                              bg='azure4', fg='white')
etiqueta_coste_comida.grid(row=0, column=0)

#Cuadro de entrada
texto_coste_comida = Entry(panel_costos, font=('Dosis',12,'bold'), bd= 1, width= 10, state='readonly',
                           textvariable=var_coste_comida)
texto_coste_comida.grid(row=0, column=1, padx=41)


#etiqueta de Bebida
etiqueta_coste_bebida = Label(panel_costos, text='Coste Bebida', font=('Dosis', 12, 'bold'),
                              bg='azure4', fg='white')
etiqueta_coste_bebida.grid(row=1, column=0)

#Cuadro de entrada
texto_coste_bebida = Entry(panel_costos, font=('Dosis',12,'bold'), bd= 1, width= 10, state='readonly',
                           textvariable=var_coste_bebida)
texto_coste_bebida.grid(row=1, column=1, padx=41)


#etiqueta de Postre
etiqueta_coste_postre = Label(panel_costos, text='Coste Postre', font=('Dosis', 12, 'bold'),
                              bg='azure4', fg='white')
etiqueta_coste_postre.grid(row=2, column=0)

#Cuadro de entrada
texto_coste_postre = Entry(panel_costos, font=('Dosis',12,'bold'), bd= 1, width= 10, state='readonly',
                           textvariable=var_coste_postre)
texto_coste_postre.grid(row=2, column=1, padx=41)



#etiqueta de Subtotal
etiqueta_Subtotal = Label(panel_costos, text='Subtotal', font=('Dosis', 12, 'bold'),
                              bg='azure4', fg='white')
etiqueta_Subtotal.grid(row=0, column=2)

#Cuadro de entrada
texto_Subtotal = Entry(panel_costos, font=('Dosis',12,'bold'), bd= 1, width= 10, state='readonly',
                           textvariable=var_Subtotal)
texto_Subtotal.grid(row=0, column=3, padx=41)


#etiqueta de Impuestos
etiqueta_Impuesto = Label(panel_costos, text='Impuestos', font=('Dosis', 12, 'bold'),
                              bg='azure4', fg='white')
etiqueta_Impuesto.grid(row=1, column=2)

#Cuadro de entrada
texto_Impuesto = Entry(panel_costos, font=('Dosis',12,'bold'), bd= 1, width= 10, state='readonly',
                           textvariable=var_Impuesto)
texto_Impuesto.grid(row=1, column=3, padx=41)


#etiqueta de Total
etiqueta_Total = Label(panel_costos, text='Total', font=('Dosis', 12, 'bold'),
                              bg='azure4', fg='white')
etiqueta_Total.grid(row=2, column=2)

#Cuadro de entrada
texto_Total = Entry(panel_costos, font=('Dosis',12,'bold'), bd= 1, width= 10, state='readonly',
                           textvariable=var_Total)
texto_Total.grid(row=2, column=3, padx=41)


# botones
botones =['total','recibo','guardar','resetear']
botones_creado=[]
columnas =0
for boton in botones:
    boton = Button(panel_botones, text= boton.title(), font=('Dosis',10,'bold'), fg= 'white', bg='azure4',
                   bd=1, width= 9)

    #añadimos a la lista creada ahora
    botones_creado.append(boton)
    boton.grid(row=0, column=columnas)
    columnas +=1

#creamos el acceso a la funciones de los botones
botones_creado[0].config(command=total)
botones_creado[1].config(command=recibo)
botones_creado[2].config(command=guardar)
botones_creado[3].config(command=resetear)

# recibo
texto_recibo = Text(panel_recibo, font=('Dosis',12,'bold'), bd=1,width=40,height=14)
texto_recibo.grid(row=0,column=0)


# calculadora

visor_calculadora = Entry(panel_calculadora, font=('Dosis',14,'bold'), width= 32, bd =1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

# vamos a hacer la calculadora

botones_calculadora= ['7','8','9','+','4','5','6','-',
                      '1','2','3','x','R','Borrar','0','/']
botones_guardados =[]

#creamos una variable
fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton.title(), font=('Dosis',10,'bold'),
                    fg='white',bg='azure4',bd=1,width=10)

    botones_guardados.append(boton)

    boton.grid(row=fila, column=columna)
    if columna == 3:
        fila += 1
    columna += 1
    if columna ==4:
        columna=0

#FUNCIONALIDAD DE LA CALCULADORA

#empezamos con los botones que se va mostrar en pantalla
botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

# evitar que la ventana se cierre
aplicacion.mainloop()