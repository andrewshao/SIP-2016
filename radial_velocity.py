#Andrew, 2016
#Plots radial velocities of blue and red orphan GCs

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 
from astropy.io import ascii
from astropy.io import fits
#import py_specrebin -- Error
from astropy.stats import sigma_clip
import math
import pdb

#arrays for blue GCs 
RA_b = [] #to find distance to M87 
DEC_b = [] #to find distance to M87 
R_b = [] #distance to M87
Vel_b = [] #velocity 

#arrays for red GCs
R_r = [] #distance to M87 
RA_r = [] #to find distance to M87 
DEC_r = [] #to find distance to M87 
Vel_r = [] #velocity

#arrays for orphans
RA_orphan = [] #to find distance to M87 
DEC_orphan = [] #to find distance to M87 
R_orphan = [] #distance to M87 
Vel_orphan = []  #velocity

#information about M87
RA_M87 = 187.7058 
DEC_M87 = 12.3911
Vel_M87 = 1307 #velocity

#open blue GCs catalog
blue = open('/Users/Andrew/Dropbox/VDGC_students/catalogs/m87bgc_radc_photvelrh_ZH15.dat')

#for loop to access data of blue GCs and add to arrays
for line in blue:

    ls = line.strip()

    #skips the line if it's a comment
    if line.startswith('#'):
        continue
	
	#split the lines from the text into an array  
    ds = line.split()

    #adds RA data to the array from blue GC catalog's column 0
    RA_b.append(float(ds[0]))
    
    #adds DEC data to the array from blue GC catalog's column 1
    DEC_b.append(float(ds[1]))
    
    #adds velocity data to the array from blue GC catalog's column 9
    Vel_b.append(float(ds[9]))

blue.close()

#open red GCs catalog
red = open('/Users/Andrew/Dropbox/VDGC_students/catalogs/m87rgc_radc_photvelrh_ZH15.dat')

#for loop to access data of blue GCs and add to arrays
for line in red:

    ls = line.strip()

    if line.startswith('#'):
        continue
	 
    ds = line.split()
    
    #adds RA data to the array from red GC catalog's column 0
    RA_r.append(float(ds[0]))

    #adds DEC data to the array from red GC catalog's column 1
    DEC_r.append(float(ds[1]))

    #adds velocity data to the array from red GC catalog's column 9
    Vel_r.append(float(ds[9]))

red.close()

#open orphans catalog
data = open('/Users/Andrew/Dropbox/VDGC_students/results/orphan_data.dat')

#for skipping lines that are not comments
counter = 0

#for loop to access data of orphans and add to arrays
for line in data:

    ls = line.strip()

    if line.startswith('#'):
        continue

    #skips the first line
    counter += 1
    if counter <= 1: 
        continue
	
    ds = line.split()

    #adds RA data to the array from orphans catalog column 6
    RA_orphan.append(float(ds[6]))

    #adds DEC data to the array from orphans catalog column 7
    DEC_orphan.append(float(ds[7]))

    #adds velocity data to the array from orphans catalog column 2
    Vel_orphan.append(float(ds[2]))

data.close()
 
#for loop to calculate distance from each blue GC to center of M87 in arcminutes
for n in range(0, 683):
    R_b.append(60*math.sqrt(((RA_M87-RA_b[n])*np.cos(np.radians(DEC_M87)))**2+(DEC_M87-DEC_b[n])**2))

#for loop to calculate distance from each red GC to center of M87 in arcminutes
for p in range(0, 228):
    R_r.append(60*math.sqrt(((RA_M87-RA_r[p])*math.cos(np.radians(DEC_M87)))**2+(DEC_M87-DEC_r[p])**2))

#for loop to calculate distance from each orphan to center of M87 in arcminutes
for m in range(0, 47):
    R_orphan.append(60*math.sqrt(((RA_M87-RA_orphan[m])*math.cos(np.radians(DEC_M87)))**2+(DEC_M87-DEC_orphan[m])**2))

plt.clf()
fig = plt.figure()  

#to make horizontal dashed line -- systemic radial velocity of M87 -- 1307 km s−1 (Binggeli et al. 1993)
plt.axhline(y = Vel_M87, xmin = 0, xmax = 100, linestyle = 'dashed')

#plots orphans as green triangles, x = distance from M87, y = velocity
plt.plot(R_orphan, Vel_orphan, 'g^', label = 'Orphan GCs', markersize = '9')

plt.xlabel(r'R$_{av}$ (arcmin)',fontsize = '20') #average radius from M87 in arcminutes
plt.ylabel(r'V$_{los}$ (km/s)',fontsize = '20') #velocity
plt.title('Radial Velocity Dispersion')

plt.xscale('log')
 
plt.legend(loc = 'upper left', numpoints = 1)

plt.tight_layout
plt.savefig('/Users/Andrew/Dropbox/VDGC_students/plots/Fig_7_presentation_version.png', dpi=100)
plt.show()
    
pdb.set_trace()
