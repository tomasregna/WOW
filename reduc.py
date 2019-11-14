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
import auxfunctions as aux
#%%
def masterbias(biaslist,outfile=None,path=None): 
# =============================================================================
#     Dada una lista de bias, genera un masterbias.
#
#      INPUT
#      biaslist  : Archivo .in con los nombres de los bias.
#      (path)    : String que indica el camino al biaslist.
#      (outfile) : Nombre del archivo de salida. Por defecto usa "Zero.fits".
#                  
#                   ---------------------------------------      
#
#      Given a bias list, generates a masterbias.
#    
#      INPUT
#      biaslist  : .in file with bias names.
#      (path)    : String containing the path to biaslist.
#      (outfile) : Output file name. If none, uses "Zero.fits".
# =============================================================================
    
    if path is not None:
        originalpath=aux.chdir(path,save=True)      
    
    bias='@'+biaslist # @ necesary for iraf to recognize .in files
    
    iraf.imred()    # open imred package
    iraf.ccdred()   # open ccdred package
    iraf.unlearn(iraf.zerocombine)  #erase all parameters seted before
    
    
    imtyp=aux.hselect(bias,'IMAGETYP')
       for tip in imtyp:
           if not tip.strip()=='zero'
               edit=True
            
    if edit: # edits the header of all images
        aux.hedit(bias,'IMAGETYP','zero')

    # if outfile not given, use default, if exist delet it
    outfile=aux.default(outfile,'Zero.fits',borrar=True)

    iraf.zerocombine.output=outfile # set outfile parameter
    iraf.zerocombine.input=bias  #set input file parameter
    iraf.zerocombine() # creates masterbias
    if path is not None:
        aux.chdir(originalpath)
#%%
    
    
    
def masterdark(darklist,outfile=None,mastbia=None,path=None):
    
# =============================================================================
#   Dada una lista de darks, genera un masterdark.
#     
#     INPUT
#     darklist  : Archivo .in con los nombres de los darks.
#     (path)    : String que indica el camino al darklist.
#     (mastbia) : Archivo que contiene el masterbias. Por defecto usa
#                 "Zero.fits" y toma el mismo path que el darklist.
#     (outfile) : Nombre del archivo de salida. Por defecto usa "Dark.fits"
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
# =============================================================================
    
#    dark= makelist(darklist,path=path) # generates list string of files
    
    if path is not None:
        originalpath=aux.chdir(path,save=True)
           
    dark='@'+darklist   
    
    iraf.imred() # open imred package
    iraf.ccdred()# open ccdred package
    iraf.unlearn(iraf.darkcombine) #erase all parameters seted before
    iraf.unlearn(iraf.ccdproc)

    imtyp=aux.hselect(dark,'IMAGETYP')
       for tip in imtyp:
           if not tip.strip()=='dark'
               edit=True

    if edit: # edits the header of all images
        aux.hedit(dark,'IMAGETYP','dark')
       
        # if outfile not given, use default, if exist delet it  
    outfile=aux.default(outfile,'Dark.fits',borrar=True)
    
        # if mastbia not given, use default   
    mastbia=aux.default(mastbia,'Zero.fits')


    iraf.darkcombine.process='yes'  #corrije imagenes dark por bias
    iraf.ccdproc.zero='yes' #indica que hay que usar el bias
    iraf.ccdpro.zero=mastbia # indica cual es el masterbias
    iraf.ccdproc.fixpix='no'
    iraf.ccdproc.overscan='no'
    iraf.ccdproc.trim='no' #no disponible trim, overs ni fixpix en la v1.0
    
    iraf.darkcombine.output=outfile # set outfile parameter
    iraf.darkcombine.input=dark     # set input file parameter
      
    iraf.darkcombine() # creates masterdark
    if path is not None:
        aux.chdir(originalpath)

 #%%   
 
 
def masterflat(flatlist,outfile=None,mastbia=None,Dark=False,
               mastdark=None,path=None):
    
# =============================================================================
#      Dada una lista de flats, genera el masterflat de cada set de flat, por
#      filtro.
#    
#     INPUT    
#    flatlist   : Archivo .in con los nombres de los archivos flat.
#    (path)     : Carácteres que indica el camino a flatlist.
#    (mastbia)  : Archivo que contiene el masterbias. Por defecto usa
#                 "Zero.fits" y toma el mismo path que el flatlist.
#    (Dark)     : Si es verdadero, corrije por Dark.
#    (mastdark) : Archivo que contiene el masterdark. Por defecto usa
#                 "Dark.fits" y toma el mismo path que el flatlist.
#    (outfile)  : nombre del archivo de salida. Por defecto usa "Flat".
#               
#                   ---------------------------------------      
#
#     Given a list of flats, generates the masterflat of every set of flats.
#    
#    INPUT
#    flatlist   : .in file with flat files names.
#    (path)     : String that indicates the path to flatlist.
#    (mastbia)  : File that contains the masterbias. If none uses
#    (Dark)     : If true, apply Dark correction.
#                 "Zero.fits" and always use the same path as flatlist.
#    (mastdark) : File that contains the msaterdark. If none uses
#                 "Dark.fits" and always use the same path as flatlist.  
#    (outfile)  : Output file name. If none, uses "Flat".
# =============================================================================
    
    if path is not None:
        originalpath=aux.chdir(path,save=True)
                        
    flat='@'+flatlist # para trabajar mas facil
    
    iraf.imred()    # open imred package
    iraf.ccdred()   # open ccdred package
    iraf.unlearn(iraf.flatcombine) #erase all parameters seted before
    iraf.unlearn(iraf.ccdproc)
    
    imtyp=aux.hselect(flat,'IMAGETYP')
       for tip in imtyp:
           if not tip.strip()=='flat'
               edit=True    
    if edit:
        aux.hedit(flat,'IMAGETYP','flat')          
          
    # if outfile not given, use default
    outfile=aux.default(outfile,'Flat.fits',borrar=True) 

    
       # if mastbia not given, use default   
    mastbia=aux.default(mastbia,'Zero.fits')
    iraf.ccdpro.zero=mastbia
    
    # if mastdark not given, use default
    iraf.ccdpro.darkcor='no' #sets no as default
    if Dark is True:
        mastdark=aux.default(mastdark,'Dark.fits')
        iraf.ccdpro.dark=mastdark
        iraf.ccdpro.darkcor='yes'

    iraf.flatcombine.process='yes'
    iraf.ccdproc.fixpix='no'
    iraf.ccdproc.overscan='no'
    iraf.ccdproc.trim='no' #no disponible trim, overs ni fixpix en la v1.0
    iraf.flatcombine.output=outfile # sets output file    
    iraf.flatcombine.input=flat    # sets input file
    iraf.flatcombine()              # generates masterflats
       
    if path is not None:
        aux.chdir(originalpath)
    
#%%
    
def process(imagelist,path=None,Dark=False,mastbia=None,mastdark=None
            ,mastflat=None,output=None):
    
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
#     (mastflat) : Nombre del archivo masterflat. Por defecto, usa "Flat.fits"
#                   y toma el camino dado por path.
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
#     (mastdark) : File that contains the masterdark. If none uses
#                   "Dark.fits" and uses path.
#     (mastflat) : File that contains the masterflat. If none uses
#                   "Flat.fits" and uses path.
#     (output)   : Output of the result images. If none given, uses the same
#                   file name adding a ".red" before ".fit".             
# =============================================================================
    
    if path is not None:
        originalpath=aux.chdir(path,save=True)
        
    iraf.imred()     # open imred package
    iraf.ccdred()    # open ccdred package
    iraf.unlearn(iraf.ccdproc)
    
    images='@'+imagelist

    imtyp=aux.hselect(images,'IMAGETYP')
       for tip in imtyp:
           if not tip.strip()=='object'
               edit=True
    if edit: # edits the header changes imagetyp
        aux.hedit(images,'IMAGETYP','object')
        
        
     # if mastbia not given, use default 
    mastbia=aux.default(mastbia,'Zero.fits')
    iraf.ccdpro.zero=mastbia
    iraf.ccdpro.zerocor='yes'
    
    
    # if Dark, set dark correction on
    # if mastdark not given, use default     
    iraf.ccdpro.darkcor='no'
    if Dark:
        mastdark=aux.default(mastdark,'Dark.fits')
        iraf.ccdpro.dark=mastdark
        iraf.ccdpro.darkcor='yes'
        
    #if mastflat not given, use default    
    mastflat=aux.default(mastflat,'Flat.fits')
    iraf.ccdpro.flat=mastflat
    iraf.ccdpro.flatcor='yes'
    
    
     #if output not given, use default
    letrita=aux.default(output,'R') 
    output=letrita+'//'+images
    alist=np.genfromtxt(imagelist,dtype=None)
    for x in alist:
        aux.rm(letrita+x)
        
    iraf.ccdproc.fixpix='no'
    iraf.ccdproc.overscan='no'
    iraf.ccdproc.trim='no' #no disponible trim, overs ni fixpix en la v1.0
    iraf.ccdpro.output=output  #set outfile
    iraf.ccdpro.images=images  # set input file
    iraf.ccdproc()    #runs ccdproc, reduces images
    if path is not None:
        aux.chdir(originalpath)
#%%
     
