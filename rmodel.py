#Andrew Shao, 2016
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.io import fits #you can also use the package pyfits
import py_specrebin
from astropy.stats import sigma_clip
import math
import pdb
from astropy.convolution import Gaussian1DKernel, convolve
from sys import argv
import pyfits as pf

data = open('/Users/Andrew/Dropbox/VDGC_students/catalogs/model_user.dat')

hbeta = [] #Hbeta
mgb = [] #Mgb5177
age = [] #age
met = [] #metallicity
counter = 0

#plot is of mgb5177 vs hbeta, sorted by their ages and metallicities (mets) - objects with same age and met connected
#purpose is to plot the orphan GCs' mgb5177 and hbeta values to determine their age and metallicity - used a library of models

for line in data:

    ls = line.strip()

    counter += 1
    if counter <= 1:
        continue
	
    ds = line.split()
    
    #only retains necessary objects
    if float(ds[1]) == -2.27 or float(ds[1]) == -0.35 or float(ds[1]) == -1.26 or float(ds[1]) == -1.49 or float(ds[2]) == 0.4 or (float(ds[0]) != 0.7 and float(ds[0]) != 1.0 and float(ds[0]) != 1.5 and float(ds[0]) != 2.0 and float(ds[0]) != 2.75 and float(ds[0]) != 3.5 and float(ds[0]) != 5.0 and float(ds[0]) != 6.5 and float(ds[0]) != 8.0 and float(ds[0]) != 10.0 and float(ds[0]) != 14.0):
        continue

    age.append(float(ds[0])) #column 0 - age
    met.append(float(ds[1])) #column 1 - met
    hbeta.append(float(ds[20])) #column 20 - hbeta
    mgb.append(float(ds[29])) #column 29 - mgb

data.close()

#purpose: join points with same age with a line, join points with same met with a line
age_h = [[] for x in range(0, 11)] #hbetas of the same age
age_m = [[] for x in range(0, 11)] #mgbs of the same age
ages = [0.7, 1, 1.5, 2, 2.75, 3.5, 5, 6.5, 8, 10, 14] #array of all the ages used
met_h = [[] for x in range(0, 8)] #2d array with each column containing hbetas of the same met
met_m = [[] for x in range(0, 8)] #mgbs of the same met 
mets = [-1.79, -0.96, -0.66, -0.25, 0.06, 0.15, 0.26, 0.4] #array of all the mets used
#age_h and met_h have the same data points (bc using hbeta for both) but they're sorted differently, same for mgb

#sorts hbeta data and mgb data into the 2d arrays based on similar age/metallicty
for x in range(0, 11):
    for z in range(0, 88): 
         if ages[x] == age[z]: #if an object's age at index z matches an age at index x...  
            age_h[x].append(hbeta[z]) 
            age_m[x].append(mgb[z])
for x in range(0, 8):
    for z in range(0, 88):
         if mets[x] == met[z]: #sorts the objects in a different order
            met_h[x].append(hbeta[z])
            met_m[x].append(mgb[z])
            
plt.clf()
fig=plt.figure()

plt.errorbar(1.8992, 2.451, 0.1984, 0.2531, 'bo', label = 'Blue Orphan GCs') #blue GCs
plt.errorbar(0.9218, 2.3944, 0.1471, 0.1822,'yo', label = 'Blue Satellite GCs')

plt.legend(loc = 'upper right', numpoints = 1)

for m in range(0, 11):
    plt.plot(age_m[m], age_h[m], 'k.', linestyle = 'dashed')
    plt.annotate(ages[m], (age_m[m][-1], age_h[m][-1]), fontsize = 8)
for m in range(0, 8):
    plt.plot(met_m[m], met_h[m], 'k.', linestyle = ':')
#labels each line with its respective age/metallicity
plt.annotate(mets[0], (met_m[0][-1], met_h[0][-1]), xytext = (met_m[0][-1]-0.4, 2.6), fontsize = 8)
plt.annotate(mets[1], (met_m[1][-1], met_h[1][-1]), xytext = (met_m[1][-1]-0.2, 2.3), fontsize = 8)
plt.annotate(mets[2], (met_m[2][-1], met_h[2][-1]), xytext = (met_m[2][-1]-0.2, 2), fontsize = 8)
plt.annotate(mets[3], (met_m[3][-1], met_h[3][-1]), xytext = (met_m[3][-1]-0.2, 1.7), fontsize = 8)
plt.annotate(mets[4], (met_m[4][-1], met_h[4][-1]), xytext = (met_m[4][-1]-0.3, 1.5), fontsize = 8)
plt.annotate(mets[5], (met_m[5][-1], met_h[5][-1]), xytext = (met_m[5][-1]-0.2, 1.5), fontsize = 8)
plt.annotate(mets[6], (met_m[6][-1], met_h[6][-1]), xytext = (met_m[6][-1]-0.1, 1.5), fontsize = 8)
plt.annotate(mets[7], (met_m[7][-1], met_h[7][-1]), xytext = (met_m[7][-1]-0.15, 1.4), fontsize = 8)

plt.xlabel('Mgb5177 (Angstroms)', fontsize='20') #labels x axis
plt.ylabel('H-beta (Angstroms)', fontsize='20') #labels y axis
plt.text(1.5, 5.8, 'Age (billions of years)', fontsize = '15')
plt.text(0.3, 1.8, 'Metallicity', fontsize = '15')
plt.title('Stellar Population Synthesis Model\n of Blue Orphan GCs and Blue Satellite GCs', fontsize = "18")
plt.tight_layout
plt.savefig('/Users/Andrew/Dropbox/VDGC_students/plots/rmodel.png')  
