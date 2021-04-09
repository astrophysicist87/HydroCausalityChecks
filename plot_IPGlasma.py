import numpy as np
import matplotlib.pyplot as plt

path = 'C:/Users/Christopher Plumberg/Desktop/Research/UIUC/'+\
       'HydroCausalityChecks/all_results_v8/'
filename = path + 'epsilon-u-Hydro-t0.4-0.dat'
#filename = path + 'PbPb_2760GeV_newGrid_epsilon-u-Hydro-t0.1-0.dat'
#filename = path + 'initial.dat'

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
print('Total=',np.sum(data[:,2])*dxy**2)
#print(np.amax(data[:,2]))
#print(np.amin(data[:,2]))

data = data[np.where((np.abs(data[:,0])<=12.906) & (np.abs(data[:,1])<=12.906))]
nx = ny = int(np.sqrt(data.size/3))

data = data.reshape([nx, ny, 3])
#print(data.shape)

im = ax.imshow(data[:,:,2], interpolation='nearest', \
          origin='lower', extent=[-0.5*nx*dx, 0.5*nx*dx, -0.5*ny*dy, 0.5*ny*dy],
          cmap=plt.get_cmap('gnuplot'))
                          
ax.set_xlabel(r'$x$ (fm)', fontsize=16)
ax.set_ylabel(r'$y$ (fm)', fontsize=16)

cbar = plt.colorbar(im, label=r'e [GeV/fm$^3$]')
#cbar.set_ticks(range(0,400,50))
#newTickLabels = [x for x in range(0,400,50)]
#newTickLabels[-1] = r'$\geq 350$'
#cbar.set_ticklabels(newTickLabels)


#plt.show()
outfilename = path + 'initial_IPglasma.png'
print('Saving to', outfilename)
fig.savefig(outfilename, bbox_inches='tight', dpi=300)
plt.close(fig)
