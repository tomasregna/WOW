#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#%%
import shutil as sh
import os

#%%
def backup(dirname=None,path=None,bformat="tar"):
    # ==================================================================
    #  Dado un directorio con archivos, genera un backup en el home.
    #  
    #  INPUT
    #  dirname  : Nombre del archivo comprimido que contendrá el backup
    #             (sin el formato)
    #  (path)   : Línea que indica el camino al directorio de 
    #             archivos a los cuales se hará backup.
    #  bformat  : Formato de compresión del archivo de backup.
    #
    # ------------------------------------------------------------------
    #
    #  Given a directory with files, generates a backup file at home.
    #
    #  INPUT
    #  dirname  : Name of the compressed backup file (without format)
    #  (path)   : String that indicates the path to the files subject to
    #             backup.
    #  bformat  : Compression format of the backup file.
    #
    # ==================================================================
    
    if path is None:
        path=os.getcwd() #si no conoce el path, usa la posición actual
      
    username=os.getenv('USER') #pide el nombre de usuario para poder
                               #concatenarlo al /home
                               
    backpath="/home/"+username+"/Backups"
    
    if os.path.exists(backpath) is False:
        os.mkdir(backpath) #si no existe un directorio de backups, 
                           #crea uno
    
    if dirname is None:
        dirname='backup'
        i=0
        while (os.path.exist(backpath+'/'+dirname+'.'+bformat)):
            i=i+1
            dirname='backup'+str(i)
    
    out=backpath+"/"+dirname #archivo concatenado al camino entero
    
    if os.path.exists(out) is False:
        sh.make_archive(out,bformat,backpath,path) #si no existe el
        #backup, genera uno con una tarea de shutil 
    
    
    
