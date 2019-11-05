#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:46:29 2019

@author: intel
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
    iraf.hedit(images,fields=fields,value=value,add='yes'
               ,update='yes',ver='no')


def rm(archivo): #if exist, removes file
    if os.path.exists(archivo):
        os.remove(archivo)
    
def hselect(images,field): # returns a value of a header parameter
    select = iraf.hselect(images,fields=field,expr='yes',Stout=1) 
    return select

def default(field,value,rm=False):  # set default values if none
    if field is None:               # can remove the file if exist
        field=value
    if rm:
        rm(field)


