import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os, sys

inpath = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/"

#===============================================================================
def generate_e2_time_dependence( mode, outpath, e2TimeDependence ):
    fig, axs = plt.subplots( nrows=1, ncols=3, figsize=(12,3), sharey=True )
    plt.subplots_adjust( wspace=0.0 )

    axs[0].plot( e2TimeDependence[:,0], e2TimeDependence[:,1], color='black', lw=2 )
    axs[0].plot( e2TimeDependence[:,0], e2TimeDependence[:,2], color='blue', lw=2 )
    #axs[0].plot( e2TimeDependence[:,0], e2TimeDependence[:,3], color='red', lw=2 )
    axs[0].plot( e2TimeDependence[:,0], e2TimeDependence[:,4], color='purple', lw=2 )
            
    axs[0].set_xlabel(r'$\tau$ (fm/$c$)', fontsize=16)
    #axs[0].set_ylabel(r'$\epsilon_{2,x}$', fontsize=16)
    axs[0].set_title(r'$\epsilon_{2,x}$', fontsize=16)
    #axs[0].legend( loc='best' )

    plt.text(0.075, 0.925, mode + ' Kompost', \
            {'color': 'black', 'fontsize': 12}, transform=axs[0].transAxes,
            horizontalalignment='left', verticalalignment='top')

    axs[1].plot( e2TimeDependence[:,0], e2TimeDependence[:,5], color='black', lw=2 )
    axs[1].plot( e2TimeDependence[:,0], e2TimeDependence[:,6], color='blue', lw=2 )
    #axs[1].plot( e2TimeDependence[:,0], e2TimeDependence[:,7], color='red', lw=2 )
    axs[1].plot( e2TimeDependence[:,0], e2TimeDependence[:,8], color='purple', lw=2 )
            
    axs[1].set_xlabel(r'$\tau$ (fm/$c$)', fontsize=16)
    #axs[1].set_ylabel(r'$\epsilon_{2,p}$ (ideal $T^{\mu\nu}$)', fontsize=16)
    axs[1].set_title(r'$\epsilon_{2,p}$ (ideal $T^{\mu\nu}$)', fontsize=16)
    #axs[1].legend( loc='best' )

    axs[2].plot( e2TimeDependence[:,0], e2TimeDependence[:,9], color='black', lw=2, label='All cells' )
    axs[2].plot( e2TimeDependence[:,0], e2TimeDependence[:,10], color='blue', lw=2, label='Causal' )
    #axs[2].plot( e2TimeDependence[:,0], e2TimeDependence[:,11], color='red', lw=2, label='Indeterm. (I)' )
    axs[2].plot( e2TimeDependence[:,0], e2TimeDependence[:,12], color='purple', lw=2,
                 label='Causal +\nIndeterminate' )
            
    axs[2].set_xlabel(r'$\tau$ (fm/$c$)', fontsize=16)
    #axs[2].set_ylabel(r'$\epsilon_{2,p}$ (full $T^{\mu\nu}$)', fontsize=16)
    axs[2].set_title(r'$\epsilon_{2,p}$ (full $T^{\mu\nu}$)', fontsize=16)
    axs[2].legend( loc='best' )

    plt.show()
    #outfilename = outpath + '/e2_vs_tau_comp1.pdf'
    #print('Saving to', outfilename)
    #fig.savefig(outfilename, bbox_inches='tight')
    #plt.close(fig)

#===============================================================================
if __name__ == "__main__":
    for mode in ['EKT']:
        # import to file
        e2TimeDependence = np.loadtxt( inpath + 'resultsFiles/results_PbPb_' + mode
                                       + 'Kompost/ecc_frames' + '/e2_ALL_vs_tau.dat' )
        
        outpath = inpath + 'resultsFiles/results_PbPb_' + mode + 'Kompost/ecc_frames'
        generate_e2_time_dependence( mode, outpath, e2TimeDependence )

