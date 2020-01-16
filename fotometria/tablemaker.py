#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:13:03 2019

@author: natalia
"""

from astropy.table import Table,Column
import funciones.auxfunctions as aux
from astropy.io import ascii
import numpy as np
import os
from colorama import Fore
#%%
def gentable(phouts,formato='commented_header',tabesq='imagen',path=None):
    '''
     Dado uno o más archivos output de la tarea phot de IRAF, con extensión
    ",phot" y la apertura de los radios de las isofotas genera un objeto Table 
    de astropy y devuelve uno o más archivos de salida en formato ascii.
    Si se ingresan varias tablas phot tendrá que ser en formato de filelist.
    Se deberá ingresar cómo quiere que se organicen las tablas, si es una tabla
    por imagen (cada fila una estrella, con sus radios de apertura) o una tabla
    por estrella por imagen (cada fila un radio de apertura). 
    
    
        INPUT
        phouts     : Archivo .phot o lista de archivos .phot
        (path)     : camino al phouts.
        (formato)  : formato de astropy.io.ascii., por defecto usa
                     "commented_header"
        (tabfiles) : Esquema de generación de tablas. Por defecto, usa "imagen"
    '''
    
    if path is not None:
        originalpath=aux.chdir(path,save=True)
        
    formato=aux.default(formato,'commented_header')
    tabesq=aux.default(tabesq,'imagen')
    if tabesq=='estrella':
        tablestars(phouts,formato)
    elif tabesq=='imagen':
        tablesimg(phouts,formato)
        
    
    print(Fore.RED +'Tablas completas')
    if path is not None:
        aux.chdir(originalpath)
                
#%%
        
def tablestars(phouts,formato='commented_header'):
    '''
    Hace una tabla por estrella, por imagen, con todos los radios de apertura.
    '''
    if os.path.splitext(phouts)[-1] == '.phot': # si es una sola tabla
        t=Table.read(phouts,format='daophot') # lee la tabla
        nstar=len(t)  # numero de estrellas
        ncol=len(t.columns) #numero de columnas
        nrapert= (ncol-25)/8 #nro de radios de apertura.
                
        # imprimiendo por estrella en diferentes archivos
        for i in range(nstar):
            name=os.path.splitext(phouts)[0]+str(i+1)+'.tab'
            basicol=t.colnames[:25] #columnas que no dependen de r_aper
            rapcol=['SUM','AREA','FLUX','MAG','MERR','PIER','PERROR']
            aux.rm(name)
            f=open(name,'w+')
            datarows=[]
            rapert=[]
            for j in range(1,nrapert+1): # para cada r_aper
                # agrego las columnas que dependen del radio de apertura
                col=basicol + t.colnames[26+(8*(j-1)):25+8*j]
                rapert.append(t[t.colnames[25+(8*(j-1))]][i])
                datarows.append(t[col][i])
            tabla=Table(rows=datarows, names=basicol+rapcol)
            columna0=Column(name='RAPERT',data=rapert)
            tabla.add_column(columna0,0)
            ascii.write(tabla,f,format=formato)
    else:  # si es más de una tabla
            listaphot=np.genfromtxt(phouts,dtype=None)
#             hace lo mismo pero para cada objeto en una lista.
            for ph in listaphot:
                t=Table.read(ph,format='daophot')
                nstar=len(t)
                ncol=len(t.columns) 
                nrapert= (ncol-25)/8 
                for i in range(nstar):
                    name=os.path.splitext(ph)[0]+'.'+str(i)+'.tab'
                    aux.rm(name)
                    basicol=t.colnames[:25]
                    rapcol=['SUM','AREA','FLUX','MAG','MERR','PIER','PERROR']
                    f=open(name,'w+')
                    datarows=[]
                    rapert=[]
                    for j in range(1,nrapert+1):
                        col=basicol + t.colnames[26+(8*(j-1)):25+8*j]
                        rapert.append(t[t.colnames[25+(8*(j-1))]][i])
                        datarows.append(t[col][i])
                    tabla=Table(rows=datarows, names=basicol+rapcol)
                    columna0=Column(name='RAPERT',data=rapert)
                    tabla.add_column(columna0,0)
                    ascii.write(tabla,f,format=formato)


#%%
                    
def tablesimg(phouts,formato='commented_header'):
    '''
    Hace una tabla por imagen, con todas las estrellas.
    '''
    if os.path.splitext(phouts)[-1] == '.phot': 
        # si hay tabla unica
        t=Table.read(phouts,format='daophot')
        name=os.path.splitext(phouts)[0]+'.tab'
        aux.rm(name)
        f=open(name,'w+')
        ascii.write(t,f,format=formato)
    else:
        #varias tablas
        listaphot=np.genfromtxt(phouts,dtype=None)
        for ph in listaphot:
                t=Table.read(ph,format='daophot')
                name=os.path.splitext(ph)[0]+'.tab'
                aux.rm(name)
                f=open(name,'w+')
                ascii.write(t,f,format=formato)