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

istep = '000005'
Lz=0.08
Ly=0.01
g = 1.0
waveLen = Ly
variable = ['PVx','PVy','PVz','PPress', 'Prho']
gamma=1.66667
delimiter =''
h5file = h5py.File('tests_single_new.h5','r')
#read dataset dimensions
mylist = ['Fields/','Prho','/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)
nz=m1.shape[0]
ny=m1.shape[1]
nx=m1.shape[2]
dz=Lz/nz

#inteface postion wrt grid points
z0 = 10*nz/16
machGiven = 1.2
#define in spike line
#density at interface
rho = (m1[z0, ny/2-1, 0] + m1[z0-1, ny/2-1, 0])/2
rho = 0.8
#pressure  
mylist = ['Fields/','PPress','/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)
press = (m1[z0, ny/2-1, 0] + m1[z0-1, ny/2-1, 0])/2
pressTop = m1[nz-1,ny/2-1,0]
wave = (g*waveLen)**0.5
cs = (gamma*press/rho)**0.5
mach = wave/cs
print 'mach number at interface is:', mach



#####given mach number calculate pressure needed
pressNeed = rho*g*waveLen/(gamma*machGiven**2)
print 'the pressure and density at interface is:', press, rho
print 'for Mach=', machGiven, "the pressure needed is:", pressNeed
print 'you need add to the pressure intial constant:', pressNeed - press

print 'pressure at top is:', pressTop




h5file.close()
    
    
    
