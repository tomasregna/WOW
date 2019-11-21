#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import auxfunctions as aux
import os
import reduc
import numpy as np
#%%
def flatw(filters,listobj,path=None,mastbia=None,Dark=False,
               mastdark=None):
# =============================================================================
#      Dada una lista con los flats por filtro, realiza el masterflat en cada
#      filtro de dicha lista.
#    
#     INPUT    
#    filters    : Lista de filtros.
#    listobj    : Lista de flats por filtro.
#    (path)     : Carácteres que indica el camino a flatlist.
#    (mastbia)  : Archivo que contiene el masterbias. Por defecto usa
#                 "Zero.fits" y toma el mismo path que el flatlist.
#    (Dark)     : Si es verdadero, corrije por Dark.
#    (mastdark) : Archivo que contiene el masterdark. Por defecto usa
#                 "Dark.fits" y toma el mismo path que el flatlist.
#               
#                   ---------------------------------------      
#
#     Given a list of flats per filter, generates the masterflat for each image
#     in said filtered set.
#    
#    INPUT
#    filters    : Filter list.
#    listobj    : Flat per filter list.
#    (path)     : String that indicates the path to flatlist.
#    (mastbia)  : File that contains the masterbias. If none uses
#    (Dark)     : If true, apply Dark correction.
#                 "Zero.fits" and always use the same path as flatlist.
#    (mastdark) : File that contains the msaterdark. If none uses
#                 "Dark.fits" and always use the same path as flatlist.  
# =============================================================================

    if path is not None:
        originalpath=aux.chdir(path,save=True)    
    
    i=0
    f=open('mflatlist.in','w+')
    for x in filters:
        outfile=os.path.splitext(listobj[i])[0]+'.fits'
        f.write(outfile)
        reduc.masterflat(listobj[i],outfile,mastbia,Dark,mastdark,path)
        i=i+1
    f.close()
    
    if path is not None:
        aux.chdir(originalpath)
 #%%      
def procw(filters,listobj,path=None,mastbia=None,Dark=False,
               mastdark=None,flatin='mflatlist.in',prefix=None):
# =============================================================================
#      Dada una lista con los flats por filtro, realiza el masterflat en cada
#      filtro de dicha lista.
#    
#     INPUT    
#    filters    : Lista de filtros.
#    listobj    : Lista de imágenes por filtro.
#    (path)     : Carácteres que indica el camino al imagelist.
#    (mastbia)  : Archivo que contiene el masterbias. Por defecto usa
#                 "Zero.fits" y toma el mismo path que el flatlist.
#    (Dark)     : Si es verdadero, corrije por Dark.
#    (mastdark) : Archivo que contiene el masterdark. Por defecto usa
#                 "Dark.fits" y toma el mismo path que el flatlist.
#    (flatin)   : Lista de master flats en cada filtro.
#    (prefix)   : Prefijo que se agregará a las imágenes reducidas. Por defecto,
#                 usa "R"
#               
#                   ---------------------------------------      
#
#     Given a list of flats per filter, generates the masterflat for each image
#     in said filtered set.
#    
#    INPUT
#    filters    : Filter list.
#    listobj    : Image per filter list.
#    (path)     : String that indicates the path to imagelist.
#    (mastbia)  : File that contains the masterbias. If none uses
#    (Dark)     : If true, apply Dark correction.
#                 "Zero.fits" and always use the same path as flatlist.
#    (mastdark) : File that contains the msaterdark. If none uses
#                 "Dark.fits" and always use the same path as flatlist.  
#    (flatin)   : Flat per filter list.
#    (prefix)   : Prefix added to the reduced image list. If none, uses "R".
# =============================================================================  
    if path is not None:
        originalpath=aux.chdir(path,save=True)    
    
    flatlist=np.genfromtxt(flatin)

    i=0
    for x in filters:
        #outfile=os.path.splitext(listobj[i])[0]+'.fits'
        image='@'+listobj[i]
        flat=flatlist[i]
#        if 
        reduc.process(image,path,Dark,mastbia,mastdark,flat,prefix)        
        i=i+1
        
    if path is not None:
        aux.chdir(originalpath)
       
