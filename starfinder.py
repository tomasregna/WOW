#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:45:15 2019

@author: intel
"""
#%%
import os
from pyraf import iraf
import auxfunctions as aux

#%%
def starfinder(image,outfile=None,fwhm,sigma,zmin='INDEF',zmax='INDEF',
               thold,path=None):
# =============================================================================
#     Dada una lista de imágenes, identifica las estrellas de campo y
#     genera un archivo de coordenadas.
#
#      INPUT
#      image     : Archivo .in con los nombres de las imágenes, o la imagen 
#                  simple.
#      fwmh      : Ancho a mitad de intensidad máxima de las estrellas.
#      sigma     : Desviación estándar del cielo.
#      thold     : Amplitud mínima por encima del valor de fondo.
#      (zmin)    : Valor mínimo de cuentas a considerar.
#      (zmax)    : Valor máximo de cuentas a considerar.
#      (path)    : String que indica el camino a la imagen.
#      (outfile) : Nombre del archivo de salida. Por defecto usa el nombre de
#                  la imagen y agrega un .coo .
#                  
#                   ---------------------------------------      
#
#      Given a images list, identifies field stars and generates a coordinates
#      file.
#    
#      INPUT
#      image     : .in file with the name of each image, or a single image. 
#      fwmh      : Full width half maximum of intensity of stars.
#      sigma     : Standard deviation of the sky.
#      thold     : Minimum amplitude above background level.
#      (zmin)    : Minimum counts value to consider.
#      (zmax)    : Maximum counts value to consider.
#      (path)    : String that indicates the path do the images.
#      (outfile) : Name of the output file, including .coo. By default, uses 
#                  image name and adds .coo extension.
#
# =============================================================================
    iraf.noao() #loads noao
    iraf.digiphot() #loads digiphot
    iraf.apphot() #loads apphot
    
    iraf.unlearn(iraf.daofind)
    iraf.unlearn(iraf.datapars)
    iraf.unlearn(iraf.findpars) #unlearns every task required
    
    iraf.datapars.fwhmpsf = fwhm
    iraf.datapars.sigma = sigma
    iraf.datapars.datamin = zmin
    iraf.datapars.datamax = zmax #sets meaningful parameters 
    
    iraf.findpars.thresho = thold #sets meaningful threshold
    
    iraf.daofind.verify="no" #avoid checking parameters given 
    
    if path is not None:
        originalpath=aux.chdir(path,save=True)
        

    if (os.path.splitext(image)[-1] == '.fit' or
        os.path.splitext(image)[-1] == '.fits'):
        aux.default(outfile,image+'.coo',rm=True)
        #if single image, delete pre-existing coord files and if no output is
        #given, generate a file with default output scheme.
    else:    #if image input is a file list
        if outfile is None :
            aux.rm(image+'.coo') #delete .in.coo list if already exists
            f=open(image+'.coo','a+')
            imagelista=np.genfromtxt(image,dtype=None)
            for im in imagelista:
                f.append(im+'.coo')
                aux.rm(im+'.coo') #delete all previous coord files if exist
            f.close()
            outfile='@'+image+'.coo'
            # if there's no defined output, generates a .in list with 
            #default output scheme.
        else :
            outfile='@'+outfile #adds @ to help iraf recognize the list
        image = '@'+image
        
    iraf.daofind.output=outfile
    iraf.daofind.image=image
    iraf.daofind()
        #execute iraf task 'daofind' 
    if path is not None:
        aux.chdir(originalpath)
