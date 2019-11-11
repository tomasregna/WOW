#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:09:36 2019

@author: guevaran
"""
#%%

import os
from pyraf import iraf
import auxfunctions as aux
#os.system('ds9 -fifo dev/imt1 &')


#%%
def photom(images,coords,anillo,danillo,apertura,outfile=None,path=None)
    # ==================================================================
    #  Dada una lista de imágenes, realiza la fotometría de apertura con
    #  la tarea phot.
    #  
    #  INPUT
    #  images   : Lista de imágenes .in o archivo .fits
    #  coords   : Archivo con las coordenadas de los objetos.
    #  anillo   : ?
    #  danillo  : ??
    #  apertura : Apretura de los radios, ingresada como una lista,
    #            ej: [.5]+range(1,31) 
    #  (outfile): Nombre de archivo(s) de salida.
    #  (path)   : Línea que indica el camino al directorio de archivos.
    #
    # ------------------------------------------------------------------
    #
    #  Given a image list, performs aperture photometry via phot task.
    #
    #  INPUT
    #  images   : .in image list or .fits file.
    #  coords   : file with objects' coordinates.
    #  anillo   : ?
    #  danillo  : ??
    #  (outfile): Name of the output file(s).
    #  (path)   : String that indicates the path to the files.
    #
    # ==================================================================
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
#    setea parámetros de la fotometría
    iraf.datapars.obstime="time-obs"
    iraf.fitskypars.annulus=anillo  # radio del anillo interior (cuentas obj - cuentas d cielo)
    iraf.fitskypars.dannulus=danillo  # radio del anillo exterior(cuentas cielo)
    iraf.photpars.apertures= apertura # intervalo de radios a tomar
    iraf.phot.interac='no'
    
    
    
    if (os.path.splitext(images)[-1] == '.fit' or
        os.path.splitext(images)[-1] == '.fits'):
        iraf.phot.image=images
        iraf.phot.coords=coords
        aux.default(outfile,os.path.splitext(images)[0]+'.phot',rm=True)        
        iraf.phot.output=outfile
    else:
        
        iraf.phot.image='@'+images
        iraf.phot.coords='@'+coords
        aux.default(outfile,images+'.phot',rm=True)
        imagelista=np.genfromtxt(images,dtype=None)
        f=open(outfile,'a+')
        for im in imagelista :
            f.append(os.path.splitext(im)[0]+'.phot')
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
