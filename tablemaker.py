#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:13:03 2019

@author: natalia
"""

from astropy.table import Table
import auxfunctions as aux
from astropy.io import ascii
import numpy as np

#%%
def gentable(phouts,path=None,apertura):
    
    if path is not None:
        originalpath=aux.chdir(path,save=True)
# =============================================================================
#     lo hice para que en principio tirara todas las columnas de la tabla
#     mi idea es que no sea así, sino que te imprima opciones y elijas qué
#    querés que tire.
#     además (ida para ver 2.0) poder peedir que imprima por imagenes
#    (solo valido para ciertos parametros que no dependen del r_aper)
# =============================================================================
    
    if os.path.splitext(phouts)[-1] == '.phot': # si es una sola tabla
        t=Table.read(phots,format='daophot') # lee la tabla
        nstar=len(t)  # numero de estrellas
                
        # imprimiendo por estrella en diferentes archivos
        for i in range(nstar):
            name=os.path.splitext(phouts)[0]+'.'+str(i)+'.tab'
            aux.rm(name)
            f=open(name,'w+')
            
            for j in range(1,len(apertura)+1): # para cada r_aper
                basicol=t.colnames[:25] #columnas que no dependen de r_aper
                # agrego las columnas que dependen del radio de apertura
                col=basicol + t.colnames[25+(8*(i-1)):25+8*i]
                
                taux=t[col][i] # tabla auxiliar
                
                ascii.write(taux,f,format='no_header') #imprime a archivo
                
    else:  # si es más de una tabla
            listaphot=np.genfromtxt(phouts,dtype=None)
#             hace lo mismo pero para cada objeto en una lista.
            for ph in listaphot:
                t=Table.read(ph,format='daophot')
                nstar=len(t)
                for i in range(nstar):
                    name=os.path.splitext(ph)[0]+'.'+str(i)+'.tab'
                    aux.rm(name)
                    f=open(name,'w+')
                    for j in range(1,len(apertura)+1):
                        basicol=t.colnames[:25] 
                        col=basicol + t.colnames[25+(8*(i-1)):25+8*i]
                        taux=t[col][i]
                        ascii.write(taux,f,format='no_header')




    if path is not None:
        aux.chdir(originalpath)
                
                