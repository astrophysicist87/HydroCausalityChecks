import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
#from scipy import interpolate
import os, sys

hbarc = 0.19733     # GeV*fm

# fix command-line arguments
minFrameNumber = int(sys.argv[1])
maxFrameNumber = int(sys.argv[2])
inpath = sys.argv[3]
outpath = inpath

tau = 0.6   #initial tau (fm/c), overwritten by value in file

energyCutOff = True
#eDec = 0.3/hbarc  # impose cut off in fm^{-4}
eDec = float(sys.argv[4])/hbarc

colorsToUse = ['black','red','purple','blue','green','orange']

#===============================================================================
def colorFunction(entry):
    if entry[7]==0:           # if basic hydro assumptions failed
        return 5
    elif entry[8]==0:         # else if diagonalization of pimunu failed
        return 4
    elif entry[1]==11111111:   # else if sufficient conditions are satisfied
        return 3
    elif entry[0]==111111:     # else if necessary conditions are satisfied
        return 2
    else:                      # else if necessary conditions are violated
        return 1

#===============================================================================
def compute_eccentricity( data ):
    return np.sqrt( np.sum(data[:,0])**2 + np.sum(data[:,1])**2 ) / np.sum(data[:,2])

#===============================================================================
def generate_eccentricity(frameNumber):
    # load data to plot
    global tau
    frameData = np.loadtxt(inpath + '/ecc_frame%(frame)04d.dat' % {'frame': frameNumber})
    if frameData.size != 0:
        tau = frameData[0,2]
        frameData = np.unique(frameData, axis=0)
        if energyCutOff:
            frameData = frameData[np.where(frameData[:,6] >= eDec)]
            
    if frameData.size == 0:
        frameData = np.zeros([2,21])

    vals = np.array([colorFunction(entry) for entry in frameData])

    e2Spatial = frameData[:,[12,13,14]]
    e2pIdeal  = frameData[:,[15,16,17]]
    e2Full    = frameData[:,[18,19,20]]
    
    causalCells = np.where( vals==3 )
    indeterminateCells = np.where( (vals==2) | (vals==4) | (vals==5) )
    causalOrIndeterminateCells = np.where( vals > 1 )
    acausalCells = np.where( vals==1 )
    
    return np.array([tau,\
                     compute_eccentricity( e2Spatial ),
                     compute_eccentricity( e2Spatial[causalCells] ),
                     compute_eccentricity( e2Spatial[indeterminateCells] ),
                     compute_eccentricity( e2Spatial[causalOrIndeterminateCells] ),
                     compute_eccentricity( e2pIdeal ),
                     compute_eccentricity( e2pIdeal[causalCells] ),
                     compute_eccentricity( e2pIdeal[indeterminateCells] ),
                     compute_eccentricity( e2pIdeal[causalOrIndeterminateCells] ),
                     compute_eccentricity( e2Full ),
                     compute_eccentricity( e2Full[causalCells] ),
                     compute_eccentricity( e2Full[indeterminateCells] ),
                     compute_eccentricity( e2Full[causalOrIndeterminateCells] )
                     ])
    
#===============================================================================
def generate_e2_time_dependence( e2TimeDependence ):
    fig, axs = plt.subplots( nrows=1, ncols=3, figsize=(12,3) )

    axs[0].plot( e2TimeDependence[:,0], e2TimeDependence[:,1], color='black', lw=2 )
    axs[0].plot( e2TimeDependence[:,0], e2TimeDependence[:,2], color='blue', lw=2 )
    axs[0].plot( e2TimeDependence[:,0], e2TimeDependence[:,3], color='red', lw=2 )
    axs[0].plot( e2TimeDependence[:,0], e2TimeDependence[:,4], color='purple', lw=2 )
            
    axs[0].set_xlabel(r'$\tau$ (fm/$c$)', fontsize=16)
    axs[0].set_ylabel(r'$\epsilon_{2,x}$', fontsize=16)
    axs[0].legend( loc='best' )

    axs[1].plot( e2TimeDependence[:,0], e2TimeDependence[:,1], color='black', lw=2 )
    axs[1].plot( e2TimeDependence[:,0], e2TimeDependence[:,2], color='blue', lw=2 )
    axs[1].plot( e2TimeDependence[:,0], e2TimeDependence[:,3], color='red', lw=2 )
    axs[1].plot( e2TimeDependence[:,0], e2TimeDependence[:,4], color='purple', lw=2 )
            
    axs[1].set_xlabel(r'$\tau$ (fm/$c$)', fontsize=16)
    axs[1].set_ylabel(r'$\epsilon_{2,p}$ (ideal $T^{\mu\nu}$)', fontsize=16)
    axs[1].legend( loc='best' )

    axs[2].plot( e2TimeDependence[:,0], e2TimeDependence[:,1], color='black', lw=2 )
    axs[2].plot( e2TimeDependence[:,0], e2TimeDependence[:,2], color='blue', lw=2 )
    axs[2].plot( e2TimeDependence[:,0], e2TimeDependence[:,3], color='red', lw=2 )
    axs[2].plot( e2TimeDependence[:,0], e2TimeDependence[:,4], color='purple', lw=2 )
            
    axs[2].set_xlabel(r'$\tau$ (fm/$c$)', fontsize=16)
    axs[2].set_ylabel(r'$\epsilon_{2,p}$ (full $T^{\mu\nu}$)', fontsize=16)
    axs[2].legend( loc='best' )

    #plt.show()
    outfilename = outpath + '/e2_ALL_vs_tau.png'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)

#===============================================================================
if __name__ == "__main__":
    # generate frames one by one
    e2TimeDependence = None
    for loop, frameNumber in enumerate(range(minFrameNumber, maxFrameNumber)):
        print('Generating frame =', frameNumber, ';', \
               maxFrameNumber - frameNumber, 'frames remaining')
        e2s = generate_frame(frameNumber)
        if loop==0:
            e2TimeDependence = e2s
        else:
            e2TimeDependence = np.c_[ e2TimeDependence, e2s ]

    e2TimeDependence = e2TimeDependence.T
    
    # export to file in case plotting fails
    np.savetxt( outpath + '/e2_ALL_vs_tau.dat', e2TimeDependence )
    
    generate_e2_time_dependence( e2TimeDependence )
