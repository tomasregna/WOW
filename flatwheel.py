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
       
