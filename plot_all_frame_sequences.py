import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

inpath = 'C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/all_frames_v8/'
outpath = inpath

energyCutOff = True
hbarc = 0.19733     # GeV*fm
numberOfFrames = 5

colorsToUse = ['black','red','purple','blue','green','orange']

simulationTypes = ['OSU_hydro', 'MUSIC_noKompost', 'MUSIC_FSKompost', 'MUSIC_EKTKompost']
hydroStrings = dict(zip(simulationTypes,
                [r'T$_{\rm R}$ENTo + free-streaming + iEBE-VISHNU',
                r'IP-Glasma + MUSIC', r'IP-Glasma + free-streaming K${\o}$MP${\o}$ST + MUSIC',
                r'IP-Glasma + effective kinetic theory K${\o}$MP${\o}$ST + MUSIC']))
scales = dict(zip(simulationTypes, [16.7778, 20.48, 20.48, 20.48]))
dxys = dict(zip(simulationTypes, [0.1434, 0.08, 0.08, 0.08]))
eDecs = dict(zip(simulationTypes, [0.265, 0.18, 0.18, 0.18]))

#res = dict(zip(test_keys, test_values))

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

def generate_frames(axs, simulationType):
    # set simulation parameters
    tau = 0.6   #initial tau (fm/c), overwritten by value in file
    scale = scales[simulationType]
    eDec = eDecs[simulationType]/hbarc  # impose cut off in fm^{-4}
    dxy = dxys[simulationType]
    hydroString = hydroStrings[simulationType]
    
    dx = dxy
    dy = dxy
    scalex = scale
    scaley = scale
    nxbins = int(np.round(1.0+2.0*scalex/dx))
    nybins = int(np.round(1.0+2.0*scaley/dx))
    
    for i in range(numberOfFrames):
        # load data to plot
        frameData = np.loadtxt(inpath + '/' + simulationType + '_frame'+str(i)+'.dat')
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
        
        H = H[ np.where( np.abs(xedges)<=16.52 ) ]
        H = H.T
        H = H[ np.where( np.abs(yedges)<=16.52 ) ]
        axs[i].imshow(H.astype(int), interpolation='nearest', origin='lower', \
                      extent=[-16.52,16.52,-16.52,16.52], \
                      cmap=ListedColormap(colorsToUse), vmin=0, vmax=(len(colorsToUse)-1))
                      
        plt.text(0.075, 0.925, r'$\tau = %(t)5.2f$ fm$/c$'%{'t': tau}, \
                {'color': 'white', 'fontsize': 12}, transform=axs[i].transAxes,
                horizontalalignment='left', verticalalignment='top')
                
    plt.text(0.075, 0.15, hydroString, \
        {'color': 'white', 'fontsize': 12}, transform=axs[0].transAxes,
        horizontalalignment='left', verticalalignment='top')
        

#===============================================================================
if __name__ == "__main__":
    fig, axs = plt.subplots( nrows=len(simulationTypes), ncols=numberOfFrames, figsize=(15,12), sharex=True, sharey=True )
    for j, simulationType in enumerate(simulationTypes):
        generate_frames(axs[j], simulationType)
        axs[j,0].set_ylabel(r'$y$ (fm)', fontsize=16)
        axs[j,0].set_yticks([-10,0,10])
        if j+1 == len(simulationTypes):
            for ax in axs[j]:
                ax.set_xlabel(r'$x$ (fm)', fontsize=16)
                ax.set_xticks([-10,0,10])

    plt.subplots_adjust( hspace=-0.01, wspace=-0.01 )
    #plt.show()
    outfilename = outpath + 'all_frame_sequences.png'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight', dpi=300)
    plt.close(fig)

