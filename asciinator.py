#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 00:00:11 2019

@author: intel
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#%%
import os
from pyraf import iraf
import auxfunctions as aux

#%%
def asciinator(intab,coltab=None,col=None,partab=None,dattab=None,path=None):
    # ==================================================================
    #  Dada una tabla de STSDAS, la convierte en tabla ASCII.
    #  
    #  INPUT
    #  intab    : Nombre de la tabla STSDAS de entrada.
    #  (coltab) : Nombre de la tabla de columnas originales.
    #  (col)    : Columnas específicas a guardar en la nueva tabla.
    #  (partab) : Nombre de la tabla de parámetros originales.
    #  (dattab) : Nombre de la tabla de datos de salida.
    #  (path)   : Línea que indica el camino al directorio de la tabla.
    #
    # ------------------------------------------------------------------
    #
    #  Given a STSDAS table, converts it to ASCII format.
    #
    #  INPUT
    #  intab    : Name of the STSDAS input table.
    #  (coltab) : Name of the original column table.
    #  (col)    : Specific columns to save in the new table.
    #  (partab) : Name of the original parameter table.
    #  (dattab) : Name of the output data table.
    #  (path)   : String that indicates the path to the input table.
    #
    # ==================================================================
    
    if path is not None:
        originalpath=aux.chdir(path,save=True)
    
    iraf.tables()
    iraf.ttools()
    iraf.unlearn(iraf.tdump) #eternal sunshine of the spotless task
    
    aux.default(coltab,os.path.splitext(intab)[0]+'.col',rm=True)
    aux.default(partab,os.path.splitext(intab)[0]+'.par',rm=True)
    aux.default(dattab,os.path.splitext(intab)[0]+'.dat',rm=True)
    #sets default table names, mainly adds .col, .par or .dat
    
    if col is not None:
        iraf.tdump.columns=col #asks for specific columns to extract
    
    iraf.tdump.cdfile=coltab
    iraf.tdump.pfile=partab
    iraf.tdump.datafile=dattab
    iraf.tdump.table=intab #set input parameters
    
    iraf.tdump() #run, youngling, run
    
    if path is not None:
        aux.chdir(originalpath)
    
    
    
    