import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os, sys

inpath = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/"

maxtaus = {'EKT': 18.4, 'FS': 19.6, 'no': 19.2}

#===============================================================================
def generate_e2_time_dependence( mode, outpath, e2TimeDependence,
                                 cellFractionTauDependence):
    fig, axs = plt.subplots( nrows=1, ncols=1, figsize=(5,5) )
    
    plt.axhline(0.0, color='black')

    axs.plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,1], color='magenta', lw=2,
              label=r'$\epsilon_{2,p}$, ideal $T^{\mu\nu}$' )
    axs.plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,2], color='cyan', lw=2,
              label=r'$\epsilon_{2,p}$, full $T^{\mu\nu}$' )
    axs.plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,3], color='gold', lw=2,
              label=r'$\epsilon_{2,x}$' )
            
    axs.plot( cellFractionTauDependence[:,0]/maxtaus[mode],
              cellFractionTauDependence[:,3], color='blue', lw=2,
              label=r'Causal' )
    axs.plot( cellFractionTauDependence[:,0]/maxtaus[mode],
              cellFractionTauDependence[:,4], color='purple', lw=2,
              label=r'Indeterminate' )

    axs.set_xlabel(r'$\tau/\tau_{\mathrm{max}}$', fontsize=16)
    axs.set_ylabel(r'$\epsilon_2$', fontsize=16)
    axs.legend( loc='best' )

    plt.text(0.075, 0.925, mode + ' Kompost', \
            {'color': 'black', 'fontsize': 12}, transform=axs.transAxes,
            horizontalalignment='left', verticalalignment='top')

    #plt.show()
    outfilename = outpath + '/e2_integ_vs_tau.pdf'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)

#===============================================================================
if __name__ == "__main__":
    for mode in ['EKT', 'FS', 'no']:
        # import to file
        cellFractionTauDependence \
            = np.loadtxt( inpath + 'resultsFiles/results_PbPb_' + mode
                          + 'Kompost/slides/cell_fractions_tau_dependence.dat' )
        e2TauDependence \
            = np.loadtxt( inpath + 'resultsFiles/results_PbPb_' + mode
                          + 'Kompost/momentum_anisotropy_eta_-0.5_0.5.dat',
                          skiprows=1, usecols=(0,1,3,4))
        
        cellFractionTauDependence = cellFractionTauDependence[np.where( e2TauDependence[:,0] <= maxtaus[mode] )]
        e2TauDependence = e2TauDependence[np.where( e2TauDependence[:,0] <= maxtaus[mode] )]
        
        outpath = inpath + 'resultsFiles/results_PbPb_' + mode + 'Kompost'
        generate_e2_time_dependence( mode, outpath, e2TauDependence,
                                     cellFractionTauDependence)


