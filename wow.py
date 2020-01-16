#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import yaml
from colorama import Fore, Style
import numpy as np
#%%
def main():
    '''
    Este archivo lee el archivo de parametros yaml y ejecuta cada proceso
    segun este indicado.
    '''
    from setmodules import setmodules
    setmodules()
    import funciones.auxfunctions as aux
    from reduccion import reduc
    from funciones.backup import backup
    from reduccion.filterseparator import filtersep2
    import reduccion.wheelee as wh
    from fotometria.starfinder import multisf
    from fotometria.photom import photom
    from fotometria.tablemaker import gentable
    from fotometria.cieloruidoso import skynoises
    from fotometria.fullwidth import multifull


#    print(Fore.MAGENTA + 'So astronomy')
#    print(Style.RESET_ALL)

#%%
    '''
    Lee archivo de parametros
    '''
    f=open('parameters.yaml','a+')
    data=yaml.load(f)
    f.close()
#%%
    '''
    Backup
    '''
    if data['backup']['dobackup']:
     
        path0=data['backup']['path']
        formato=data['backup']['opciones']['formato']
        nombre=data['backup']['opciones']['filename']
        backup(dirname=nombre,path=path0,bformat=formato)

    
#%%
    '''
    Reduccion
    '''
    if data['reducir']['doreducir']:
        imagenes=data['reducir']['imobj']
        pathim=data['reducir']['pathim']
        bias=data['reducir']['imbias']
        pathbi=data['reducir']['pathbi']
        flat=data['reducir']['imflat']
        pathfl=data['reducir']['pathfl']
        dark=data['reducir']['opciones']['imdark']
        pathdk=data['reducir']['opciones']['pathdk']
        trim=data['reducir']['trim']
        ov=data['reducir']['overscan']
        reduc.masterbias(bias,path=pathbi,area=trim,sec=ov)
        if data['reducir']['opciones']['dark']:
            reduc.masterdark(dark,path=pathdk,area=trim,sec=ov)
        fieldfilt=data['reducir']['opciones']['filterfield']
        filters,flats=filtersep2(flat,path=pathfl,field=fieldfilt)
        filters2,objs=filtersep2(imagenes,path=pathim,field=fieldfilt)
        wh.flatw(filters,flats,dark=data['reducir']['opciones']['dark'],
        path=pathfl,area=trim,sec=ov)
        wh.procw(filters2,objs,dark=data['reducir']['opciones']['dark'],
        path=pathim,area=trim,sec=ov)
        
#%%  
    '''
    Fotometria
    '''
    if data['fotometria']['dofotometria']:  # if dofotometria
        images=data['fotometria']['imobj']  # get images
        path2=data['fotometria']['path']    # get path
        if data['fotometria']['opciones']['buscarest']:   # if buscar est
            #busca estrellas
            
            if data['fotometria']['opciones']['autocielo']: # if autocielo
                cielo=skynoises(images,path=path2) #obtiene array de skynoise
            else:                                           # else lee file
                cielo=data['fotometria']['opciones']['cielo']

            if data['fotometria']['opciones']['autofwhm']:  # if autofwhm
                fw=multifull(images,path=path2)             #calcula array fwhm
            else:                                           # else lee file
                fw=data['fotometria']['opciones']['fwhm']
                
            tres=data['fotometria']['opciones']['tr']       # get treshold
            
            # busca las estrellaas.
            multisf(images,farr=2*fw,sarr=cielo,thold=tres,path=path2)
            cords='coords.in'   # auto value
            pathc=path2         # auto value
        else:                                      # else lee file para coords
            cords=data['fotometria']['opciones']['coords']   # user input
            pathc=data['fotometria']['opciones']['pathc']    # user input             
            
        an=data['fotometria']['opciones']['annulus']    # get annulus
        dan=data['fotometria']['opciones']['dannulus']  # get dannulus
        if data['fotometria']['opciones']['autoapertura']:   # if auto aper
            fwhm=np.unique(fw)
            fwhm=round(fwhm[0],1)
            ap=str(fwhm)+','+str(2*fwhm)  # redondeo a un decimal
            
        else:
            ap=data['fotometria']['opciones']['apertura']    # else lee file
        photom(images,an,dan,ap,path=pathc,coords=cords)
            #%%
    '''
    Tabla
    '''
    if data['tabla']['dotabla']:
        path3=data['tabla']['path']
        form=data['tabla']['opciones']['formato']
        esque=data['tabla']['opciones']['esquema']
        gentable(data['tabla']['phouts'],formato=form,tabesq=esque,path=path3)
        
        
    print('\n' + Fore.YELLOW + 'WOW')
    print(Style.RESET_ALL)
#%%
  
if __name__== "__main__":
    print(Fore.MAGENTA + 'Bienvenidx a la versión vintage de WOW!')
    print(Style.RESET_ALL)
    main()
