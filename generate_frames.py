import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import sys

# fix command-line arguments
#path = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/"
scale = float(sys.argv[1])
minFrameNumber = int(sys.argv[2])
maxFrameNumber = int(sys.argv[3])
inpath = sys.argv[4]
outpath = sys.argv[5]

dx = 0.1
dy = 0.1
scalex = scale
scaley = scale
nxbins = int(np.round(1.0+2.0*scalex/dx))
nybins = int(np.round(1.0+2.0*scaley/dx))

energyCutOff = True
eDec = 0.3  # GeV/fm^3

#===============================================================================
def colorFunction(entry):
    if entry[1]==11111111:
        return 3
    elif entry[0]==111111:
        return 2
    else:
        return 1

#===============================================================================
def generate_frame(frameNumber):
    # load data to plot
    frameData = np.loadtxt(inpath + 'frame'+str(frameNumber)+'.dat')
    if frameData.size == 0:
        frameData = np.array([[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]])
    else:
        frameData = np.unique(frameData, axis=0)
        if energyCutOff:
            frameData = frameData[np.where(frameData[:,6] >= eDec)]
    dataToPlot = frameData[:,[3,4]]

    fig, ax = plt.subplots(1,1)
    
    # histogram with each entry weighted by causality conditions
    vals = np.array([colorFunction(entry) for entry in frameData])
    H, xedges, yedges = np.histogram2d(dataToPlot[:,0], dataToPlot[:,1], \
                        bins=(nxbins, nybins), weights=vals, \
                        range=[[-scalex-0.5*dx,scalex+0.5*dx],
                               [-scaley-0.5*dy,scaley+0.5*dy]])
        
    #print 'Total:', vals.shape
    #print 'Good:', vals[np.where(vals==3)].shape
    #print 'Iffy:', vals[np.where(vals==2)].shape
    #print 'Bad:', vals[np.where(vals==1)].shape
        
    plt.imshow(H.astype(int), interpolation='nearest', origin='low', \
                  extent=[-scalex-0.5*dx,scalex+0.5*dx,-scaley-0.5*dy,scaley+0.5*dy], \
                  cmap=ListedColormap(['black','red','purple','blue']),
                  vmin=0, vmax=3)
    
    #plt.show()
    outfilename = outpath + '/slide%(frame)03d.png' % {'frame': frameNumber}
    print 'Saving to', outfilename
    plt.savefig(outfilename, bbox_inches='tight')

#===============================================================================
if __name__ == "__main__":
    # generate frames one by one
    for frameNumber in xrange(minFrameNumber, maxFrameNumber+1):
        print 'Generating frame =', frameNumber
        generate_frame(frameNumber)
