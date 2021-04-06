import numpy as np
import matplotlib.pyplot as plt
import os, sys

path='C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/KRevo_frame0000.dat'
#inpath=sys.argv[1]
#outpath=sys.argv[2]
#nFiles=int(sys.argv[3])

KRdata = np.loadtxt(path)

fig, ax = plt.subplots( nrows=1, ncols=1, figsize=(8,8) )
im = ax.imshow(KRdata[:,-2].reshape([512,512]), interpolation='nearest', origin='lower', \
                      extent=[-20.48,20.48,-20.48,20.48], \
                      cmap=plt.get_cmap('gnuplot2'), vmin=0.0, vmax=5.0)

cbar = plt.colorbar(im, fraction=0.046, pad=0.04, label=r'$R_\pi$')

plt.show()


'''for i in range(nFiles):
    path = inpath + '/KRevo_frame{:04}.dat'.format(i)
    KRdata = np.loadtxt(path)

    fig, ax = plt.subplots( nrows=1, ncols=1, figsize=(6,6) )
    im = ax.imshow(KRdata[:,-2].reshape([512,512]), interpolation='nearest', origin='lower', \
                          extent=[-20.48,20.48,-20.48,20.48], \
                          cmap=plt.get_cmap('gnuplot2'), vmin=0.0, vmax=1.0)

    cbar = plt.colorbar(im, label=r'e [GeV/fm$^3$]')

    plt.show()
    outfilename = outpath + '/KRevo_slide{:04}.png'.format(i)
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight', dpi=300)
    plt.close(fig)'''

