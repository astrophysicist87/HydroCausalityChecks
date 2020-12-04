import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

path = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/"

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
    frameData = np.unique(np.loadtxt(path + 'frame'+str(frameNumber)+'.dat'), axis=0)
    
    dataToPlot = frameData[:,[3,4]]
    
    #print dataToPlot.shape

    #mycmap = ListedColormap(['r', 'g', 'b'])
    #norm = BoundaryNorm([0,1,2], cmap.N)
    
    fig, ax = plt.subplots(1,1)
    
    #ax.pcolormesh(dataToPlot[:,0], dataToPlot[:,1], dataToPlot[:,2], cmap=mycmap, vmin=0, vmax=2)
    #ax.hist2d(dataToPlot[:,0], dataToPlot[:,1], bins=(80, 10), color)
    #n, bins, patches = ax.hist2d(dataToPlot[:,0], dataToPlot[:,1])
    # create data
    #x = np.random.normal(size=50000)
    #y = x * 3 + np.random.normal(size=50000)
    
    # Big bins
    vals = np.array([colorFunction(entry) for entry in frameData])
    H, xedges, yedges = np.histogram2d(dataToPlot[:,0], dataToPlot[:,1], bins=(261, 261), \
                        weights=vals, range=[[-13.05,13.05],[-13.05,13.05]])
    
    X, Y = np.meshgrid(xedges, yedges)
    
    #print vals.shape
    #print 'Good:', vals[np.where(vals==3)].shape
    #print 'Iffy:', vals[np.where(vals==2)].shape
    #print 'Bad:', vals[np.where(vals==1)].shape
    
    factor = 1
    #if frameNumber >= 622:
    #    factor = 0
    
    plt.imshow(factor*(H.astype(int)), interpolation='nearest', origin='low', \
                  extent=[-13.05,13.05,-13.05,13.05], \
                  cmap=ListedColormap(['black','red','purple','blue']),
                  vmin=0, vmax=3)
    
    #for cell in H.ravel():
    #    cell.set_facecolor(colorFunction)

    #plt.show()
    outfilename = path + '/slide%(frame)03d.png' % {'frame': frameNumber}
    print 'Saving to', outfilename
    plt.savefig(outfilename, bbox_inches='tight')

#===============================================================================
if __name__ == "__main__":
    # generate frames one by one
    for frameNumber in xrange(622):
        print 'Generating frame =', frameNumber
        generate_frame(frameNumber)
    #for frameNumber in xrange(622,651):
    #    generate_frame(frameNumber)
