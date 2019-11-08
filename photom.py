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
def photom(images,coords,anillo,danillo,outfile=None,path=None)
    # ==================================================================
    #  Dada una lista de imágenes, realiza la fotometría de apertura con
    #  la tarea phot.
    #  
    #  INPUT
    #  images   : Lista de imágenes .in o archivo .fits
    #  coords   : Archivo con las coordenadas de los objetos.
    #  anillo   : ?
    #  danillo  : ??
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

    iraf.datapars.ccdread="rdnoise"
    iraf.datapars.gain="gain"
    iraf.datapars.exposure="exptime"
    iraf.datapars.airmass="airmass"
#    iraf.datapars.filter="filter"
    iraf.datapars.obstime="time-obs"
    iraf.fitskypars.annulus=anillo
    iraf.fitskypars.dannulus=danillo
    iraf.photpars.apertures="0.5,1:30:1" #no quiero tocar y arruinar esto aaaaa
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
        imagelista=np.genfromtxt(images,dtype=None)
        f=open(images+'.phot','a+')
        for im in imagelista :
            f.append(os.path.splitext(im)[0]+'.phot')
            aux.rm(os.path.splitext(im)[0]+'.phot')
        f.close()
        aux.default('@'+outfile,'@'+images+'.phot',rm=True)
        iraf.phot.output=outfile
    
    
    iraf.phot()

#%%
    if (os.path.splitext(images)[-1] == '.fit' or
        os.path.splitext(images)[-1] == '.fits'):
        with open(coords) as fp:
            for curline in fp:
            # check if the current line
            # starts with "#"
                if curline.startswith("#"): #if it's a commented line
                    continue #do nothing
                else:         
                    line = fp.readline() #initialize reading
                    cnt = 1
                    while line:
                        #print("Line {}: {}".format(cnt, line.strip()))
                        #eso puede servir para comprimir los dos for en
                        #uno solo, pero no sé como jeje... pronto pronto...
                        line = fp.readline()
                        cnt += 1 #count how many lines -stars- in coords file.
        fp.close()
        
        for i in range(0,cnt+1): #to include last one, add one
            name=os.path.splitext(images)[0]+'.'+str(i)+'.tab'
            aux.rm(name)
            f=open(name,'w+')
            for j in range(1,32): #a partir de aca no entiendo, pero te creo que esta bien...
                fields="Id,Rapert["+str(j)+"],Mag["+str(j)+"],Merr["+str(j
                                 )+"],Area["+str(j)+"],Flux["+str(j
                                 )+"],Annulus,Dannulus,MSky,Stdev,NSky,Sum["+str(j
                                 )+"],XCenter,YCenter" 
                iraf.txdump.fields=fields
                test=iraf.txdump(outfile,expr="Id == "+str(i),headers='no',Stdout=1)
                print >> f,test[0] #??? wat
            f.close()
    else :
        print 'to be continued...'
        
    if path is not None:
        aux.chdir(originalpath)
#%%
