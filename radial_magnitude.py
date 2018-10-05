#Andrew Shao, 2016
#Plots radial distribution vs apparent i magnitude

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 
from astropy.io import ascii
from astropy.io import fits
from astropy.stats import sigma_clip
import math
import pdb

#arrays for blue GCs 
RA_b = [] #to find distance to M87 
DEC_b = [] #to find distance to M87 
R_b = [] #distance to M87
i_b = [] #imag 

#arrays for red GCs
R_r = [] #distance to M87 
RA_r = [] #to find distance to M87 
DEC_r = [] #to find distance to M87 
i_r = [] 

#arrays for orphans
RA_orphan = [] #to find distance to M87 
DEC_orphan = [] #to find distance to M87 
R_orphan = [] #distance to M87 
i_orphan = [] 

#information about M87
RA_M87 = 187.7058 
DEC_M87 = 12.3911

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
    
    #adds imag data to the array from blue GC catalog's column 5
    i_b.append(float(ds[5]))

blue.close()

#open red GCs catalog
red = open('/Users/Andrew/Dropbox/VDGC_students/catalogs/m87rgc_radc_photvelrh_ZH15.dat')

#for loop to access data of blue GCs and add to arrays
for line in red:

    ls = line.strip()

    #skips the line if it's a comment
    if line.startswith('#'):
        continue
	
	#split the lines from the text into an array  
    ds = line.split()
    
    #adds RA data to the array from red GC catalog's column 0
    RA_r.append(float(ds[0]))

    #adds DEC data to the array from red GC catalog's column 1
    DEC_r.append(float(ds[1]))

    #adds imag data to the array from red GC catalog's column 5
    i_r.append(float(ds[5]))

red.close()

#open orphans catalog
data = open('/Users/Andrew/Dropbox/VDGC_students/results/orphan_data.dat')

#for skipping lines that are not comments
counter = 0

#for loop to access data of orphans and add to arrays
for line in data:

    ls = line.strip()

    #skips the line if it's a comment
    if line.startswith('#'):
        continue

    #skips the first line
    counter += 1
    if counter <= 1: 
        continue

    #split the lines from the text into an array  
    ds = line.split()

    #adds RA data to the array from orphans catalog column 6
    RA_orphan.append(float(ds[6]))

    #adds DEC data to the array from orphans catalog column 7
    DEC_orphan.append(float(ds[7]))
    
    #adds imag data to the array from orphans catalog column 9
    i_orphan.append(float(ds[9]))

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

#delete orphans with no photometry
for i in range(0, 45):
    if i_orphan[i] < 1:
        del i_orphan[i]
        del R_orphan[i]

#pdb.set_trace()
    

plt.clf()
fig = plt.figure()  

#plots blue GCs as blue squares, x = distance from M87
plt.plot(R_b, i_b, 'bs', label = 'Blue GCs', markersize = '3')

#plots red GCs as red stars, x = distance from M87
plt.plot(R_r, i_r, 'r*', label = 'Red GCs', markersize = '4') 

#plots orphans as yellow triangles, x = distance from M87
plt.plot(R_orphan, i_orphan, 'y^', label = 'Orphan GCs', markersize = '9')


plt.xlabel(r'R$_{av}$ (arcmin)',fontsize = '15') #average radius from M87 in arcminutes
plt.ylabel(r'i$_{o}$ (mag)',fontsize = '15')
#plt.title(, fontsize = '20') #average radius from M87 in kiloparsecs 

plt.xscale('log')

plt.gca().invert_yaxis()
 
plt.legend(loc = 'lower left', numpoints = 1)
plt.title(r'Distribution of GCs in Projected Distance vs. Apparent i$_{0}$ Magnitude Space', fontsize = '15')
plt.tight_layout
plt.savefig('/Users/Andrew/Dropbox/VDGC_students/plots/Fig_5.png')
plt.show()
    
pdb.set_trace()
