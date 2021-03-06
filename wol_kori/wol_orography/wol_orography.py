import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm

df = pd.read_csv('wol_16dir.csv',
                    sep = ",",
                    header = None,
                    engine = 'python')

df = np.array(df)

index = df[0,0:59]
index=index.astype(int)

orography = np.zeros((16,len(index)))
#orography = df[1:17,0:59]

orography_new = np.zeros((16,len(index)))
for i in range(16):
    if i <= 7:
        orography_new[i+8,:] = orography[i,:]
    elif i > 7:
        orography_new[i-8,:] = orography[i,:]

orography = orography_new

# comment-out below here (no figure)
"""
minoro = np.amin(orography)
maxoro = np.amax(orography)
locateoro = np.where(orography == maxoro)
print('maxoro is ',maxoro)
print('distance is ',index[locateoro[1]])
print('direction is ',locateoro[0])

# 2D surface plot
azimuths = np.radians(np.linspace(0, 360, 17))
zeniths = index[0:59]

r, theta = np.meshgrid(zeniths, azimuths)
values = np.zeros((azimuths.size, zeniths.size))
###################################################################
for k in range(len(zeniths)):
    for l in range(len(azimuths)-1):
        # Wind direction is opposite to dispersion direction
        if l <= 7:
            values[l+8,k] = orography[l,k] ## select xoq or doq
        elif l > 7:
            values[l-8,k] = orography[l,k] ## select xoq or doq
    values[16,k] = orography[8,k]
###################################################################

fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))

# Set clockwise polar coordinate
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

##################################################################
## colorbar level setting
lev = [c for c in np.arange(minoro,maxoro*1.1,(maxoro-minoro)/10, dtype=float)]
# lev1 = [c*10**-7 for c in np.arange(0,1.1,0.1, dtype=float)]
##################################################################

cs = ax.contour(theta, r, values, levels = lev, cmap = 'gray')
cbaxes = fig.add_axes([0.88, 0.1, 0.03, 0.8]) 
cbar = fig.colorbar(cs, cax = cbaxes)

plt.show()
"""