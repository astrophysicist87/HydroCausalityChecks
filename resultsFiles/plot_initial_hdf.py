import h5py
import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

filename = 'C:/Users/Christopher Plumberg/Desktop/Research/UIUC/initial.hdf'

fig, ax = plt.subplots( nrows=1, ncols=1 )

with h5py.File(filename, "r") as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = np.array(f[a_group_key])
    
    dxy = 0.1434
    nx = ny = 110
    dx = dxy
    dy = dxy
    
    #print(data.shape)
    #print(np.amax(data[:,2]))
    #print(np.amin(data[:,2]))
    
    ev = f['event_0']
    print(ev.attrs.keys())
    
    ax.imshow(data, interpolation='nearest', \
              origin='lower', extent=[-nx*dx, nx*dx, -ny*dy, ny*dy],
              cmap=plt.get_cmap('gnuplot'))
                  
    #plt.text(0.075, 0.925, r'$\tau = %(t)5.2f$ fm$/c$'%{'t': tau}, \
    #        {'color': 'white', 'fontsize': 12}, transform=ax.transAxes,
    #        horizontalalignment='left', verticalalignment='top')
            
    ax.set_xlabel(r'$x$ (fm)', fontsize=16)
    ax.set_ylabel(r'$y$ (fm)', fontsize=16)
    
    plt.show()
    #outfilename = 'C:/Users/Christopher Plumberg/Desktop/Research/UIUC/initial_Duke.pdf'
    #print('Saving to', outfilename)
    #fig.savefig(outfilename, bbox_inches='tight')
    #plt.close(fig)
