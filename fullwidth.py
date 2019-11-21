#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:57:23 2019

@author: guevaran
"""
import numpy as np
import auxfunctions as aux
#%%

def fullwidth(obser,binning=1,RF=False):
    '''
    Dado el telescopio que se esté usando (HSH o JS), usando el valor medio
    del seeing en casleo da un estimado del FWHM. Se puede ingresar el binning
    que se utiliza .
    Contempla el caso de que se use, en el JS, el reductor focal.
    '''
    seeing=2.5 #seeing promedio de casleo en "
    if obser=='HSH' :
        escala= 0.5424 #  arcsec/pix
    elif obser=='JS':
        if not RF:
            escala= 0.15  #  arcsec/pix
        else:
         escala= 0.45  #  arcsec/pix
    
    full=seeing/(escala*binning)
    return full
#%%
def multifull(images,obser,path=None,RF=False):
    if path is not None:
        originalpath=aux.chdir(path,save=True)
    
    images=np.genfromtxt(images,dtype=None)
    fwhm=[]
    for im in images:
       binn=aux.hselect(im,'CCDSUM') # gets binning of the image
       binn=binn[0]  # access element 0 of the array
       binn=binn[1]  # access first character
       binn=int(binn)  # converts string to integer
       fwhm.append(fullwidth(obser,binn,RF))
      
        
    if path is not None:
        aux.chdir(originalpath)
    return(fwhm)