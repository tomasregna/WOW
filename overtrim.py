#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:24:09 2019

@author: intel
"""
from pyraf import iraf
import auxfunctions as aux

#%%
def oversc(image,section='image',readax='line'):
    
    iraf.ccdproc.readaxis=readax
#    imlist=np.genfromtxt(images,dtype=None)
    
    if section!='image':
        iraf.ccdproc.overscan='yes'  
        iraf.ccdproc.biassec=section
    else:    
        if aux.hsel(image,'BIASSEC') is not None:    
            iraf.ccdproc.overscan='yes'
            iraf.ccdproc.biassec=section
        else:
            print('Nonexistent BIASSEC data in header')
            iraf.ccdproc.overscan='no'
def trimmer(image,section='image'):    
    
#    imlist=np.genfromtxt(images,dtype=None)
    if section!='image':
        iraf.ccdproc.overscan='yes'  
        iraf.ccdproc.trimsec=section
    else:    
        if aux.hsel(image,'TRIMSEC') is not None:    
            iraf.ccdproc.overscan='yes'
            iraf.ccdproc.trimsec=section
        else:
            print('Nonexistent TRIMSEC data in header')
            iraf.ccdproc.trim='no'   