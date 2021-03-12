import numpy as np
import matplotlib.pyplot as plt
#import glob

path = 'C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/resultsFiles/'
#filenames = [path + 'edFiles/RESULTS_OPTIMAL_FINAL_TAUFS0_TAU0_01_RS1/ed.dat']
filenames = [path + 'edFiles/RESULTS_OPTIMAL_FINAL_TAUFS010_RS1/ed.dat']

#for filename in glob.glob(path + 'edFiles/RESULTS_OPTIMAL_FINAL*/ed.dat'):
for filename in filenames:
    data = np.fromfile(filename)
    Ng = int(np.sqrt(len(data)))
    nx = ny = int((Ng-1)/2)
    dxy = 0.1434
    dx = dy = dxy

    data = data.reshape([Ng, Ng])
    
    print(np.amax(data))

    fig, ax = plt.subplots( nrows=1, ncols=1 )

    im = ax.imshow(data, interpolation='nearest', \
                  origin='lower', extent=[-nx*dx, nx*dx, -ny*dy, ny*dy],
                  cmap=plt.get_cmap('gnuplot'))
            
    ax.set_xlabel(r'$x$ (fm)', fontsize=16)
    ax.set_ylabel(r'$y$ (fm)', fontsize=16)

    plt.colorbar(im, label=r'e [GeV/fm$^3$]')

    plt.show()
    #outfilename = path + 'initial_Duke.pdf'
    #print('Saving to', outfilename)
    #fig.savefig(outfilename, bbox_inches='tight')
    #plt.close(fig)