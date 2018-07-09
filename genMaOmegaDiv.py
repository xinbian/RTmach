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

g = 1.0
Lz = 3.2
gamma=1.0
specout = 1000
totalsteps = 170000
step = []
for i in range(totalsteps/specout):
    step.append(str((i+1)*specout).zfill(6))
delimiter =''
h5file = h5py.File('tests_single_new.h5','r')
h5new = h5py.File('div_vorticiy.h5','w') 
#read dataset dimensions
mylist = ['Fields/','Prho','/','002000']
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)
nz=m1.shape[0]
ny=m1.shape[1]
nx=m1.shape[2]
dx = dy = dz = Lz/nz


for istep in step:

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
	mylist = ['Fields/','PMa','/',istep]
	filepath = delimiter.join(mylist)
	h5new.create_dataset(filepath,data=mach)



	dzVy = np.gradient(vy, dz, axis=0)
	dyVz = np.gradient(vz, dy, axis=1)
	dzVz = np.gradient(vz, dz, axis=0)
	dyVy = np.gradient(vy, dy, axis=1)

	div = dzVz + dyVy

	mylist = ['Fields/','PDiv','/',istep]
	filepath = delimiter.join(mylist)
	h5new.create_dataset(filepath,data=div)
	

	#omega 
	
	dyVz = np.gradient(vz, dy, axis=1)
	dzVy = np.gradient(vy, dz, axis=0)
	
	omega_x = dyVz - dzVy
	
	mylist = ['Fields/','POmex','/',istep]
	filepath = delimiter.join(mylist)
	h5new.create_dataset(filepath,data=omega_x)
	
	
	if nx != 1:
		dyVx = np.gradient(vx, dy, axis=1)
		dzVx = np.gradient(vx, dz, axis=0)
		dxVy = np.gradient(vy, dx, axis=2)
		dxVz = np.gradient(vz, dx, axis=2)
		
		omega_y = dzVx - dxVz
		omega_z = dxVy - dyVx
		
		mylist = ['Fields/','POmey','/',istep]
		filepath = delimiter.join(mylist)
		h5new.create_dataset(filepath,data=omega_y)
		
		mylist = ['Fields/','POmez','/',istep]
		filepath = delimiter.join(mylist)
		h5new.create_dataset(filepath,data=omega_z)
	
	
	
	print('progress:', float(istep)/totalsteps*100, '%')







h5file.close()
h5new.close()
    
    
