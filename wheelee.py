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
#%%
def flatw(filters,listobj,path=None,mastbia=None,Dark=False,
               mastdark=None,edit=False):
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
#    (edit)     : En caso de que sea verdadero, edita el header de las
#                 imágenes para agregarles el tipo "flat".
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
#    (edit)     : If true, edits the header of the images, changing imagetyp    
#                 to "flat".
# =============================================================================

    if path is not None:
        originalpath=aux.chdir(path,save=True)    
    
    i=0
    f=open('mflatlist.in','a+')
    for x in filters:
        outfile=os.path.splitext(listobj[i])[0]+x+'.fits'
        f.append(outfile)
        reduc.masterflat(listobj[i],outfile,mastbia,Dark,mastdark,edit,path)
        i=i+1
    f.close()
    
    if path is not None:
        aux.chdir(originalpath)
       
def procw(filters,listobj,path=None,mastbia=None,Dark=False,
               mastdark=None,mflatlist='mflatlist.in',edit=False,output=None):
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
#    (mflatlist): Lista de master flats en cada filtro.
#    (edit)     : En caso de que sea verdadero, edita el header de las
#                 imágenes para agregarles el tipo "flat".
#    (output)   : tbd
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
#    (mflatlist): Flat per filter list.
#    (edit)     : If true, edits the header of the images, changing imagetyp    
#                 to "flat".
#    (output)   : tbd
# =============================================================================  
    if path is not None:
        originalpath=aux.chdir(path,save=True)    
    
    listaflat=np.genfromtxt(mflatlist,dtype=None)
    listaimag=np.genfromtxt(images,dtype=None)
    
    i=0
    for x in filters:
        #outfile=os.path.splitext(listobj[i])[0]+'.fits'
        reduc.process(imagelist=listaimag[i],path,Dark,mastbia,mastdark
                ,mastflat=listaflat[i],edit,output)        
        i=i+1
        
    if path is not None:
        aux.chdir(originalpath)
       