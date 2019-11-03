#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:06:43 2019

@author: guevaran


"""

#%%
import numpy as np 
import os
from pyraf import iraf
#%%
# =============================================================================
#  funciones auxiliares 
# =============================================================================
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
#%%
def masterbias(biaslist,outfile=None,edit=False,path=None): 
# =============================================================================
#     Dada una lista de bias, genera un masterbias.
#
#      INPUT
#      biaslist  : Archivo .in con los nombres de los bias.
#      (path)    : String que indica el camino al biaslist.
#      (outfile) : Nombre del archivo de salida. Por defecto usa "Zero.fits".
#      (edit)    : En caso de que sea verdadero, edita el header de las
#                  imágenes para agregarles el tipo "zero".
#                  
#                   ---------------------------------------      
#
#      Given a bias list, generates a masterbias.
#    
#      INPUT
#      biaslist  : .in file with bias names.
#      (path)    : String containing the path to biaslist.
#      (outfile) : Output file name. If none, uses "Zero.fits".
#      (edit)    : If true, edits the biaslist headers changing imagetyp to
#                  "zero".
# =============================================================================
    
    if path is not None:
        originalpath=chdir(path,save=True)      
    
    bias='@'+biaslist # @ necesary for iraf to recognize .in files
    
    iraf.imred()    # open imred package
    iraf.ccdred()   # open ccdred package
    iraf.unlearn(iraf.zerocombine)  #erase all parameters seted before
        
    if edit: # edits the header of all images
        hedit(bias,'IMAGETYP','zero')

    # if outfile not given, use default, if exist delet it
    default(outfile,'Zero.fits',rm=True)

    iraf.zerocombine.output=outfile # set outfile parameter
    iraf.zerocombine.input=bias  #set input file parameter
    iraf.zerocombine() # creates masterbias
    if path is not None:
        chdir(originalpath)
#%%
    
    
    
def masterdark(darklist,outfile=None,mastbia=None,edit=False,path=None):
    
# =============================================================================
#   Dada una lista de darks, genera un masterdark.
#     
#     INPUT
#     darklist  : Archivo .in con los nombres de los darks.
#     (path)    : String que indica el camino al darklist.
#     (mastbia) : Archivo que contiene el masterbias. Por defecto usa
#                 "Zero.fits" y toma el mismo path que el darklist.
#     (outfile) : Nombre del archivo de salida. Por defecto usa "Dark.fits"
#     (edit)    : En caso de que sea verdadero, edita el header de las
#                 imágenes para agregarles el tipo "dark".
#                  
#                   ---------------------------------------      
#
#      Given a dark list, generates a masterdark.
#    
#     INPUT
#     darklist  : .in file with dark files names.
#     (path)    : String that indicates the path to darklist.
#     (mastbia) : File that contains the masterbias. If none uses
#                 "Zero.fits" and always use the same path as darklist.
#     (outfile) : Output file name. If none, uses "Dark.fits".
#     (edit)    : If true, edits the header of the images, changing imagetyp
#                 to "dark".
# =============================================================================
    
#    dark= makelist(darklist,path=path) # generates list string of files
    
    if path is not None:
        originalpath=chdir(path,save=True)
           
    dark='@'+darklist   
    
    iraf.imred() # open imred package
    iraf.ccdred()# open ccdred package
    iraf.unlearn(iraf.darkcombine) #erase all parameters seted before

    if edit: # edits the header of all images
        hedit(dark,'IMAGETYP','dark')
       
        # if outfile not given, use default, if exist delet it  
    default(outfile,'Dark.fits',rm=True)
    
        # if mastbia not given, use default   
    default(mastbia,'Zero.fits')


    iraf.darkcombine.process='yes'  #corrije imagenes dark por bias
    iraf.ccdproc.zero='yes' #indica que hay que usar el bias
    iraf.ccdpro.zero=mastbia # indica cual es el masterbias
    
    iraf.darkcombine.output=outfile # set outfile parameter
    iraf.darkcombine.input=dark     # set input file parameter
      
    iraf.darkcombine() # creates masterdark
    if path is not None:
        chdir(originalpath)

 #%%   
 
 
def masterflat(flatlist,outfile=None,mastbia=None,
               mastdark=None,edit=False,path=None,subsets=True):
    
# =============================================================================
#      Dada una lista de flats, genera el masterflat de cada set de flat, por
#      filtro.
#    
#     INPUT    
#    flatlist   : Archivo .in con los nombres de los archivos flat.
#    (path)     : Carácteres que indica el camino a flatlist.
#    (subsets)  : Si es verdadero, crea el archivo subsets.
#    (mastbia)  : Archivo que contiene el masterbias. Por defecto usa
#                 "Zero.fits" y toma el mismo path que el flatlist.
#    (mastdark) : Archivo que contiene el masterdark. Por defecto usa
#                 "Dark.fits" y toma el mismo path que el flatlist.
#    (outfile)  : nombre del archivo de salida. Por defecto usa "Flat".
#    (edit)     : En caso de que sea verdadero, edita el header de las
#                 imágenes para agregarles el tipo "flat".
#               
#                   ---------------------------------------      
#
#     Given a list of flats, generates the masterflat of every set of flats.
#    
#    INPUT
#    flatlist   : .in file with flat files names.
#    (path)     : String that indicates the path to flatlist.
#    (subsets)  : If true, creates subsets file.
#    (mastbia)  : File that contains the masterbias. If none uses
#                 "Zero.fits" and always use the same path as flatlist.
#    (mastdark) : File that contains the msaterdark. If none uses
#                 "Dark.fits" and always use the same path as flatlist.  
#    (outfile)  : Output file name. If none, uses "Flat".
#    (edit)     : If true, edits the header of the images, changing imagetyp    
#                 to "flat".
# =============================================================================
    
    if path is not None:
        originalpath=chdir(path,save=True)
                        
    flat='@'+flatlist # para trabajar mas facil
    
    iraf.imred()    # open imred package
    iraf.ccdred()   # open ccdred package
    iraf.unlearn(iraf.flatcombine) #erase all parameters seted before
        
    if edit:
        hedit(flat,'IMAGETYP','flat')          
        
    while(subsets):   # creates subsets file
# =============================================================================
#         OJO CON ESTO
#        El archivo subsets que crea hace una realación 
#        FILTER LETTER -> FILTER LETTER
#        para imagenes tomadas en casleo no sirve
#        pues le asignan a cada filtro un numero
# =============================================================================
        
        f=open('subsets','w+') 
        lista=iraf.hselect(flat,fields='FILTER',expr = "yes",Stdout=1)
        print lista
        filters=np.unique(lista)
        for x in filters:
            print >> f , x,x
        f.close()
        subsets=False # flag down
      
    
    # if outfile not given, use default
    default(outfile,'Flat',rm=True) # segun el subsets va a agregar letra
    rm(outfile+'.fits')             # por filtro,ej:FlatV.fits
    
       # if mastbia not given, use default   
    default(mastbia,'Zero.fits')
    iraf.ccdpro.zero=mastbia
    
    # if mastdark not given, use default
    default(mastdark,'Dark.fits')
    iraf.ccdpro.dark=mastdark

    iraf.cccdproc.process='yes'
    
    for x in filters:
        if os.path.exists(outfile+x+'.fits'): # if file exist
            os.remove(outfile+x+'.fits') # remove it
        f=open(outfile+x+'.in', 'a+') # +a to append 
        for im in flat:
            if iraf.hselect(im,fields='FILTER',expr = "yes",Stdout=1) == x :
                f.append(im) #if image filter is x, append to filter file output
        f.close()
        listout='@'+outfile+x+'.in' #list format for iraf
        iraf.flatcombine.output=outfile+x+'.fits' # sets output file    
        iraf.flatcombine.input=listout    # sets input file
        iraf.flatcombine()              # generates masterflats
        
    
    if path is not None:
        chdir(originalpath)
    

#%%
    
    
def process(imagelist,path=None,Dark=False,mastbia=None,mastdark=None
            ,mastflat=None,edit=False,output=None):
    
# =============================================================================
#     Dada una lista de imágenes de ciencia, las reduce.
#     
#     INPUT
#     imagelist  : Archivo .in con las imágenes de ciencia.
#     (path)     : Camino al archivo imagelist.
#     (Dark)     : Si es verdadero, corrije por Dark.
#     (mastbia)  : Nombre del archivo masterbias. Por defecto, usa "Zero.fits"
#                   y toma el camino dado por path.
#     (mastdark) : Nombre del archivo masterdark. Por defecto, usa "Dark.fits"
#                   y toma el camino dado por path.
#     (mastflat) : Nombre del archivo in que contiene los nombres de los
#                   masterflats. Por defecto usa "mflatlist.in" 
#                   y toma el camino dado por path
#     (edit)     : Si es verdadero, edita el header de las imágenes cambiando
#                   el tipo a "object".
#     (output)   : Output de las imágenes reducidas. Por defecto, el output es
#                   el nombre del archivo con un ".red" antes del ".fit".
#     
#                        ---------------------------------------      
#            
#     Process science images, given a list of the file names.
#     
#     INPUT
#     imagelist  : .in file containing the objetcs file names.
#     (path)     : Path to imagelist.
#     (Dark)     : If true, apply Dark correction.
#     (mastbia)  : File that contains the masterbias. If none uses
#                   "Zero.fits" and uses path.
#     (mastdark) : File that contains the msaterdark. If none uses
#                   "Dark.fits" and uses path.
#     (mastflat) : .in file that contains the list of masterflats. If none uses
#                   "mflatlist.in" and takes the same path as imagelist.
#     (edit)     : If true, edits the header of the images, changing imagetyp
#                   to "object".
#     (output)   : Output of the result images. If none given, uses the same
#                   file name adding a ".red" before ".fit".             
# =============================================================================
    
    if path is not None:
        originalpath=chdir(path,save=True)
        
    iraf.imred()     # open imred package
    iraf.ccdred()    # open ccdred package
    
    images='@'+imagelist

    while edit: # edits the header changes imagetyp
        hedit(images,'IMAGETYP','object')
        edit=False # flag down
        
        
     # if mastbia not given, use default 
    default(mastbia,'Zero.fits')
    iraf.ccdpro.zero=mastbia
    iraf.ccdpro.zerocor='yes'
    
    
    # if Dark, set dark correction on
    # if mastdark not given, use default     
    if Dark:
        default(mastdark,'Dark.fits')
        iraf.ccdpro.dark=mastdark
        iraf.ccdpro.darkcor='yes'
        
    #if mastflat not given, use default    
    default(mastflat,'mflatlist.in')
    iraf.ccdpro.flat='@'+mastflat
    iraf.ccdpro.flatcor='yes'
    
    
     #if output not given, use default
    default(output,'R//'+images) #segun kmi esto funca
    alist=imagelist.split(',')
    for x in alist:
        rm('R'+x)
        
    iraf.ccdpro.process='yes'
    iraf.ccdpro.output=output  #set outfile
    iraf.ccdpro.images=images  # set input file
    iraf.ccdproc()    #runs ccdproc, reduces images
    if path is not None:
        chdir(originalpath)
#%%
     
