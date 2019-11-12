#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
CONTAINS:

chdir(newpath,save=False) moves to path, can save the original path

hedit(images,fields,value) edits header of files

rm(archivo) if exist, removes file 

hselect(images,field) returns a value of a header parameter

default(field,value,rm=False) set default value if none, can delete file
"""
#%%
import os
from pyraf import iraf


#%%
def chdir(newpath,save=False):  #moves to path, can save the original path
    original=os.getcwd()
    os.chdir(newpath)
    if save:
        return original

        
def hedit(images,fields,value): # edits header of files
    iraf.hedit(images=images,fields=fields,value=value,add='yes',update='yes',ver='no')


def rm(archivo): #if exist, removes file
    if os.path.exists(archivo):
        os.remove(archivo)
    
def hselect(images,field): # returns a value of a header parameter
    select = iraf.hselect(images,fields=field,expr='yes',Stdout=1) 
    return select

def default(field,value,borrar=False):  # set default values if none
    if field is None:               # can remove the file if exist
        field=value
    if borrar:
        rm(field)
    return(field)
