import numpy as np
import matplotlib.pyplot as plt

path = 'C:/Users/Christopher Plumberg/Desktop/Research/UIUC/'+\
       'HydroCausalityChecks/resultsFiles/'
filename = path + 'PbPb_2760GeV_epsilon-u-Hydro-t0.1-0.dat'
filename = path + 'initial.dat'

fig, ax = plt.subplots( nrows=1, ncols=1 )

dxy = 0.08
nx = ny = 512
dx = dxy
dy = dxy

# Get the data
data = np.loadtxt(filename, skiprows=1, usecols=(1, 2, 3))

maxED = np.amax(data[:,2])
#data[:,2] /= maxED
print(maxED)
#print(np.amax(data[:,2]))
#print(np.amin(data[:,2]))

data = data[np.where((np.abs(data[:,0])<=15.774) & (np.abs(data[:,1])<=15.774))]
nx = ny = int(np.sqrt(data.size/3))

data = data.reshape([nx, ny, 3])
#print(data.shape)

im = ax.imshow(data[:,:,2], interpolation='nearest', \
          origin='lower', extent=[-0.5*nx*dx, 0.5*nx*dx, -0.5*ny*dy, 0.5*ny*dy],
          cmap=plt.get_cmap('gnuplot'), vmin=0.0, vmax=352.0)
                          
ax.set_xlabel(r'$x$ (fm)', fontsize=16)
ax.set_ylabel(r'$y$ (fm)', fontsize=16)

plt.colorbar(im, label=r'e [GeV/fm$^3$]')

plt.show()
#outfilename = path + 'initial_McGill.pdf'
#print('Saving to', outfilename)
#fig.savefig(outfilename, bbox_inches='tight')
#plt.close(fig)
