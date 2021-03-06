#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:09:36 2019

@author: guevaran
"""
#%%

import os
from pyraf import iraf
import funciones.auxfunctions as aux
import numpy as np


#%%
def photom(images,anillo,danillo,apertura,outfile=None,path=None,coords='coords.in'):
    '''
      Dada una lista de imágenes, realiza la fotometría de apertura con
      la tarea phot.
      
      INPUT
      images   : Lista de imágenes .in o archivo .fits
      (coords)   : Archivo con las coordenadas de los objetos, por defecto
                       es "coords.in"
      anillo   : radio annulus
      danillo  : radio dannulus
      apertura : Apretura de los radios, ingresada como un string
                    ej: r1,r2:rn-1,rn
      (outfile): Nombre de archivo(s) de salida. por defecto es el nombre de
      images en extension phot
      (path)   : Línea que indica el camino al directorio de archivos.
    
     ------------------------------------------------------------------
    
      Given a image list, performs aperture photometry via phot task.
    
      INPUT
      images   : .in image list or .fits file.
      coords   : file with objects' coordinates.
      anillo   : ?
      danillo  : ??
      (outfile): Name of the output file(s).
      (path)   : String that indicates the path to the files.
    
    '''
    if path is not None:
        originalpath=aux.chdir(path,save=True)

    iraf.noao()
    iraf.digiphot()
    iraf.apphot()
    iraf.unlearn(iraf.datapars)
    iraf.unlearn(iraf.fitskypars)
    iraf.unlearn(iraf.photpars)
    iraf.unlearn(iraf.phot) #eterno resplandor de una tarea sin recuerdos
#  serie de comandos que indican el campo del header donde ir a buscar info
    iraf.datapars.ccdread="rdnoise"
    iraf.datapars.gain="gain"
    iraf.datapars.exposure="exptime"
    iraf.datapars.airmass="airmass"
    iraf.datapars.filter="filtnew"
    iraf.datapars.obstime="time-obs"

 #    setea parámetros de la fotometría   
    iraf.fitskypars.annulus=anillo  # radio del anillo interior (cuentas obj - cuentas d cielo)
    iraf.fitskypars.dannulus=danillo  # radio del anillo exterior(cuentas cielo)
#    iraf.photpars.apertures="0.5,1:30:1"
    iraf.photpars.apertures= apertura # intervalo de radios a tomar
    iraf.phot.interac='no'
    iraf.phot.verify='no'
    iraf.phot.verbose='no'
    
    
    
    if (os.path.splitext(images)[-1] == '.fit' or
        os.path.splitext(images)[-1] == '.fits'):
        iraf.phot.image=images
        iraf.phot.coords=coords
        outfile=aux.default(outfile,os.path.splitext(images)[0]+'.phot',borrar=True)        
        iraf.phot.output=outfile
    else:
        
        iraf.phot.image='@'+images
        iraf.phot.coords='@'+coords
        outfile=aux.default(outfile,os.path.splitext(images)[0]+'_phots.in',borrar=True)
        imagelista=np.genfromtxt(images,dtype=None)
        f=open(outfile,'a+')
        for im in imagelista :
            f.write(os.path.splitext(im)[0]+'.phot'+'\n')
            aux.rm(os.path.splitext(im)[0]+'.phot')
        f.close()  
        iraf.phot.output='@'+outfile
    
    
    iraf.phot()

#%%
# contador de cantidad de filas en un archivo -sin contar los comentarios-
#    if (os.path.splitext(images)[-1] == '.fit' or
#        os.path.splitext(images)[-1] == '.fits'):
#        with open(coords) as fp:
#            for curline in fp:
            # check if the current line
            # starts with "#"
#                if curline.startswith("#"): #if it's a commented line
#                    continue #do nothing
#                else:         
#                    line = fp.readline() #initialize reading
#                    cnt = 1
#                    while line:
                        #print("Line {}: {}".format(cnt, line.strip()))
                        #eso puede servir para comprimir los dos for en
                        #uno solo, pero no sé como jeje... pronto pronto...
 #                       line = fp.readline()
 #                       cnt += 1 #count how many lines -stars- in coords file.
 #       fp.close()               
    if path is not None:
        aux.chdir(originalpath)
#%%
