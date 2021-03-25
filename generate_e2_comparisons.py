import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os, sys

inpath = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/all_results_v4/"

#maxtaus = {'EKT': 18.4, 'FS': 19.6, 'no': 19.2, 'Duke': 12.2}
maxtaus = {'EKT': 14.2, 'FS': 14.8, 'no': 21.4, 'Duke': 12.2}
paths = {'EKT': 'MUSIC_v4_PbPb_EKTKompost_results',
         'FS': 'MUSIC_v4_PbPb_FSKompost_results',
         'no': 'MUSIC_v4_PbPb_noKompost_results',
         'Duke': 'OSUhydro_RESULTS_OPTIMAL_FINAL_TAUFS116_RS1'}
#paths = {'EKT': 'MUSIC_results_newE2P_PbPb_EKTKompost',
#         'FS': 'MUSIC_results_newE2P_PbPb_FSKompost',
#         'no': 'MUSIC_results_newE2P_PbPb_noKompost',
#         'Duke': 'OSUhydro_RESULTS_OPTIMAL_FINAL_TAUFS116_RS1'}
e2Filenames = {'EKT': 'momentum_anisotropy_eta_-0.5_0.5.dat',
               'FS': 'momentum_anisotropy_eta_-0.5_0.5.dat',
               'no': 'momentum_anisotropy_eta_-0.5_0.5.dat',
               'Duke': 'anisotropies.dat'}
#linestyles = {'EKT': '--', 'FS': '-.', 'no': ':', 'Duke': '-'}
linestyles = {'EKT': '-', 'FS': '--', 'no': '-.', 'Duke': ':'}
tau0 = {'EKT': 0.8, 'FS': 0.8, 'no': 0.4, 'Duke': 1.16}

#(0,6,7,5)
#(0,2,3,5)
colsToUse = {'EKT': (0,1,3,4),
             'FS': (0,1,3,4),
             'no': (0,1,3,4),
             'Duke': (0,6,7,5)}


#===============================================================================
def get_halfCausal_tau(pathToRead):
    cellFractionData = np.loadtxt(pathToRead, usecols=(0,3))
    # function to return difference between causal cell fraction and 50%
    from scipy.optimize import fsolve
    f = lambda x : np.interp(x, cellFractionData[:,0], cellFractionData[:,1])-0.5
    # make a reasonable guess for when causal cell fraction is 50%
    return fsolve( f, 3.0 )


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
    plt.rcParams["mathtext.fontset"] = "cm"
    fig, axs = plt.subplots( nrows=1, ncols=2, figsize=(9,4), sharey=False )
    plt.subplots_adjust( wspace=0 )
    
    axs[0].axhline(0.0, color='black')
    axs[1].axhline(0.0, color='black')
    
    # set halfway times
    #halfCausalTaus = {'EKT': 3.58977, 'FS': 3.56162, 'no': 3.52675, 'Duke': 3.21882}

    for mode in ['EKT', 'FS', 'no', 'Duke']:
        # import file
        e2TimeDependence \
            = np.loadtxt( inpath + paths[mode] + '/' + e2Filenames[mode],
                          skiprows=1, usecols=colsToUse[mode])
        
        e2TimeDependence = e2TimeDependence[ np.where( e2TimeDependence[:,0] <= maxtaus[mode] )]
        
        t0 = tau0[mode]   
        outpath = inpath + paths[mode] + '/'
        axs[0].plot( (e2TimeDependence[:,0]-t0)/(maxtaus[mode]-t0), e2TimeDependence[:,2],
                  color='crimson', lw=2, ls=linestyles[mode] )
        axs[1].plot( (e2TimeDependence[:,0]-t0)/(maxtaus[mode]-t0), e2TimeDependence[:,3],
                  color='steelblue', lw=2, ls=linestyles[mode] )

        #tHalf = halfCausalTaus[mode]
        tHalf = get_halfCausal_tau(outpath + '/cell_fractions_tau_dependence.dat')
        print(mode,":",tHalf," is about when 50% of fluid cells are causal")
        e2pTHalf = np.interp( tHalf, e2TimeDependence[:,0], e2TimeDependence[:,2])
        e2xTHalf = np.interp( tHalf, e2TimeDependence[:,0], e2TimeDependence[:,3])
        axs[0].plot( (tHalf-t0)/(maxtaus[mode]-t0), e2pTHalf, 'o', color='black', ms=5 )
        axs[1].plot( (tHalf-t0)/(maxtaus[mode]-t0), e2xTHalf, 'o', color='black', ms=5 )

    axs[1].axhline( -1000.0, color='black', ls='-.', label=r'IP-Glasma + MUSIC' )
    axs[1].axhline( -1000.0, color='black', ls='-', label=r'+ EKT K${\o}$MP${\o}$ST' )
    axs[1].axhline( -1000.0, color='black', ls='--', label=r'+ FS K${\o}$MP${\o}$ST' )
    axs[1].axhline( -1000.0, color='black', ls=':', label=r'Trento + FS + VISHNU' )
    axs[1].plot( np.array([0.5,-1000.0]), 'o', color='black', label=r'50% cells causal' )

    plt.text(0.15, 0.9, r'$\epsilon_{2,p}$', \
            {'color': 'black', 'fontsize': 16}, transform=axs[0].transAxes,
            horizontalalignment='center', verticalalignment='top')
    plt.text(0.15, 0.15, r'$\epsilon_{2,x}$', \
            {'color': 'black', 'fontsize': 16}, transform=axs[1].transAxes,
            horizontalalignment='center', verticalalignment='top')

    axs[0].set_ylim(bottom=-0.0025, top=0.1)
    axs[1].set_ylim([-0.004375,0.175])
    axs[0].set_xlabel(r'$\Delta\tau/\Delta\tau_{\mathrm{max}}$', fontsize=16)
    axs[1].set_xlabel(r'$\Delta\tau/\Delta\tau_{\mathrm{max}}$', fontsize=16)
    #axs[0].set_ylabel(r'$\epsilon_{2,p}$', fontsize=16)
    #axs[1].yaxis.set_label_position("right")
    axs[1].yaxis.tick_right()
    #axs[1].set_ylabel(r'$\epsilon_{2,x}$', fontsize=16)
    #axs[0].legend( loc='best' )
    axs[1].legend( loc='best' )

    #plt.show()
    outfilename = inpath + '/e2_vs_tau_comparison.pdf'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)
    
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


