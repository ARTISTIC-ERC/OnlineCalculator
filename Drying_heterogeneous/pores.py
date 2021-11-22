import numpy as np
import glob
#from skimage.external import tifffile as tif
#from random import seed
#from random import random
import itertools
#from scipy import ndimage
#import matplotlib.pyplot as plt
from numba import njit
#import time


@njit
def get_array_from_data(data,npar,lxm,lxp,lym,lyp,lzm,lzp):
      #Define array that has 1 values if inside sphere and 0 if outside
      # Define mesh
      lx = lxp - lxm
      ly = lyp - lym
      lz = lzp - lzm
      
      count = 0
      ncol = 5

      tmp_data = np.zeros((100*npar,1*ncol),dtype=np.float32)

# To understand
      tmp_data[:npar,0] = data[:,0]
      tmp_data[:npar,1] = data[:,1]
      tmp_data[:npar,2] = data[:,2]
      tmp_data[:npar,3] = data[:,3]
      tmp_data[:npar,4] = data[:,4]

      ni1 = 0
      ni2 = npar

      for i in np.arange(3):

            count1 = 0
            count += 1

            for j in np.arange(ni1,ni2):

                  count1 += 1
                  particle = tmp_data[j,:]

                  #Set Masks for PBC
                  xp = (particle[0] + (particle[3])) > lxp and ((particle[0]-lx) < lxm)
                  xn = (particle[0] - (particle[3])) < lxm and ((particle[0]+lx) > lxp)
                  yp = (particle[1] + (particle[3])) > lyp and ((particle[1]-ly) < lym)
                  yn = (particle[1] - (particle[3])) < lym and ((particle[1]+ly) > lyp)
                  zp = (particle[2] + (particle[3])) > lzp and ((particle[2]-lz) < lzm)
                  zn = (particle[2] - (particle[3])) < lzm and ((particle[2]+lz) > lzp) # Here there were 0 instead of 2, typo?
                  #Is particle close to a border such that it needs PBC?
                  #Face Images (6 faces)
                  if xp:
                        tmp_data[npar,0] = particle[0] - lx
                        tmp_data[npar,1] = particle[1]
                        tmp_data[npar,2] = particle[2]
                        tmp_data[npar,3] = particle[3]
                        tmp_data[npar,4] = particle[4]
                        npar += 1
                  elif xn:
                        tmp_data[npar,0] = particle[0] + lx
                        tmp_data[npar,1] = particle[1]
                        tmp_data[npar,2] = particle[2]
                        tmp_data[npar,3] = particle[3]
                        tmp_data[npar,4] = particle[4]
                        npar += 1
                  if yp:
                        tmp_data[npar,0] = particle[0]
                        tmp_data[npar,1] = particle[1] - ly
                        tmp_data[npar,2] = particle[2]
                        tmp_data[npar,3] = particle[3]
                        tmp_data[npar,4] = particle[4]
                        npar += 1
                  elif yn:
                        tmp_data[npar,0] = particle[0]
                        tmp_data[npar,1] = particle[1] + ly
                        tmp_data[npar,2] = particle[2]
                        tmp_data[npar,3] = particle[3]
                        tmp_data[npar,4] = particle[4]
                        npar += 1
#                  if zp:
#                        tmp_data[npar,0] = particle[0]
#                        tmp_data[npar,1] = particle[1]
#                        tmp_data[npar,2] = particle[2] - lz
#                        tmp_data[npar,3] = particle[3]
#                        tmp_data[npar,4] = particle[4]
#                        npar += 1
#                  elif zn:
#                        tmp_data[npar,0] = particle[0]
#                        tmp_data[npar,1] = particle[1]
#                        tmp_data[npar,2] = particle[2] + lz
#                        tmp_data[npar,3] = particle[3]
#                        tmp_data[npar,4] = particle[4]
#                        npar += 1

            ni1 = ni2
            ni2 = npar

      return tmp_data[:npar,:]

@njit
def get_image(data,npar,vox,lxm,lxp,lym,lyp,lzm,lzp):

      lx = lxp - lxm
      ly = lyp - lym
      lz = lzp - lzm
      x_ = np.linspace(lxm,lxp,int(lx/vox))
      y_ = np.linspace(lym,lyp,int(ly/vox))
      z_ = np.linspace(lzm,lzp,int(lz/vox))

      M = np.zeros((x_.size,y_.size,z_.size),dtype=np.int_)

      zi = 0
      for z in z_:
            yi = 0
            for y in y_:
                  xi = 0
                  for x in x_:

                        for i in np.arange(npar):

                              particle = data[i,:]
                              I = (x-particle[0])**2 + (y-particle[1])**2 + (z-particle[2])**2 < (particle[3])**2

                              #Here I am missing something
                              if I and (int(particle[4]) <= 3):
                                    M[xi,yi,zi] += 1
                              elif I and (int(particle[4]) > 3):
                                    M[xi,yi,zi] += 100
                              #elif I and (int(particle[4]) == 7):
                              #      M[xi,yi,zi] += 10000

                        xi += 1
                  yi += 1
            zi += 1
           
      return M

def read_data(filename):
      #Read LAMMPS data file
      with open(filename,'r') as f:
            dum = f.readline()
            dum = f.readline()
            dum = f.readline()
            dum = dum.split()
            npar = int(dum[0])
            dum = f.readline()
            dum = dum.split()
            ntype = int(dum[0])
            dum = f.readline()
            dum = f.readline()
            dum = dum.split()
            Lxm = float(dum[0])
            Lxp = float(dum[1])
            dum = f.readline()
            dum = dum.split()
            Lym = float(dum[0])
            Lyp = float(dum[1])
            dum = f.readline()
            dum = dum.split()
            Lzm = float(dum[0])
            Lzp = float(dum[1])
            dum = f.readline()
            dum = f.readline()
            dum = f.readline()
            masses = np.genfromtxt(itertools.islice(f,ntype),dtype="i,f8",names=['ntype','mass'])
            dum = f.readline()
            dum = f.readline()
            dum = f.readline() 
            particles = np.genfromtxt(itertools.islice(f,npar),dtype="i,i,f8,f8,f8,f8,f8,f8,3i",names=['num','ntype','x','y','z','charg','r','rho','dum'])

            return [npar,Lxm,Lxp,Lym,Lyp,Lzm,Lzp,particles]

def read_dump(filename):
	#Read LAMMPS data file
	with open(filename,'r') as f:
		dum = f.readline()
		dum = f.readline()
		dum = f.readline()
		dum = f.readline()
		dum = dum.split()
		npar = int(dum[0])
		dum = f.readline()
		dum = f.readline()
		dum = dum.split()
		Lxm = float(dum[0])
		Lxp = float(dum[1])
		dum = f.readline()
		dum = dum.split()
		Lym = float(dum[0])
		Lyp = float(dum[1])
		dum = f.readline()
		dum = dum.split()
		Lzm = float(dum[0])
		Lzp = float(dum[1])
		dum = f.readline()
		particles = np.genfromtxt(itertools.islice(f,npar),dtype="f8,f8,f8,f8,f8,f8",names=['num','ntype','x','y','z','radius'])

	return [npar,Lxm,Lxp,Lym,Lyp,Lzm,Lzp,particles]

#start_time = time.process_time()

filename = 'Dried_electrode.atom'
data = read_dump(filename)

################### PRISTINE ELECTRODE ######################
npar = data[0]
Lxm = data[1]
Lxp = data[2]
Lym = data[3]
Lyp = data[4]
Lzm = data[5]
Lzp = data[6]
particles = data[7]

part = np.zeros((npar,5), dtype=float)

part[:,0] = particles['x']
part[:,1] = particles['y']
part[:,2] = particles['z']
part[:,3] = particles['radius']
part[:,4] = particles['ntype']

voxel = 0.2

M = get_array_from_data(part,npar,Lxm,Lxp,Lym,Lyp,Lzm,Lzp)

npar_ghost = np.shape(M)[0]

#Calculate highest z value 
zmax = np.amax(part[:,2])
#npar_ghost = np.shape(atoms)[0]

C = get_image(M,npar_ghost,voxel,Lxm,Lxp,Lym,Lyp,Lzm,zmax)

mask1 = C > -0.1
mask2 = C < 0.1

mask = mask1 & mask2

C[mask] = 0

mask3 = C > 0.4
mask4 = C < 99.99

mask = mask3 & mask4

C[mask] = 1

mask5 = C > 99.99
mask6 = C < 9999.99

mask = mask5 & mask6

C[mask] = 2

#mask7 = C > 9999.99
#mask8 = C < 1e30

#mask = mask7 & mask8

#C[mask] = 3


#FOR CALCULATING POROSITY
#COUNT UNIQUE LABELS IN C
unique, counts = np.unique(C, return_counts=True)
uqvals = np.asarray((unique, counts)).T

#Recover the new CBD nanoporosity
path_nanon = r'CBD_nanoporosity_ini'
with open(path_nanon, 'r') as f:
    lines = f.readlines()
    f.close()

nano = float(lines[0])

#CALCULATE NUMBER OF VOXELS OF EACH TYPE

path_new = r'porosity_bulk.out'
path_new2 = r'porosity_all.out'
path_new3 = r'check.txt'


o = open(path_new, 'a')
p = open(path_new2, 'a')
q = open(path_new3, 'a')
q.write("bulk_pores, CBD, AM \n")

totvol = np.sum(uqvals,axis=0)[1]
bulk_pore = ((uqvals[0,1])/totvol)*100
overall_pores = ((uqvals[0,1] + nano*uqvals[1,1])/totvol)*100
CBD_vol = ((uqvals[1,1])/totvol)*100
AM_vol = ((uqvals[2,1])/totvol)*100

o.write(str(bulk_pore))
p.write(str(overall_pores))
q.write(str(bulk_pore) + ',' + str(CBD_vol) + ',' + str(AM_vol))

o.close()
p.close()
q.close()

#tif.imsave('coord_min_param1_numba.tif', C)

#print(str(time.process_time() - start_time) + " seconds")
