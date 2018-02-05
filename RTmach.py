# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:19:02 2016
calcualte mach number at interface
https://ac.els-cdn.com/S0021999115007354/1-s2.0-S0021999115007354-main.pdf?_tid=6b352868-b805-11e7-a777-00000aacb35f&acdnat=1508772087_e2113d86ae1e7aa2636bc1bcdfe6484b

designed for single mode
@author: Xin
"""

import h5py
import numpy as np
import pylab
import matplotlib.pyplot as plt

istep = '889000'
g = 1.0
Lz = 3.2
variable = ['PVy','PVz','PPress', 'Prho']
gamma=1.0
delimiter =''
h5file = h5py.File('./temp.h5','r')
#read dataset dimensions
mylist = ['Fields/','Prho','/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)
nz=m1.shape[0]
ny=m1.shape[1]
nx=m1.shape[2]
dx = dy = dz = Lz/nz

#pressure  
mylist = ['Fields/','PPress','/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
press = np.array(databk)
#rho  
mylist = ['Fields/','Prho','/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
rho = np.array(databk)
#PVy
mylist = ['Fields/','PVy','/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
vy = np.array(databk)

#PVz
mylist = ['Fields/','PVz','/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
vz = np.array(databk)


cs = (gamma*press/rho)**0.5
mach = (vz**2+vy**2)**0.5/cs

delimiter = ''		
mylist = ['Fields/','Ma','/',istep]
filepath = delimiter.join(mylist)
h5new.create_dataset(filepath,data=mach)

dzVz = np.gradient(vz, dz, axis=0)
dyVy = np.gradient(vy, dy, axis=1)
div = dzVz + dyVy
mylist = ['Fields/','Div','/',istep]
filepath = delimiter.join(mylist)
h5new.create_dataset(filepath,data=div)








h5file.close()
    
    
    
