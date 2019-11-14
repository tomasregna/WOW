#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:46:46 2019

@author: guevaran
"""

import auxfunctions as aux
import numpy as np
import os
from pyraf import iraf

#%%

def filtersep(images,path=None,field='FILTER02'):
# =============================================================================
#     
#    Dada una lista de imágenes y el parámetro del header de las mismas, busca
#    el flitro de cada imágen, las separa por filtro en listas, en archivos
#    distintos.
#    Devuelve una lista de todos los filtros de las imágenes.
#    Por defecto interpreta que se están tomando datos con el telescopio
#    de 2.15m de CASLEO, con su respectivo formato: "(N) X" donde N es un
#    número asociado a filtro X, que se encuentra en el campo "FILTER02" del 
#    header de la imagen. Si lo encuentra en free usa el "FILTER01". 
#    
#       INPUT
#       images   : Archivo .in con los nombres de las imágenes.  
#       (path)   : Camino al archivo images
#       (field)  : Campo del header que contiene la información del filtro,
#                    por defecto utiliza el campo "FILTER02"
#        
#       OUTPUT
#        name       type    
#  listadefiltros   nparray  : Lista de filtros en las imágenes.
#  listadearchivos  list     : Lista de archivos de lista que generó la tarea. 
#                   ---------------------------------------      
# =============================================================================

    if path is not None: # moves to path, saves working directory
        originalpath=aux.chdir(path,save=True)
        
        
    #   le agrego un arroba
    # para pasarlo como argumento en iraf 
    imagesl='@'+images
                                   
    listafull = aux.hselect(imagesl,field) # genera lista de todos los filtros       
#     excluyo el filtro 1 que es ningùn filtro.
    j=0
    for x in listafull: 
        if "(1)" in x: #    excluyo los filtros free:
            listafull.remove(j)
        j=j+1
    
    listafull2= aux.hselect(imagesl,"FILTER01") # busco los filtros 1
    j=0
    for x in listafull2:
        for h in [1,2,4,5]:
            if "("+str(h)+")" in x:
                print 'santitopo'
                listafull2.pop(j)
        j=j+1
    # separa individualmente x filtro
    listadefiltros = np.unique(listafull+listafull2) 
   
      # me genero una lista de las imágenes
    listaimagenes = np.genfromtxt(images,dtype=None)
    
    i=0
    for filt in listadefiltros:
        filt = filt.strip()[-2] # se queda con el último carácter
        listadefiltros[i]=filt # lo guarda en listadefiltros
        i=i+1
       
#         A cada imagen le asigna un nuevo valor en el header que contiene
#         el filtro de cada imagen, en el formato de un solo caracter.
    for im in listaimagenes:
        x=aux.hselect(im,field)  # obtengo el filtro, lo guardo en un array x
        y=aux.hselect(im,"FILTER01")
        orfilt=x[0] # separo el elemento único del array
        orfilt2=y[0]
        if not ("(1)" in orfilt):
            orfilt=orfilt.strip()[-2] # me quedo con el último carácter no blanco.
            aux.hedit(im,fields="FILTNEW",value=orfilt)  
        else:
            orfilt2=orfilt2.strip()[-2]
            aux.hedit(im,fields="FILTNEW",value=orfilt2) 
        
    #genera lista vacia de archivos
    listadearchivos=[]
    #guarda el nombre del archivo input
    imagename=os.path.splitext(images)[0]
    
    for f in listadefiltros: # por cada filtro
        
        #genera un nuevo nombre de archivo .in
        if type(f) == str:
            newf=imagename+f+'.in'
        else:
            newf=imagename+str(f)+'.in'
        
        # los agrega a la lista de archivos
        listadearchivos.append(newf)
        
        #crea el archivo
        h=open(newf,'w+')
        
        # para cada imagen
        for im in listaimagenes:
            #agarra el filtro
            x=aux.hselect(im,"FILTNEW")
            if x[0].strip() in f:  # lo compara con el filtro que estoy buscando
                print >> h, im # si es igual lo guarda en la lista
        h.close()

    if path is not None:
        aux.chdir(originalpath)

    return listadefiltros,listadearchivos

#%%
def filtersep2(images,path=None,field='FILTER02'):    
    imagesl='@'+images

    if path is not None: # moves to path, saves working directory
        originalpath=aux.chdir(path,save=True)    
                               
    listafull = aux.hselect(imagesl,field)
    imagelist= np.genfromtxt(images,dtype=None)
    
    j=0
    filt=[]
    for x in listafull:
        var=str(x)[-2]
        filt.append(var)
        aux.hedit(imagelist[j],fields="FILTNEW",value=var)
        j=j+1
    
    filt1=np.unique(filt)
    
    listadearchivos=[]
    for f in filt1:
        filterfile=os.path.splitext(images)[0]+f+'.in'
        aux.rm(filterfile)
        listadearchivos.append(filterfile)
        
        h=open(filterfile,'w+')
        
        # para cada imagen
        for im in imagelist:
            #agarra el filtro
            x=aux.hselect(im,"FILTNEW")
            if x[0].strip() in f:  # lo compara con el filtro que estoy buscando
                print >> h, im # si es igual lo guarda en la lista
        h.close()
    
    if path is not None:
        aux.chdir(originalpath)
    
    return filt1,listadearchivos
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    