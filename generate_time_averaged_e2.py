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
def compute_eccentricity_sq( data ):
    return ( (np.sum(data[:,0]))**2 + (np.sum(data[:,1]))**2) / (np.sum(data[:,2]))**2

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
    
    return np.sqrt( np.array([tau**2,
                              compute_eccentricity_sq( e2Spatial ), compute_eccentricity_sq( e2Spatial[causalCells] ),
                              compute_eccentricity_sq( e2pFull ), compute_eccentricity_sq( e2pFull[causalCells] ) ]))
    




#===============================================================================
if __name__ == "__main__":
    # generate frames one by one
    e2TimeDependence = np.zeros(0)
    for loop, frameNumber in enumerate(range(minFrameNumber, maxFrameNumber)):
        print('Generating frame =', frameNumber, ';', \
               maxFrameNumber - frameNumber, 'frames remaining')
        e2s = generate_eccentricity(frameNumber)
        print(e2s)
        if loop==0:
            e2TimeDependence = e2s
        else:
            e2TimeDependence = np.c_[ e2TimeDependence, e2s ]

    e2TimeDependence = e2TimeDependence.T
    
    # export to file in case plotting fails
    np.savetxt( outpath + '/e2_ALL_vs_tau.dat', e2TimeDependence )
    
