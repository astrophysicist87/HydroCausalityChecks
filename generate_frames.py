import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from scipy import interpolate
import sys

hbarc = 0.19733     # GeV*fm

# fix command-line arguments
#path = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/"
scale = float(sys.argv[1])
minFrameNumber = int(sys.argv[2])
maxFrameNumber = int(sys.argv[3])
inpath = sys.argv[4]
outpath = sys.argv[5]

tau = 0.6   #initial tau (fm/c)
dx = 0.1
dy = 0.1
scalex = scale
scaley = scale
nxbins = int(np.round(1.0+2.0*scalex/dx))
nybins = int(np.round(1.0+2.0*scaley/dx))

energyCutOff = True
eDec = 0.3/hbarc  # impose cut off in fm^{-4}

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
    global tau
    frameData = np.loadtxt(inpath + '/frame%(frame)03d.dat' % {'frame': frameNumber})
    if frameData.size != 0:
        tau = frameData[0,2]
        frameData = np.unique(frameData, axis=0)
        if energyCutOff:
            frameData = frameData[np.where(frameData[:,6] >= eDec)]
            
    if frameData.size == 0:
        frameData = np.array([[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]])
        
    dataToPlot = frameData[:,[3,4]]     # swap x and y to get correct orientation

    fig, ax = plt.subplots( nrows=1, ncols=1 )
    
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
    
    H = H.T
    ax.imshow(H.astype(int), interpolation='nearest', origin='low', \
                  extent=[-scalex-0.5*dx,scalex+0.5*dx,-scaley-0.5*dy,scaley+0.5*dy], \
                  cmap=ListedColormap(['black','red','purple','blue']),
                  vmin=0, vmax=3)
                  
    plt.text(0.075, 0.925, r'$\tau = %(t)5.2f$ fm$/c$'%{'t': tau}, \
            {'color': 'white', 'fontsize': 12}, transform=ax.transAxes,
            horizontalalignment='left', verticalalignment='top')
            
    ax.set_xlabel(r'$x$ (fm)', fontsize=16)
    ax.set_ylabel(r'$y$ (fm)', fontsize=16)
    
    #plt.show()
    outfilename = outpath + '/slide%(frame)03d.png' % {'frame': frameNumber}
    print 'Saving to', outfilename
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)

#===============================================================================
#def identify_violations(piViolations, BulkPiViolations):
#    # convert pi to make it easier to process
#    piViolation[:,1] = int(np.round(1000.0*piViolation[:,1]))
    
#===============================================================================
def get_value(point, x, y, z):
    return z[ np.where( np.isclose(x,point[0]) & np.isclose(y,point[1]) ) ]

#===============================================================================
def generate_frame_wRegulation(frameNumber):
    # load data to plot
    global tau
    #energyDensity = lambda x, y : 0.0
    frameData = np.loadtxt(inpath + '/frame%(frame)03d.dat' % {'frame': frameNumber})
    frameDataCopy = np.copy(frameData[:,[3,4,6]])
    if frameData.size != 0:
        tau = frameData[0,2]
        frameData = np.unique(frameData, axis=0)
        #energyDensity = interpolate.interp2d(frameData[:,3], frameData[:,4], frameData[:,6], kind='linear')
        if energyCutOff:
            frameData = frameData[np.where(frameData[:,6] >= eDec)]
            
    if frameData.size == 0:
        frameData = np.array([[0,0,0,-1000.0,-1000.0,0,0,0],\
                              [0,0,0,-1000.0,1000.0,0,0,0],\
                              [0,0,0,1000.0,-1000.0,0,0,0],\
                              [0,0,0,1000.0,1000.0,0,0,0]])
        
    dataToPlot = frameData[:,[3,4]]     # swap x and y to get correct orientation

    fig, axs = plt.subplots( nrows=1, ncols=2, figsize=(10,5) )
    
    # histogram with each entry weighted by causality conditions
    vals = np.array([colorFunction(entry) for entry in frameData])
    H, xedges, yedges = np.histogram2d(dataToPlot[:,0], dataToPlot[:,1], \
                        bins=(nxbins, nybins), weights=vals, \
                        range=[[-scalex-0.5*dx,scalex+0.5*dx],
                               [-scaley-0.5*dy,scaley+0.5*dy]])
                
    H = H.T
    axs[0].imshow(H.astype(int), interpolation='nearest', origin='low', \
                  extent=[-scalex-0.5*dx,scalex+0.5*dx,-scaley-0.5*dy,scaley+0.5*dy], \
                  cmap=ListedColormap(['black','red','purple','blue']),
                  vmin=0, vmax=3)
    
    # load piViolation and BulkPiViolation files to track where regulator is needed
    # (assumed to be one directory level up)
    piViolations = np.loadtxt(inpath + '/../piViolation.dat')
    BulkPiViolations = np.loadtxt(inpath + '/../BulkpiViolation.dat')
    piViolations = piViolations[np.where( np.isclose(piViolations[:,0], tau) \
                                & (piViolations[:,1]>0) \
                                & (piViolations[:,1]>1) )] \
                   if piViolations.size > 0 \
                   else np.array([[1000.0,1000.0]])
    BulkPiViolations = BulkPiViolations[np.where( np.isclose(BulkPiViolations[:,0], tau) )] \
                   if BulkPiViolations.size > 0 \
                   else np.array([[1000.0,1000.0]])
    # swap x and y for consistency with above
    dataToPlot = np.unique( np.vstack( (piViolations[:,[-2,-1]], BulkPiViolations[:,[-2,-1]]) ) )
    #eAtCells = np.array([energyDensity( point[0], point[1] ) for point in dataToPlot ])
    eAtCells = np.array([get_value(point, frameDataCopy[:,3], frameDataCopy[:,4], frameDataCopy[:,6])\
                         for point in dataToPlot ])
    dataToPlot = dataToPlot[ np.where( eAtCells >= eDec ) ]

    # to avoid throwing exceptions...
    if dataToPlot.size==0:
        dataToPlot = np.array([[-1000.0,-1000.0],[-1000.0,1000.0],\
                               [1000.0,-1000.0], [1000.0,1000.0]])

    H, xedges, yedges = np.histogram2d(dataToPlot[:,0], dataToPlot[:,1], \
                                    bins=(nxbins, nybins), \
                                    range=[[-scalex-0.5*dx,scalex+0.5*dx],
                                           [-scaley-0.5*dy,scaley+0.5*dy]])
        
    H = H.T
    axs[1].imshow(H.astype(int), interpolation='nearest', origin='low', \
                  extent=[-scalex-0.5*dx,scalex+0.5*dx,-scaley-0.5*dy,scaley+0.5*dy], \
                  cmap=ListedColormap(['black','white']), vmin=0, vmax=1)
                  
    plt.text(0.075, 0.925, r'$\tau = %(t)5.2f$ fm$/c$'%{'t': tau}, \
            {'color': 'white', 'fontsize': 12}, transform=axs[0].transAxes,
            horizontalalignment='left', verticalalignment='top')
            
    for ax in axs.ravel():
        ax.set_xlabel(r'$x$ (fm)', fontsize=16)
        ax.set_ylabel(r'$y$ (fm)', fontsize=16)
    
    #plt.show()
    outfilename = outpath + '/slide_wReg%(frame)03d.png' % {'frame': frameNumber}
    print 'Saving to', outfilename
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)

#===============================================================================
if __name__ == "__main__":
    # generate frames one by one
    for frameNumber in range(minFrameNumber, maxFrameNumber):
        print 'Generating frame =', frameNumber
        generate_frame(frameNumber)
        generate_frame_wRegulation(frameNumber)
