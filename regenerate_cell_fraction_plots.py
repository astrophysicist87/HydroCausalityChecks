import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os, sys

hbarc = 0.19733     # GeV*fm
path = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/all_results_v4/"

maxtaus = {'EKT': 14.2, 'FS': 14.8, 'no': 21.4, 'Duke': 12.2}
colors = ['orange', 'green', 'blue', 'purple', 'red']


#===============================================================================
def generate_fraction_time_dependence( data1, data2, data3, data4, lw ):
    plt.rcParams["mathtext.fontset"] = "cm"
    fig, axs = plt.subplots( nrows=1, ncols=3, figsize=(15,4), sharey=True )
    plt.subplots_adjust( wspace=0 )

    axs[0].plot( (data1[:,0]-0.8)/(maxtaus['EKT']-0.8), data1[:,3],
                 color='blue', ls='-', lw=lw )
    axs[0].plot( (data2[:,0]-0.8)/(maxtaus['FS']-0.8), data2[:,3],
                 color='blue', ls='--', lw=lw )
    axs[0].plot( (data3[:,0]-0.4)/(maxtaus['no']-0.4), data3[:,3],
                 color='blue', ls='-.', lw=lw )
    axs[0].plot( (data4[:,0]-1.16)/(maxtaus['Duke']-1.16), data4[:,3],
                 color='blue', ls=':', lw=lw )
    
    axs[1].plot( (data1[:,0]-0.8)/(maxtaus['EKT']-0.8), data1[:,4],
                 color='purple', ls='-', lw=lw )
    axs[1].plot( (data2[:,0]-0.8)/(maxtaus['FS']-0.8), data2[:,4],
                 color='purple', ls='--', lw=lw )
    axs[1].plot( (data3[:,0]-0.4)/(maxtaus['no']-0.4), data3[:,4],
                 color='purple', ls='-.', lw=lw )
    axs[1].plot( (data4[:,0]-1.16)/(maxtaus['Duke']-1.16), data4[:,4],
                 color='purple', ls=':', lw=lw )
    
    axs[2].plot( (data1[:,0]-0.8)/(maxtaus['EKT']-0.8), data1[:,5],
                 color='red', ls='-', lw=lw )
    axs[2].plot( (data2[:,0]-0.8)/(maxtaus['FS']-0.8), data2[:,5],
                 color='red', ls='--', lw=lw )
    axs[2].plot( (data3[:,0]-0.4)/(maxtaus['no']-0.4), data3[:,5],
                 color='red', ls='-.', lw=lw )
    axs[2].plot( (data4[:,0]-1.16)/(maxtaus['Duke']-1.16), data4[:,5],
                 color='red', ls=':', lw=lw )
        
    '''legend1=axs.legend(lc1, ('Causal', 'Indeterminate', 'Acausal'), fontsize=16, loc=(0.47,0.6))
    axs.legend(lc2, ('EKT Kompost', 'FS Kompost', 'no Kompost', 'Duke'), fontsize=16, loc=(0.5,0.2))
    plt.gca().add_artist(legend1)'''

    for ax in axs.ravel():
        ax.set_xlim([0,0.65])
        ax.set_ylim([-0.025,1.025])
        ax.set_xlabel(r'$\Delta\tau/\Delta\tau_{\mathrm{max}}$', fontsize=16)
        #ax.set_xlabel(r'$(\tau-\tau_0)/(\tau_{\mathrm{max}}-\tau_0)$', fontsize=16)
        
    plt.text(0.65, 0.4, r'Causal cells', \
            {'color': 'black', 'fontsize': 14}, transform=axs[0].transAxes,
            horizontalalignment='center', verticalalignment='top')
    plt.text(0.65, 0.4, r'Indeterminate cells', \
            {'color': 'black', 'fontsize': 14}, transform=axs[1].transAxes,
            horizontalalignment='center', verticalalignment='top')
    plt.text(0.65, 0.4, r'Acausal cells', \
            {'color': 'black', 'fontsize': 14}, transform=axs[2].transAxes,
            horizontalalignment='center', verticalalignment='top')

    axs[2].axhline( -1000.0, color='black', ls='-.', label=r'IP-Glasma + MUSIC' )
    axs[2].axhline( -1000.0, color='black', ls='-', label=r'+ EKT K${\o}$MP${\o}$ST' )
    axs[2].axhline( -1000.0, color='black', ls='--', label=r'+ FS K${\o}$MP${\o}$ST' )
    axs[2].axhline( -1000.0, color='black', ls=':', label=r'Trento + FS + VISHNU' )
    axs[2].legend( loc='best', fontsize=14 )
    axs[0].set_ylabel(r'Fraction of total', fontsize=16)

    #plt.show()
    outfilename = path + '/cell_fractions_tau_dependence.pdf'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)



#===============================================================================
if __name__ == "__main__":
    # import datasets
    IPGlasmaEKTKompostMUSIC = np.loadtxt(path + 'MUSIC_v4_PbPb_EKTKompost_results/' \
                                         + 'cell_fractions_tau_dependence.dat')
    IPGlasmaFSKompostMUSIC = np.loadtxt(path + 'MUSIC_v4_PbPb_FSKompost_results/' \
                                         + 'cell_fractions_tau_dependence.dat')
    IPGlasmanoKompostMUSIC = np.loadtxt(path + 'MUSIC_v4_PbPb_noKompost_results/' \
                                         + 'cell_fractions_tau_dependence.dat')
    TrentoFSVishnu = np.loadtxt(path + 'OSUhydro_RESULTS_OPTIMAL_FINAL_TAUFS116_RS1/' \
                                         + 'cell_fractions_tau_dependence.dat')
    
    generate_fraction_time_dependence( IPGlasmaEKTKompostMUSIC, IPGlasmaFSKompostMUSIC,
                                           IPGlasmanoKompostMUSIC, TrentoFSVishnu, 2 )
