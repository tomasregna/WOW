#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:09:36 2019

@author: guevaran
"""
#%%

import os
from pyraf import iraf
os.system('ds9 -fifo dev/imt1 &')


#%%
def photom(images,coords,path=None)
    iraf.noao()
    iraf.digiphot()
    iraf.apphot()

    iraf.datapars.ccdread="rdnoise"
    iraf.datapars.gain="gain"
    iraf.datapars.exposure="exptime"
    iraf.datapars.airmass="airmass"
#    iraf.datapars.filter="filter"
    iraf.datapars.obstime="time-obs"
    iraf.fitskypars.annulus=30
    iraf.fitskypars.dannulus=5
    iraf.photpars.apertures="0.5,1:30:1"

    if os.path.exists('phot.out'):
        os.remove('phot.out')
    
    if (os.path.splitext(images)[-1] == '.fit' or
        os.path.splitext(images)[-1] == '.fits'):
        iraf.phot.image=images
        iraf.phot.coords=coords
    iraf.phot.output='phot.out'
    iraf.phot.interac='no'
    iraf.phot()

#%%

    for i in range(1,4):
        name='star'+ str(i) + '.tab'
        if os.path.exists(name):
            os.remove(name)
        f=open(name,'w+')
        for j in range(1,32):
            fields="Id,Rapert["+str(j)+"],Mag["+str(j)+"],Merr["+str(j
                             )+"],Area["+str(j)+"],Flux["+str(j
                             )+"],Annulus,Dannulus,MSky,Stdev,NSky,Sum["+str(j
                             )+"],XCenter,YCenter"
            iraf.txdump.fields=fields
            test=iraf.txdump("phot.out",expr="Id == "+str(i),headers='no',Stdout=1)
            print >> f,test[0]
        f.close()
#%%
