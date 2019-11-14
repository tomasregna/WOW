#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:56:08 2019

@author: guevaran
"""
import os
os.chdir('/home/guevaran')
from pyraf import iraf
os.chdir('/home/guevaran/Documents/Observacional/Trabajo_Final/trabajo_astro_observacional-master/')
import random
import auxfunctions as aux
os.chdir('/home/guevaran/Documents/Observacional/Trabajo_Final/20180602')
#%%

def skynoise(image,output,path=None):
    
     if path is not None:
        originalpath=aux.chdir(path,save=True)
        
        
    limits=aux.hselect(image,'CCDSIZE')
    limit=limits[0]
    limit=limit.strip()
    dd=[]
    c=[]
    i=0
    for x in limit:
        if x==':':
            dd.append(i)
        elif x==',':
            c.append(i)
        i=i+1
    l1=int(limit[dd[0]+1:c[0]])
    l2=int(limit[dd[1]+1:-1])
    aux.default(output,'ruidoceleste.coo',delete=True)
    f=open(output,'a+')

    for i in range(int(l1/10.)):
        x=random.randint(1,l1)
        y=random.randint(1,l2)
        print >> f,x,y
    if path is not None:
        aux.chdir(originalpath)
