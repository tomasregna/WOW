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
    
#    bias=makelist(biaslist,path=path) # generates list string of files
    
    if path is not None:
        originalpath=os.getcwd() # saves working directory
        os.chdir(path) #moves to path
       
      
    
    bias='@'+biaslist # @ necesary for iraf to recognize .in files
    
    iraf.imred()    # open imred package
    iraf.ccdred()   # open ccdred package
    iraf.unlearn(iraf.zerocombine)  #erase all parameters seted before
     
    
        # saves header IMAGETYP value of images
        # if is not BIAS, edits the header.
        
#    testing=iraf.hselect(bias,fields='IMAGETYP',expr = "yes",Stdout=1)
#    for x in testing:  
#        if x != 'zero':
#            edit=True # flag for edit
    
    while(edit): # edits the header of all images
        iraf.hedit(bias,fields='IMAGETYP',
                   value='zero',add='yes',update='yes',ver='no')
        edit=False    # flag down

    # if outfile not given, use default
    if outfile is None:
        outfile='Zero.fits'
    outfile=outfile
        # if file alredy exist, delete it 
    if os.path.exists(outfile):
        os.remove(outfile)

    iraf.zerocombine.output=outfile # set outfile parameter
    iraf.zerocombine.input=bias  #set input file parameter
    iraf.zerocombine() # creates masterbias
    if path is not None:
        os.chdir(originalpath)  # goes back to original directory
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
        originalpath=os.getcwd() # saves working directory
        os.chdir(path) #moves to path
           
    dark='@'+darklist   
    
    
    iraf.imred() # open imred package
    iraf.ccdred()# open ccdred package
    iraf.unlearn(iraf.darkcombine) #erase all parameters seted before


        # saves header IMAGETYP value of images
        # if is not DARK, edits the header.   
#    testing=iraf.hselect(darklist,fields='IMAGETYP',expr = "yes",Stdout=1)
#    for x in testing:
#        if x != 'dark':
#            edit=True
    while(edit): # edits the header of all images
        iraf.hedit(dark,fields='IMAGETYP',value='dark',add='yes',
                   update='yes',ver='no')
        edit=False # flag down
        

        # if outfile not given, use default  
    if outfile is None:
        outfile='Dark.fits'
    outfile=outfile
        # if file alredy exist, delete it 
    if os.path.exists(outfile):
            os.remove(outfile)
        # if mastbia not given, use default   
    if mastbia is None:
        mastbia='Zero.fits'
    mastbia=mastbia

    iraf.ccdpro.zero=mastbia
    iraf.darkcombine.output=outfile # set outfile parameter
    iraf.darkcombine.input=dark     # set input file parameter
    iraf.darkcombine() # creates masterdark
    if path is not None:
        os.chdir(originalpath)  # goes back to original directory

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
        originalpath=os.getcwd() # saves working directory
        os.chdir(path) #moves to path
        
    flat='@'+flatlist # para trabajar mas facil
    
    iraf.imred()    # open imred package
    iraf.ccdred()   # open ccdred package
    iraf.unlearn(iraf.flatcombine) #erase all parameters seted before
    
        # saves header IMAGETYP value of images
        # if is not FLAT, edits the header.   
#    testing=iraf.hselect(flat,fields='IMAGETYP',expr='yes',Stdout=1)
#    for x in testing:
#        if x != 'flat':
#            edit=True
    while(edit): # edits the header of all images
        iraf.hedit(images=flat,fields='IMAGETYP',
                   value='flat',add='yes',update='yes',ver='no')
        edit=False        # flag down
        
        
    while(subsets):   # creates subsets file
        f=open('subsets','w+') 
        lista=iraf.hselect(flat,fields='FILTER',expr = "yes",Stdout=1)
        print lista
        filters=np.unique(lista)
        for x in filters:
            print >> f , x,x
        f.close()
        subsets=False # flag down
      
    
    # if outfile not given, use default 
    if outfile is None:       
        outfile='Flat'
        if os.path.exists(outfile+'.fits'):
            os.remove(outfile+'.fits')
    else:
        outfile=outfile
                
#    Generate a .in file with output masterflats files, by filter    
    h=open('mflatlist.in','w+') # creates file

    for x in filters:   # for every filter
        if os.path.exists(outfile+x+'.fits'): # if file exist
            os.remove(outfile+x+'.fits') # remove it
        print >> h, outfile+x+'.fits' # write in .in file the masterflat output
    h.close() # close .in file
    
    
       # if mastbia not given, use default     
    if mastbia is None:
        mastbia='Zero.fits'
    else:
        mastbia=mastbia
    iraf.ccdpro.zero=mastbia
    
    # if mastdark not given, use default
    if mastdark is None:
        mastdark='Dark.fits'
    else:
        mastdark=mastdark
    iraf.ccdpro.dark=mastdark
    


    iraf.flatcombine.output=outfile # sets output file
    iraf.flatcombine.input=flat     # sets input file
    iraf.flatcombine()              # generates masterflats
    if path is not None:
        os.chdir(originalpath)  # goes back to original directory
    

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
#                   masterflats. Por defecto usa "flatlist.in" 
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
#                   "flatlist.in" and takes the same path as imagelist.
#     (edit)     : If true, edits the header of the images, changing imagetyp
#                   to "object".
#     (output)   : Output of the result images. If none given, uses the same
#                   file name adding a ".red" before ".fit".             
# =============================================================================
    
    if path is not None:
        originalpath=os.getcwd() # saves working directory
        os.chdir(path) #moves to path
        
    iraf.imred()     # open imred package
    iraf.ccdred()    # open ccdred package
    
    images='@'+imagelist

                #saves header IMAGETYP value of images
                # if not object edits the header
#    test=iraf.hselect(images,fields='IMAGETYP',expr='yes',Stdout=1)
#    if test!='object':
#        edit=True
                
    while edit: # edits the header changes imagetyp
        iraf.hedit(images,fields='IMAGETYP',value='object'
                   ,up='yes',ver='no',add='yes')
        edit=False # flag down
        
        
                 # if mastbia not given, use default     
    if mastbia is None:
        mastbia='Zero.fits'
    else:
        mastbia=mastbia
    iraf.ccdpro.zero=mastbia
    
    
                 # if Dark, set dark correction on
                 # if mastdark not given, use default     
    if Dark:
        if mastdark is None:
            mastdark='Dark.fits'
        else:
            mastdark=mastdark
        iraf.ccdpro.dark=mastdark
        iraf.ccdpro.darkcor='yes'
        
                #if mastflat not given, use default
    if mastflat is None:
        mastflat='@'+'mflatlist.in'
    else:   
        mastflat='@'+mastflat
    iraf.ccdpro.flat=mastflat
    
                #if output not given, use default
    if output is None:
        output=''
        alist=imagelist.split(',') # list of input images
        for y in alist:  
            y=y[:-3]+'red.fit,'  #adds .red before .fit
            if os.path.exists(y):  # if alredy exist, remove
                os.remove(y)
        output=output[:-1]  #kill last comma
        
        
    iraf.ccdpro.output=output  #set outfile
    iraf.ccdpro.images=images  # set input file
    iraf.ccdproc()    #runs ccdproc, reduces images
    if path is not None:
        os.chdir(originalpath)  # goes back to original directory
#%%