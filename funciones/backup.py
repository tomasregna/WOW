#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#%%
import shutil as sh
import os
from datetime import datetime
import auxfunctions as aux
from colorama import Fore

#%%
def backup(dirname=None,path=None,bformat="tar"):
    '''
     Dado un directorio con archivos, genera un backup en el home, en la 
     carpeta "Backups".
      
      INPUT
      dirname  : Nombre del archivo comprimido que contendrá el backup
                 (sin el formato)
      (path)   : Línea que indica el camino al directorio de 
                 archivos a los cuales se hará backup.
      bformat  : Formato de compresión del archivo de backup.
    
     ------------------------------------------------------------------
    
      Given a directory with files, generates a backup file at home.
    
      INPUT
      dirname  : Name of the compressed backup file (without format)
      (path)   : String that indicates the path to the files subject to
                 backup.
      bformat  : Compression format of the backup file.
    '''    
        
    if path is not None:
        originalpath=aux.chdir(path,save=True) # moves towards path

# =============================================================================
#   CREATES BACKUP FOLDER IF NECESARY      
# =============================================================================
    username=os.getenv('USER') #pide el nombre de usuario para poder
                               #concatenarlo al /home
                               
    backpath="/home/"+username+"/Backups"
    
    if os.path.exists(backpath) is False:
        os.mkdir(backpath) #si no existe un directorio de backups, 
                           #crea uno
    now=datetime.now()
    
# =============================================================================
#     CREATES DIRNAME
# =============================================================================
    if dirname is not None:   # antes ignoraba el entry de aca
        if os.path.exists(backpath+"/"+dirname+'.'+bformat):  
            add=str(now.year)+str(now.day)+str(now.month) 
            i=0
            while (os.path.exists(backpath+'/'+dirname+add+'.'+bformat)):
                i=i+1
                add=str(now.year)+str(now.day)+str(now.month)+'-'+str(i)
            dirname=dirname+add
    else:   
        dirname=str(now.year)+str(now.day)+str(now.month)
        i=0
        while (os.path.exists(backpath+'/'+dirname+'.'+bformat)):
            i=i+1
            dirname=str(now.year)+str(now.day)+str(now.month)+'-'+str(i)
  
# =============================================================================
#       MAKE COMPRESS FILE
# =============================================================================
    sh.make_archive(dirname,bformat,path)#si no existe el
        #backup, genera uno con una tarea de shutil 
        
    here=os.getcwd() # gets current path 
    sh.move(here+'/'+dirname+'.'+bformat,backpath)
    
    
    
    print(Fore.RED +'Backup completo')
    
    if path is not None:  # vuelve al directorio principal.
        aux.chdir(originalpath)
