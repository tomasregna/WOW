#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:57:05 2019

@author: intel
"""

#%%
from tkinter import *

root = Tk() #algo que hay que poner primero, siempre... 
            #... es como plantarse en la tarea de iraf ahre

''' en tkinter son siempre 2 pasos:
    1. crear un widget
    2. plasmarlo en pantalla
'''

myLabel = Label(root, text='Hello World') 
#asignar a myLabel,un texto que diga hello world
#se hace llamando simplemente a Label del paquete tkinter

#hay 2 maneras de poner por pantalla algo... una es pack,
#la otra luego

'''
Otro asunto importante es a dónde ponemos todo lo que vayamos a
hacer... al seleccionar root, elegimos disponer lo que sea que haga
dicha acción, en el root -algo así como en la base- del widget
que crearemos
'''

myLabel.pack() #mostrarlo en pantalla

'''
ahora hay que hacer un eventloop... te preguntarás que cornos
es un eventloop... bueno, acá va: estos programas para 
interpretar lo que están haciendo, están constantemente en un 
loop -creo que- para estar actualizados constantemente

Dado que está en loop todo el tiempo, identifica, por ejemplo,
a donde está tu mouse...

Normalmente un programa termina cuando termina el loop; además,
el loop sigue y sigue y sigue hasta que algo ocurra. En este caso,

Queremos crear un root:
'''

root.mainloop() #parece ser que esto abre el loop...

#cuando cerras el widget, se interrumpe el loop ---> 
# ---> sale del programa!

#%%
from tkinter import *

'''
En el anterior ejemplo, hay un string impreso arriba de todo, que no
sufre ningún cambio tras ampliar, estirar, achicar, y demás acciones
sobre el widget... Probemos con el sistema de grilla -grid-, que nos
va a permitir jugar con este esquema, con las columnas y demás.

En vez de trabajar con el pack, veamos cómo funciona el sistema de
grid.
'''

root = Tk()

myLabel1 = Label(root, text='Hello World')
myLabel2 = Label(root, text='Me llamo Tomás')

myLabel1.grid(row=0, column=0) #usamos el grid en vez de pack
#además, es python... asi que arranca de cero
myLabel2.grid(row=1, column=1)

'''
vemos claramente al correrlo, que no se queda en el centro, si
jugamos con el tamaño del widget! Siempre se queda donde le
indicamos, fila cero col cero, y fila 1 col 1

Ahora bien... si intentamos ponerle columna 5, el tkinter
es inteligente... lo va a dejar en la columna 1, porque funciona
de manera relativa -no entiende facilmente que es o no una columna-

Hay maneras más sofisticadas de mejorar esto, pero es lo más
básico que hay al respecto por ahora.
'''

root.mainloop()

#%%
from tkinter import *

root = Tk()

'''
Hay otra sintaxis posible, más bizarra, pero que funciona; es más
compacta, porque comprime la creación y la muestra en pantalla del
widget en una sola acción!

esquemáticamente, es algo así como crear(algo).mostrar(algo)
'''

myLabel1 = Label(root, text='Hello World').grid(row=0, column=0)
myLabel2 = Label(root, text='Me llamo Tomás').grid(row=1, column=1)
# podemos agregar columnspan=nro para indicar cuantas columnas ocupa algo 
#en particular

#y funciona exactamente igual...

root.mainloop()

#%%
from tkinter import *

root = Tk()

'''
Ahora... Botones!!!

para agregar uno, llamamos a Button, de tkinter
'''

myButton1 = Button(root, text='Hacé click!')
#nuevamente, lo creamos

myButton1.pack() #y lo mostramos en pantalla...

#este botón es medio triste, no hace nada porque
#no le asignamos nada, solo algo de texto básico.

myButton2 = Button(root, text='Hacé click!', state= DISABLED)
myButton2.pack()
#se puede agregar un botón que por defecto, esté desactivado!
# agregando un state=DISABLED

myButton3 = Button(root, text='Click', padx=50)
myButton3.pack()
# se le puede modificar también el tamaño del botón, con agregar
# padx=nro y pady=nro para variar los ejes...

root.mainloop()

#%%
from tkinter import *

root = Tk()

'''
Una pregunta válida es, ¿cómo darle utilidar a este botón?
Hay que darle una función... entonces, definamos una:
'''

def myClick():
    myLabel = Label(root, text='Lindo click metiste crack!')
    #la funcion agrega simplemente un texto
    #en pantalla
    myLabel.pack() #mostrar en pantalla

myButton1 = Button(root, text='Hacé click!',command=myClick)
#para decirle que ejecute algo, le asignamos la función como un
#comando del botón.
'''
OJO: al poner el comando = algunafunción, NO LE AGREGAMOS EL
PARÉNTESIS; no va a correr bien, no vas a saber por qué

osea: command = func() está MAL
      command = func está BIEN
      
¿Y cómo le pasamos un argumento de la función? Escribiendo la
sintaxis de Lambda:
    ...command=Lambda: myClick(argumento) y listo! 
'''
#se pueden cambiar los colores, fg='blue' pinta las letras de azul
# bg='red' pinta el fondo del botón de rojo...
myButton2 = Button(root, text='Hacé click!', fg='blue')
myButton3 = Button(root, text='Hacé click!', bg='red')

myButton1.pack()
myButton2.pack()
myButton3.pack()

root.mainloop()

#%%
from tkinter import *

root = Tk()

e1 = Entry(root) #podemos armar entradas de texto simples!
e1.pack() #y mostrarlo COMO SIEMPRE

#y agregarle cosas piolas, como cambiarle el largo, etc etc
# y demás chucherías como el color de letra, de fondo, bla bla...
e2 = Entry(root, width=50)
e2.pack()
#y al correrlo vemos que es muuuuuucho más largo

#el borde también puede variarse:
e3 = Entry(root, borderwidth=5)
e3.pack()
#y se ve bastante grueso

#e3.delete(0, END) borra lo que esté en la entrada!

root.mainloop()

#%%
from tkinter import *

root = Tk()

'''
Bien, la pregunta natural es... ¿cómo le damos utilidad el entry?
Hay una opción elegante, que pide -get- lo que le escriba de
entrada.

Vamos a armar una función myName, que agarre lo que esté escrito
en el entry, vía e1.get(), y que ese texto lo imprima en el widget
cada vez que se llama a la función.

Y para llamar a la función, ponemos un botón que llama a myName 
cada vez que hagamos click!
'''
e1 = Entry(root)
e1.pack()
#se puede agregar e1.insert(0, 'Ingrese su nombre: '), que está por
#defecto en el texto, y lo tendría que borrar y luego poner mi
#nombre... como en muchas webs donde piden usuario -al menos en las
#webs viejas-...

def myName():
    myLabel = Label(root, text=e1.get())
    #notar que para el label, las funciones sí van con el paréntesis
    #... el único gorra es el command por ahora ¬¬
    myLabel.pack()

def mySalute():
    holis = 'Holis ' + e1.get()
    myLabel = Label(root, text=holis)
    #y si, pueden definirse variables por fuera, para evitar que 
    #termine siendo kilométrico el asunto...
    myLabel.pack()

myButton1 = Button(root, text='Di tu nombre', command=myName)
myButton1.pack()
myButton2 = Button(root, text='Saludá', command=mySalute)
myButton2.pack()

root.mainloop()

#%%
from tkinter import *

root = Tk()
root.title('Título del Widget') #adiviná qué hace esto...

root.mainloop()