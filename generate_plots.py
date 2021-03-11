import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
#from scipy import interpolate
import sys

hbarc = 0.19733     # GeV*fm

# fix command-line arguments
#path = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/"
scale = float(sys.argv[1])
minFrameNumber = int(sys.argv[2])
maxFrameNumber = int(sys.argv[3])
inpath = sys.argv[4]
outpath = sys.argv[5]
'''scale=10
minFrameNumber=0
maxFrameNumber=40
inpath="C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/frames"
outpath="C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/slides"'''


tau = 0.6   #initial tau (fm/c), overwritten by value in file
#dx = 0.1
#dy = 0.1
dxy = float(sys.argv[7])
dx = dxy
dy = dxy
scalex = scale
scaley = scale
nxbins = int(np.round(1.0+2.0*scalex/dx))
nybins = int(np.round(1.0+2.0*scaley/dx))

energyCutOff = True
#eDec = 0.3/hbarc  # impose cut off in fm^{-4}
eDec = float(sys.argv[6])/hbarc

colorsToUse = ['black','red','purple','blue','green','orange']

#===============================================================================
def colorFunction(entry):
    if entry[-2]==0:           # if basic hydro assumptions failed
        return 5
    elif entry[-1]==0:         # else if diagonalization of pimunu failed
        return 4
    elif entry[1]==11111111:   # else if sufficient conditions are satisfied
        return 3
    elif entry[0]==111111:     # else if necessary conditions are satisfied
        return 2
    else:                      # else if necessary conditions are violated
        return 1

#===============================================================================

def generate_frames(frameNumbers):
    global tau
    fig, axs = plt.subplots( nrows=1, ncols=len(frameNumbers), figsize=(15,3) )
    plt.subplots_adjust( hspace=0.0, wspace=0.0 )
    for i, frameNumber in enumerate(frameNumbers):
        # load data to plot
        frameData = np.loadtxt(inpath + '/frame%(frame)04d.dat' % {'frame': frameNumber})
        if frameData.size != 0:
            tau = frameData[0,2]
            frameData = np.unique(frameData, axis=0)
            if energyCutOff:
                frameData = frameData[np.where(frameData[:,6] >= eDec)]
                
        if frameData.size == 0:
            frameData = np.array([[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]])
            
        dataToPlot = frameData[:,[3,4]]     # swap x and y to get correct orientation
        
        # histogram with each entry weighted by causality conditions
        vals = np.array([colorFunction(entry) for entry in frameData])
        H, xedges, yedges = np.histogram2d(dataToPlot[:,0], dataToPlot[:,1], \
                            bins=(nxbins, nybins), weights=vals, \
                            range=[[-scalex-0.5*dx,scalex+0.5*dx],
                                   [-scaley-0.5*dy,scaley+0.5*dy]])
                
        H = H.T
        axs[i].imshow(H.astype(int), interpolation='nearest', origin='low', \
                      extent=[-scalex-0.5*dx,scalex+0.5*dx,-scaley-0.5*dy,scaley+0.5*dy], \
                      cmap=ListedColormap(colorsToUse), vmin=0, vmax=(len(colorsToUse)-1))
                      
        plt.text(0.075, 0.925, r'$\tau = %(t)5.2f$ fm$/c$'%{'t': tau}, \
                {'color': 'white', 'fontsize': 12}, transform=axs[i].transAxes,
                horizontalalignment='left', verticalalignment='top')
                
        axs[i].set_xlabel(r'$x$ (fm)', fontsize=16)
        if i==0:
            axs[i].set_ylabel(r'$y$ (fm)', fontsize=16)
        
    #plt.show()
    outfilename = outpath + '/frame_sequence.png'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)
        

#===============================================================================
if __name__ == "__main__":
    # generate sequence of frames
    frameNumbers = [0, 50, 100, 150, 200]
    generate_frames(frameNumbers)