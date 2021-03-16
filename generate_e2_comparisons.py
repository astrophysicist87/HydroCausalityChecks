import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os, sys

inpath = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/"

maxtaus = {'EKT': 18.4, 'FS': 19.6, 'no': 19.2, 'Duke': 12.2}
paths = {'EKT': 'MUSIC_results_PbPb_EKTKompost',
         'FS': 'MUSIC_results_PbPb_FSKompost',
         'no': 'MUSIC_results_PbPb_noKompost',
         'Duke': 'OSUhydro_RESULTS_OPTIMAL_FINAL_TAUFS116_RS1'}
e2Filenames = {'EKT': 'momentum_anisotropy_eta_-0.5_0.5.dat',
               'FS': 'momentum_anisotropy_eta_-0.5_0.5.dat',
               'no': 'momentum_anisotropy_eta_-0.5_0.5.dat',
               'Duke': 'anisotropies.dat'}
linestyles = {'EKT': '--', 'FS': '-.', 'no': ':', 'Duke': '-'}
tau0 = {'EKT': 0.8, 'FS': 0.8, 'no': 0.4, 'Duke': 1.16}

#(0,6,7,5)
#(0,2,3,5)
colsToUse = {'EKT': (0,1,3,4),
             'FS': (0,1,3,4),
             'no': (0,1,3,4),
             'Duke': (0,6,7,5)}
#===============================================================================
def generate_e2_time_dependence( mode, outpath, e2TimeDependence ):
    fig, axs = plt.subplots( nrows=1, ncols=1, figsize=(5,5) )
    
    plt.axhline(0.0, color='black')

    #axs.plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,1], color='magenta', lw=2,
    #          ls=linestyles[mode], label=r'$\epsilon_{2,p}$, ideal $T^{\mu\nu}$' )
    axs.plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,2], color='cyan', lw=2,
              label=r'$\epsilon_{2,p}$, full $T^{\mu\nu}$' )
    axs.plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,3], color='magenta', lw=2,
              label=r'$\epsilon_{2,x}$' )
            
    axs.set_xlabel(r'$\tau/\tau_{\mathrm{max}}$', fontsize=16)
    axs.set_ylabel(r'$\epsilon_2$', fontsize=16)
    axs.legend( loc='best' )

    plt.show()
    #outfilename = outpath + '/e2_integ_vs_tau.pdf'
    #print('Saving to', outfilename)
    #fig.savefig(outfilename, bbox_inches='tight')
    #plt.close(fig)


#===============================================================================
def generate_ALL_e2_time_dependences():
    fig, axs = plt.subplots( nrows=1, ncols=2, figsize=(9,4) )
    
    axs[0].axhline(0.0, color='black')
    axs[1].axhline(0.0, color='black')

    for mode in ['EKT', 'FS', 'no', 'Duke']:
        # import file
        e2TimeDependence \
            = np.loadtxt( inpath + 'all_results/'+ paths[mode] + '/' + e2Filenames[mode],
                          skiprows=1, usecols=colsToUse[mode])
        
        e2TimeDependence = e2TimeDependence[ np.where( e2TimeDependence[:,0] <= maxtaus[mode] )]
        
        t0 = tau0[mode]
        outpath = inpath + 'all_results/' + paths[mode] + '/'
        #axs.plot( e2TimeDependence[:,0]/maxtaus[mode], e2TimeDependence[:,1], color='magenta', lw=2,
        #          label=r'$\epsilon_{2,p}$, ideal $T^{\mu\nu}$' )
        axs[0].plot( (e2TimeDependence[:,0]-t0)/(maxtaus[mode]-t0), e2TimeDependence[:,2],
                  color='crimson', lw=2, ls=linestyles[mode] )
        axs[1].plot( (e2TimeDependence[:,0]-t0)/(maxtaus[mode]-t0), e2TimeDependence[:,3],
                  color='steelblue', lw=2, ls=linestyles[mode] )

    '''l1 = axs.axhline( -1000.0, lw=3, color='crimson', label=r'$\epsilon_{2,p}$' )
    l2 = axs.axhline( -1000.0, lw=3, color='steelblue', label=r'$\epsilon_{2,x}$' )
    l4 = axs.axhline( -1000.0, lw=3, color='black', ls='-', label='Duke' )
    l5 = axs.axhline( -1000.0, lw=3, color='black', ls='--', label='EKT Kompost' )
    l6 = axs.axhline( -1000.0, lw=3, color='black', ls='-.', label='FS Kompost' )
    l7 = axs.axhline( -1000.0, lw=3, color='black', ls=':', label='no Kompost' )

    lc1 = (l1, l2)
    lc2 = (l4, l5, l6, l7)
    
    #legend1=axs.legend(lc1, ('Causal', 'Indeterminate', 'Acausal'), fontsize=16, loc=(0.47,0.6))
    #axs.legend(lc2, ('EKT Kompost', 'FS Kompost', 'no Kompost', 'Duke'), fontsize=16, loc=(0.5,0.2))
    #plt.gca().add_artist(legend1)

    axs.set_ylim([0.0, 0.2])
    axs.set_xlabel(r'$(\tau-\tau_0)/(\tau_{\mathrm{max}}-\tau_0)$', fontsize=16)
    axs.set_ylabel(r'$\epsilon_2$', fontsize=16)
    axs.legend( loc='best', ncol=2 )'''

    plt.show()
    #outfilename = inpath + 'all_results/e2_vs_tau_comparison.pdf'
    #print('Saving to', outfilename)
    #fig.savefig(outfilename, bbox_inches='tight')
    #plt.close(fig)
    
#===============================================================================
if __name__ == "__main__":
    '''for mode in ['EKT', 'FS', 'no', 'Duke']:
        # import file
        e2TauDependence \
            = np.loadtxt( inpath + 'all_results/'+ paths[mode] + '/' + e2Filenames[mode],
                          skiprows=1, usecols=colsToUse[mode])
        
        e2TauDependence = e2TauDependence[ np.where( e2TauDependence[:,0] <= maxtaus[mode] )]
        
        outpath = inpath + 'all_results/' + paths[mode] + '/'
        generate_e2_time_dependence( mode, outpath, e2TauDependence )'''

    generate_ALL_e2_time_dependences()


