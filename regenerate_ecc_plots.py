import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os, sys

inpath = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/"
maxtaus = {'EKT': 18.4, 'FS': 19.6, 'no': 19.2}

#===============================================================================
def generate_e2_time_dependence( mode, outpath, e2TimeDependence ):
    fig, axs = plt.subplots( nrows=1, ncols=2, figsize=(8,4), sharey=True )
    plt.subplots_adjust( wspace=0.0 )

    axs[0].axhline(0.0, color='black')
    axs[0].plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,1], color='black', lw=2 )
    axs[0].plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,2], color='blue', lw=2 )
    #axs[0].plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,3], color='red', lw=2 )
    axs[0].plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,4], color='purple', lw=2 )
            
    axs[0].set_xlabel(r'$\tau/\tau_{\mathrm{max}}$', fontsize=16)
    #axs[0].set_ylabel(r'$\epsilon_{2,x}$', fontsize=16)
    axs[0].set_title(r'$\epsilon_{2,x}$', fontsize=16)
    #axs[0].legend( loc='best' )

    plt.text(0.5, 0.925, mode + ' Kompost', \
            {'color': 'black', 'fontsize': 12}, transform=axs[0].transAxes,
            horizontalalignment='left', verticalalignment='top')

    axs[1].axhline(0.0, color='black')
    axs[1].plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,9], color='black', lw=2, label='All cells' )
    axs[1].plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,10], color='blue', lw=2, label='Causal' )
    #axs[1].plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,11], color='red', lw=2, label='Indeterm. (I)' )
    axs[1].plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,12], color='purple', lw=2,
                 label='Causal +\nIndeterminate' )
            
    axs[1].set_xlabel(r'$\tau/\tau_{\mathrm{max}}$', fontsize=16)
    #axs[1].set_ylabel(r'$\epsilon_{2,p}$ (full $T^{\mu\nu}$)', fontsize=16)
    axs[1].set_title(r'$\epsilon_{2,p}$ (full $T^{\mu\nu}$)', fontsize=16)
    axs[1].legend( loc='best' )

    plt.show()
    #outfilename = outpath + '/e2_vs_tau_comp.pdf'
    #print('Saving to', outfilename)
    #fig.savefig(outfilename, bbox_inches='tight')
    #plt.close(fig)
    



#===============================================================================
def generate_e2x_time_dependence( outpath, e2TimeDependence ):
    fig, axs = plt.subplots( nrows=1, ncols=3, figsize=(15,4), sharey=True )
    plt.subplots_adjust( wspace=0.0 )

    colors=['blue','red','green']
    for loop, mode in enumerate(['EKT','FS','no']):
        # import to file
        e2TimeDependence = np.loadtxt( inpath + 'resultsFiles/results_PbPb_' + mode
                                       + 'Kompost/ecc_frames' + '/e2_ALL_vs_tau.dat' )
        
        axs[loop].axhline(0.0, color='black')
        axs[loop].plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,1], color=colors[loop], lw=2,
                  ls='dashed', label=(mode + ' Kompost: all cells'))
        axs[loop].plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,2], color=colors[loop], lw=2,
                  label=(mode + ' Kompost: causal only'))
                
        axs[loop].set_xlabel(r'$\tau/\tau_{\mathrm{max}}$', fontsize=16)
        axs[loop].set_title(r'$\epsilon_{2,x}$', fontsize=16)

        axs[loop].legend( loc='best' )
        #plt.text(0.5, 0.925, mode + ' Kompost', \
        #        {'color': 'black', 'fontsize': 12}, transform=axs[0].transAxes,
        #        horizontalalignment='left', verticalalignment='top')

    #plt.show()
    outfilename = outpath + '/e2x_vs_tau_comp.pdf'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)

#===============================================================================
if __name__ == "__main__":
    for mode in ['no']:
        # import to file
        e2TimeDependence = np.loadtxt( inpath + 'resultsFiles/results_PbPb_' + mode
                                       + 'Kompost/ecc_frames' + '/e2_ALL_vs_tau.dat' )
        
        outpath = inpath + 'resultsFiles/results_PbPb_' + mode + 'Kompost/ecc_frames'
        generate_e2_time_dependence( mode, outpath, e2TimeDependence )

    outpath = inpath + 'resultsFiles'
    #generate_e2x_time_dependence( outpath, e2TimeDependence )

