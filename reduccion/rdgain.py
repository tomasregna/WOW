#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:21:49 2020

@author: natalia
"""
import numpy as np 
from pyraf import iraf
import os
#%%
import funciones.auxfunctions as aux
#%%
def telescopefinder(image,path=None):
    if path is not None:
        originalpath=aux.chdir(path,save=True)
    a=os.path.splitext(image)[-1]
 
    if a=='.fit' or a=='.fits':
    
        telfield=aux.hselect(image,'TELESCOP')
        if 'HSH' in telfield:
            telescopio='HSH'
        else:
            telescopio='JS'
    else:
        lista=np.genfromtxt(image,dtype=None)
        im=lista[0]
        telfield=aux.hselect(im,'TELESCOP')
        if 'HSH' in telfield:
            telescopio='HSH'
        else:
            telescopio='JS'     
            
    if path is not None:
        aux.chdir(originalpath)
    return telescopio

#%% 
def rdngn(image):
    
    tel=telescopefinder(image)    
    gain=aux.hselect(image,'gain')
    gain=gain[0]
    jsgain=('1.12','2.18','4.20')
    jsrd=(2.7,3.14,4.29)
    if tel == 'JS':
        rdn=jsrd[int(gain)-1]
        gn=jsgain[int(gain)-1]
    elif tel=='HSH':
        rdn=aux.hselect(image,'rdnoise')
        gn=aux.hselect(image,'gain')
    return rdn,gn

#%%
    
def getrdga(images): # same tipe images, same gain same rdnoise
    lista=np.genfromtxt(images,dtype=None)
    rd,ga=rdngn(lista[0])
    return rd,ga

#%%
    
    
def fillheader(images): 
    lista=np.genfromtxt(images,dtype=None)
    image=lista[0]
    rd,ga= rdngn(image)
    tel=telescopefinder(image)
    
    if tel == 'JS':
        for im in lista:
            aux.hedit(im,'rdnoise',rd)
       # aux.hedit(image,'gain',ga)
            aux.hedit(im,'tel',tel)
    else:
        for im in lista:
            aux.hedit(im,'tel',tel)
             
#%%%%%%%%%
        
def RF(images,path=None):
    if path is not None:
        originalpath=aux.chdir(path,save=True)
    
    ext=os.path.splitext(images)[-1]
    tel=telescopefinder(images)
    if ext=='.fit' or ext=='.fits':
        
        if tel=='JS':
            comnt=aux.hselect(images,'COMMENT')
            
            criterio="c/Red. Focal"
            if criterio in comnt[0]:
                redF=True
            else:
                redF=False          
            
        else:
            redf=False
            
    else:
        im=np.genfromtxt(images,dtype=None)[0]
        
        if tel=='JS':
            comnt=aux.hselect(im,'COMMENT')
            comnt=comnt[0]
            criterio="c/Red. Focal"
            if criterio in comnt:
                redF=True
            else:
                redF=False          
            
        else:
            redF=False
    if path is not None:
        aux.chdir(originalpath)
    return redF

            
        
