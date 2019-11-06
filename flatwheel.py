#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import auxfunctions as aux
import os
from reduc import masterflat
#%%
def flatwheel(filters,listobj,path=None,mastbia=None,Dark=False,
               mastdark=None,edit=False):
    
    if path is not None:
        originalpath=aux.chdir(path,save=True)    
    
    i=0
    for x in filters:
        outfile=os.path.splitext(listobj[i])[0]+'.fits'
        masterflat(listobj[i],outfile,mastbia,Dark,mastdark,edit,path)
        i=i+1
        
    if path is not None:
        aux.chdir(originalpath)