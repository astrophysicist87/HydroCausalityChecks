import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, sys

hbarc = 0.19733

#inpath='C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/KRevo_ePlusp_frame0000.dat'
inpath=sys.argv[1]
outpath=sys.argv[2]
#nFiles=int(sys.argv[3])
#gridSize = 512 if len(sys.argv) < 4 else int(sys.argv[3])
#gridScale = 20.48 if len(sys.argv) < 5 else int(sys.argv[4])

KRdata = np.loadtxt(inpath)

gridSize = int(np.sqrt(len(KRdata[:,1])))
gridScale = -KRdata[0,1]

tau = KRdata[0,0]

eDec = 0.18
eBelowFO = np.where(KRdata[:,3] < eDec/hbarc)
Rpi = KRdata[:,-2]
RPi = KRdata[:,-1]
Rpi[eBelowFO] = 0.0
RPi[eBelowFO] = 0.0

#===========================================================
# Plot pi
fig, ax = plt.subplots( nrows=1, ncols=1, figsize=(6,6) )
im = ax.imshow(Rpi.reshape([gridSize,gridSize]), interpolation='nearest', origin='lower', \
                      extent=[-gridScale,gridScale,-gridScale,gridScale], \
                      cmap=plt.get_cmap('gnuplot2'), vmin=0.0, vmax=1.0)

cbar = plt.colorbar(im, fraction=0.046, pad=0.04)
cbar.set_label(label=r'$\mathrm{Re}^{-1}_\pi$', size=16, weight='bold')

plt.text(0.075, 0.925, r'$\tau = %(t)5.2f$ fm$/c$'%{'t': tau}, \
        {'color': 'white', 'fontsize': 12}, transform=ax.transAxes,
        horizontalalignment='left', verticalalignment='top')
        
ax.set_xlabel(r'$x$ (fm)', fontsize=16)
ax.set_ylabel(r'$y$ (fm)', fontsize=16)

#plt.show()
outfilename = outpath
print('Saving to', outfilename)
fig.savefig(outfilename, bbox_inches='tight', dpi=300)
plt.close(fig)



#===========================================================
# Reset, plot Pi
fig, ax = plt.subplots( nrows=1, ncols=1, figsize=(6,6) )
im = ax.imshow(RPi.reshape([gridSize,gridSize]), interpolation='nearest', origin='lower', \
                      extent=[-gridScale,gridScale,-gridScale,gridScale], \
                      cmap=plt.get_cmap('gnuplot2'), vmin=0.0, vmax=1.0)

cbar = plt.colorbar(im, fraction=0.046, pad=0.04)
cbar.set_label(label=r'$\mathrm{Re}^{-1}_\Pi$', size=16, weight='bold')

plt.text(0.075, 0.925, r'$\tau = %(t)5.2f$ fm$/c$'%{'t': tau}, \
        {'color': 'white', 'fontsize': 12}, transform=ax.transAxes,
        horizontalalignment='left', verticalalignment='top')
        
ax.set_xlabel(r'$x$ (fm)', fontsize=16)
ax.set_ylabel(r'$y$ (fm)', fontsize=16)

#plt.show()
outfilename = outpath.replace('pi','Pi')
print('Saving to', outfilename)
fig.savefig(outfilename, bbox_inches='tight', dpi=300)
plt.close(fig)

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

