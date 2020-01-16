#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:45:15 2019

@author: intel
"""
#%%
import os
from pyraf import iraf
import funciones.auxfunctions as aux
import numpy as np

#%%
def unisf(image,fwhm,sigma,thold,zmin='INDEF',zmax='INDEF',
               path=None,outfile=None):
    '''
     Dada una lista de imágenes, identifica las estrellas de campo y
     genera un archivo de coordenadas.

      INPUT
      image     : Archivo .in con los nombres de las imágenes, o la imagen 
                  simple.
      fwmh      : Ancho a mitad de intensidad máxima de las estrellas.
      sigma     : Desviación estándar del cielo.
      thold     : Amplitud mínima por encima del valor de fondo.
      (zmin)    : Valor mínimo de cuentas a considerar.
      (zmax)    : Valor máximo de cuentas a considerar.
      (path)    : String que indica el camino a la imagen.
      (outfile) : Nombre del archivo de salida. Por defecto usa el nombre de
                  la imagen y agrega un .coo .
                  
                   ---------------------------------------      

      Given a images list, identifies field stars and generates a coordinates
      file.
    
      INPUT
      image     : .in file with the name of each image, or a single image. 
      fwmh      : Full width half maximum of intensity of stars.
      sigma     : Standard deviation of the sky.
      thold     : Minimum amplitude above background level.
      (zmin)    : Minimum counts value to consider.
      (zmax)    : Maximum counts value to consider.
      (path)    : String that indicates the path do the images.
      (outfile) : Name of the output file, including .coo. By default, uses 
                  image name and adds .coo extension.
    '''
    if path is not None:
        originalpath=aux.chdir(path,save=True)
    
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
    
    aux.default(outfile,image+'.coo',borrar=True)
    
    iraf.daofind.output=outfile
    iraf.daofind.image=image
    iraf.daofind()
        #execute iraf task 'daofind' 
    if path is not None:
        aux.chdir(originalpath)

#%% 
def multisf(imagelist,farr,sarr,thold,zmin=None,zmax=None,
            path=None,outfile=None):     
    if path is not None:
        originalpath=aux.chdir(path,save=True)        
    listaim=np.genfromtxt(imagelist,dtype=None)
    
    if zmin is None:
        zmin=[]
        for im in listaim:
            zmin.append('INDEF')
    
    if zmax is None:
        zmax=[]
        for im in listaim:
            zmax.append('INDEF')
        
    if outfile is None :
        outfile=[]
        for im in listaim:
            imn=os.path.splitext(im)[0]
            aux.rm(imn+'.coo') #delete all previous coord files if exist
            outfile.append(imn+'.coo')
    f=open('coords.in','w+')
    for out in outfile:
      print >> f,out
    f.close()
    i=0
    for im in listaim:
        unisf(im,farr[i],sarr[i],thold,zmin[i],zmax[i],
           path,outfile[i])
        i=i+1
    if path is not None:
        aux.chdir(originalpath)
