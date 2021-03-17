import numpy as np
import os, sys

hbarc = 0.19733     # GeV*fm

# fix command-line arguments
minFrameNumber = int(sys.argv[1])
maxFrameNumber = int(sys.argv[2])
inpath = sys.argv[3]
outpath = inpath

tau = 0.6   #initial tau (fm/c), overwritten by value in file

colorsToUse = ['black','red','purple','blue','green','orange']

#===============================================================================
def colorFunction(entry):
    if entry[7]==0:            # if basic hydro assumptions failed
        return 5
    elif entry[8]==0:          # else if diagonalization of pimunu failed
        return 4
    elif entry[1]==11111111:   # else if sufficient conditions are satisfied
        return 3
    elif entry[0]==111111:     # else if necessary conditions are satisfied
        return 2
    else:                      # else if necessary conditions are violated
        return 1


#===============================================================================
def generate_eccentricity(frameNumber):
    # load data to plot
    global tau
    frameData = np.loadtxt(inpath + '/ecc_frame%(frame)04d.dat' % {'frame': frameNumber})
    if frameData.size != 0:
        tau = frameData[0,2]
        frameData = np.unique(frameData, axis=0)
            
    if frameData.size == 0:
        frameData = np.zeros([2,21])

    vals = np.array([colorFunction(entry) for entry in frameData])

    e2Spatial = frameData[:,[12,13,14]]
    e2pFull   = frameData[:,[18,19,20]]
    
    causalCells = np.where( vals==3 )
    
    #runninge2Spatial       += np.sum( e2Spatial, axis=0 )
    #runninge2SpatialCausal += np.sum( e2Spatial[causalCells], axis=0 )
    #runninge2pFull         += np.sum( e2pFull, axis=0 )
    #runninge2pFullCausal   += np.sum( e2pFull[causalCells], axis=0 )
    return tau, np.sum( e2Spatial, axis=0 ), np.sum( e2Spatial[causalCells], axis=0 ),\
           np.sum( e2pFull, axis=0 ),   np.sum( e2pFull[causalCells], axis=0 )

#===============================================================================
def compute_eccentricity( data ):
    return np.sqrt( data[0]**2 + data[1]**2 ) / data[2]


#===============================================================================
if __name__ == "__main__":
    # generate frames one by one
    #e2TimeDependence = np.zeros(0)
    runninge2x = np.zeros([3])
    runninge2xC = np.zeros([3])
    runninge2p = np.zeros([3])
    runninge2pC = np.zeros([3])
    for loop, frameNumber in enumerate(range(minFrameNumber, maxFrameNumber)):
        print('Generating frame =', frameNumber, ';', \
               maxFrameNumber - frameNumber, 'frames remaining')
        tau, e2x, e2xC, e2p, e2pC = generate_eccentricity(frameNumber)
        print('Check:', tau,
                compute_eccentricity( e2x ),
                compute_eccentricity( e2xC ),
                compute_eccentricity( e2p ),
                compute_eccentricity( e2pC ) )
        runninge2x += e2x
        runninge2xC += e2xC
        runninge2p += e2p
        runninge2pC += e2pC
        #if loop==0:
        #    e2TimeDependence = e2s
        #else:
        #    e2TimeDependence = np.c_[ e2TimeDependence, e2s ]
        if tau >= float(sys.argv[4]):
            break

    #e2TimeDependence = e2TimeDependence.T
    print( tau, compute_eccentricity( runninge2x ),
                compute_eccentricity( runninge2xC ),
                compute_eccentricity( runninge2p ),
                compute_eccentricity( runninge2pC ) )
    
    # export to file in case plotting fails
    #print('Saving to ' + outpath + '/e2_ALL_vs_tau.dat')
    #np.savetxt( outpath + '/e2_ALL_vs_tau.dat', e2TimeDependence )
    
