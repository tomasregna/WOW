#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:46:46 2019

@author: guevaran
"""

from pyraf import iraf
import auxfunctions as aux
import numpy as np
import os

#%%

def filtersep(images,path=None,field='FILTER'):
# =============================================================================
#     
#    Dada una lista de imágenes y el parámetro del header de las mismas, busca
#    el flitro de cada imágen, las separa por filtro en listas, en archivos
#    distintos.
#    Devuelve una lista de todos los filtros de las imágenes.
#    
#       INPUT
#       images   : Archivo .in con los nombres de las imágenes.  
#       (path)   : Camino al archivo images
#       (field)  : Campo del header que contiene la información del filtro,
#                    por defecto utiliza el campo "FILTER"
#        
#       OUTPUT
#        name       type    
#  listadefiltros   nparray  : Lista de filtros en las imágenes.
#  listadearchivos  list     : Lista de archivos de lista que generó la tarea. 
#                   ---------------------------------------      
# =============================================================================

    if path is not None:
        originalpath=aux.chdir(path,save=True)
        
        
    #   le agrego un arroba
    # para pasarlo como argumento en iraf 
    imagesl='@'+images
                                    # genera lista de todos los filtros
    listafull = iraf.hselect(imagesl,fields=field,expr = "yes",Stdout=1)
    listadefiltros = np.unique(listafull) # separa individualmente x filtro
    
     # me genero una lista de las imágenes
    listaimagenes = np.genfromtxt(images,dtype=None)
    
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
            x=iraf.hselect(im,fields=field,expr = "yes",Stdout=1)
            if x[0] in f:  # lo compara con el filtro que estoy buscando
                print >> h, im # si es igual lo guarda en la lista
        h.close()

    if path is not None:
        aux.chdir(originalpath)

    return listadefiltros,listadearchivos
