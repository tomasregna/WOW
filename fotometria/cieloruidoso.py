#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:56:08 2019

@author: guevaran
"""
from pyraf import iraf
import random
import funciones.auxfunctions as aux
from scipy.stats import mode
import numpy as np

#%%

def skynoise(image,path=None):
    '''
     Calcula el ruido del cielo de una imagen. 
     Toma una moda de la imagen total con \verb|imstat|. Luego genera una lista
     de n puntos aleatorios entre los límites de la imagen, con
     $n=\frac{anchoCCD^2}{10}$, y corre \verb|imexa| sobre cada punto, sacando
     la estadística. Descarta los puntos que superen en cuentas 3 veces la moda
     y toma la media de la desviación estandar del cielo de los puntos
     restantes. Este valor es el que devuelve como aproximación del skynoise.
    INPUT
    image : una imagen
    (path): camino a imagen
     '''
    
    if path is not None:
        originalpath=aux.chdir(path,save=True)
        
    stat= iraf.imstat(image,fields='mode',Stdout=1) #get the mode of the image
    moda=float(stat[1]) # reads the mode as a float variable

    binn=aux.hselect(image,'CCDSUM') # gets binning of the image
    binn=binn[0]  # access element 0 of the array
    binn=binn[1]  # access first character
    binn=int(binn)  # converts string to integer

    #------------------------------------------------------------------
    ccdsec=aux.hselect(image,'CCDSEC') # para agarrar imagenes con trim
    if ccdsec[0]=='':
        limits=aux.hselect(image,'CCDSIZE') # gets ccd pixel size
    else:
        limits=aux.hselect(image,'BIASSEC')
    limit=limits[0]  # gets element 0 of the array
    limit=limit.strip() # removes white space
    dd=[]  # stores position of double dot
    c=[]   # stores position of comma
    i=0 
    for x in limit:  # for every character
        if x==':': # if character is :
            dd.append(i) #stores index
        elif x==',': # if character is ,
            c.append(i) #stores index
        i=i+1
    #-----------------------------------------------------------------
#   
#    x1=int(limit[1:dd[0]])  # saves first limit
#    y1=int(limit[c[0]+1:dd[1]]) #saves las limit

    x2=int(limit[dd[0]+1:c[0]]) 
    y2=int(limit[dd[1]+1:-1])  
    
    l1=x2/binn # limit one 

    l2=y2/binn # limit two  
    # set random numbers aux file   
    aux.rm('ruidoceleste.coo') #delete if already exists
    output='ruidoceleste.coo'
  
    
    coords=[]
    nrandom=int((l1**2)/100.) #quadratic growth
    
    f=open(output,'a+') # creates outfile
    for i in range(nrandom): # creates l1/10 random coordinates
        x=random.randint(1,l1) # random x coord, from x1 to l1
        y=random.randint(1,l2) # random y coord, from y1 to l2
        coords.append([x,y])
        print >> f,x,y  # writes coords in file 
    f.close()

    iraf.unlearn(iraf.imexamine) #unlearns imexamine first
# tuve que mandar estos comandos para que no me cambie el z1yz2 cada vez
# que calculaba todo. Cosa de como tenia mi seteado mi iraf ( o no?)            
    iraf.imexamine.autoredraw='no' #noredraw of the image 
#    iraf.display.zscale='no'
    iraf.imexamine.allframes='no'
    iraf.imexamine.use_display='no'  
    iraf.imexamine.imagecur=output # sets imexa infile
    iraf.imexamine.defkey='m'  # sets key to use in imexa
    imst=iraf.imexamine(image,frame=1,Stdout=1)  # calls imexa
    

    stdev=[]
    maxi=[]

    for lin in imst[1:]:
        stdev.append(float(lin.split()[4]))
        maxi.append(float(lin.split()[6]))

    # criterio de seleccion <3*moda no es estrella
    validos=[]
    for j in range(nrandom):
            if maxi[j] < 3*moda:
                validos.append(stdev[j])

                
    sigmasky=mode(validos) # toma la moda
    sigmasky=sigmasky[0][0]
    
#     tomo la media de la disperción
#    sigmasky=np.mean(validos)
#    print validos             
    aux.rm(output) # mata el archivo auxiliar    
    
    if path is not None:
        aux.chdir(originalpath)
    return(sigmasky) 
#%%
    
def skynoises(images,path=None):
    '''
    Llama a skynoise para una lista de imagenes.
    '''   
    if path is not None:
        originalpath=aux.chdir(path,save=True)
    lista=np.genfromtxt(images,dtype=None)
    i=0
    sigmas=[]
    for im in lista:
        sigmas.append(skynoise(im,path))
        i=i+1
    if path is not None:
        aux.chdir(originalpath)
    return(sigmas)
