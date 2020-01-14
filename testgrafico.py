#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 12:08:42 2019

@author: intel
"""

#%%
from tkinter import *

root = Tk()
#root.minsize(700,200)
root.title('WOW 1.0.0 GUI')
#root.iconbitmap('/home/intel/Desktop/Observacional/tp_final/dogeicon1.bmp')
#img = PhotoImage(file='/home/intel/Desktop/Observacional/tp_final/dogeicon1.gif')
#root.tk.call('wm', 'iconphoto', root._w, img)

entrada = Label(root,text='\n'+'W.O.W: WOW Observational Work'+'\n'+'\n'+
                '''Bienvenidx a WOW, un programa de Backup de archivos,
                Reducción de Imágenes de ciencia, Fotometría básica
                de Apertura, y Estilización de Tablas Fotométricas.'''+'\n'+
                '\n'+'Presione Ok para continuar.').grid(column=0,row=0,columnspan=2)


def menuPrincipal():
    menu = Tk()
    menu.title('WOW Menu')
    botonBackup = Button(menu,text='Backup',padx=40,state=
                         DISABLED).grid(column=0,row=0)
    botonReduc = Button(menu,text='Reducción',padx=29,state=
                         DISABLED).grid(column=1,row=0)
    botonFotom = Button(menu,text='Fotometría',padx=31,state=
                         DISABLED).grid(column=0,row=1)
    botonTabla = Button(menu,text='Tablas',padx=40,state=
                         DISABLED).grid(column=1,row=1)
    botonInfo = Button(menu,text='Info',padx=40,command=winInfo).grid(column=0,row=2)
    salir = Button(menu,text='Salir',fg='red',command=menu.destroy).grid(column=1,row=2)
    
    root.destroy()
    menu.mainloop()
    
def winInfo():
    window = Tk()
    window.title('WOW Info')
    
    infoLabel0 = Label(window,text='WOW Observational Work'+'\n',font=
                      'Helvetica 12 italic').grid(column=0,row=0,columnspan=3)
    infoLabel1 = Label(window,text='Versión:',font=
                       'Helvetica 10 bold').grid(column=0,row=1)
    infolabel2 = Label(window,text='1.1.0'+'\n').grid(column=1,row=2)
    infolabel3 = Label(window,text='Autores:',font=
                       'Helvetica 10 bold').grid(column=0,row=3)
    infolabel4 = Label(window,text='Natalia Guevara',).grid(column=1,row=4)
    infolabel5 = Label(window,text='Tomás Regna').grid(column=1,row=5)
#    infolabel6 = Label(window,text=)
#    infolabel7 = Label(window,text=)
    
    salir = Button(window,text='Salir',fg='red',command=
                   window.destroy).grid(column=2,row=6)
#    menu.destroy()
    window.mainloop()
    
   

continuar = Button(root,text='Ok',command=menuPrincipal).grid(column=0,row=1)
salir = Button(root,text='Salir',fg='red',command=root.destroy).grid(column=1,row=1)

root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    