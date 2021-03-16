import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os, sys

hbarc = 0.19733     # GeV*fm
path = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/all_results/"

maxtaus = {'EKT': 18.4, 'FS': 19.6, 'no': 19.2, 'Duke': 12.2}
colors = ['orange', 'green', 'blue', 'purple', 'red']

#===============================================================================
def generate_individual_fraction_time_dependence( fractionTimeDependence ):
    fig, axs = plt.subplots( nrows=1, ncols=1, figsize=(6,6) )

    axs.plot( fractionTimeDependence[:,0], fractionTimeDependence[:,1], color='orange', lw=2 )
    axs.plot( fractionTimeDependence[:,0], fractionTimeDependence[:,2], color='green', lw=2 )
    axs.plot( fractionTimeDependence[:,0], fractionTimeDependence[:,3], color='blue', lw=2 )
    axs.plot( fractionTimeDependence[:,0], fractionTimeDependence[:,4], color='purple', lw=2 )
    axs.plot( fractionTimeDependence[:,0], fractionTimeDependence[:,5], color='red', lw=2 )
            
    axs.set_xlabel(r'$\tau/\tau_{\mathrm{max}}$', fontsize=16)
    axs.set_ylabel(r'Fraction', fontsize=16)
    axs.legend( loc='best' )

    plt.show()
    #outfilename = outpath + '/cell_fractions_tau_dependence.png'
    #print('Saving to', outfilename)
    #fig.savefig(outfilename, bbox_inches='tight')
    #plt.close(fig)
    
#===============================================================================
def generate_fraction_time_dependence( data1, data2, data3, data4, column, lw, labels ):
    fig, axs = plt.subplots( nrows=1, ncols=1, figsize=(6,6) )

    axs.plot( data1[:,0]/maxtaus['EKT']+0.01, data1[:,column],
              color=colors[column-1], ls='-', lw=lw, label=labels[0] )
    axs.plot( data2[:,0]/maxtaus['FS']+0.01, data2[:,column],
              color=colors[column-1], ls='--', lw=lw, label=labels[1] )
    axs.plot( data3[:,0]/maxtaus['no']+0.01, data3[:,column],
              color=colors[column-1], ls='-.', lw=lw, label=labels[2] )
    axs.plot( data4[:,0]/maxtaus['Duke']+0.01, data4[:,column],
              color=colors[column-1], ls=':', lw=lw, label=labels[3] )
    
    axs.set_xlim([0,1])
    axs.set_ylim([0,1])
    axs.set_xlabel(r'$\tau/\tau_{\mathrm{max}}$', fontsize=16)
    axs.set_ylabel(r'Fraction', fontsize=16)
    axs.legend( loc='best' )

    plt.show()
    #outfilename = outpath + '/cell_fractions_tau_dependence.png'
    #print('Saving to', outfilename)
    #fig.savefig(outfilename, bbox_inches='tight')
    #plt.close(fig)
    
#===============================================================================
def generate_fraction_time_dependence( data1, data2, data3, data4, lw ):
    fig, axs = plt.subplots( nrows=1, ncols=1, figsize=(6,6) )

    axs.plot( data1[:,0]/maxtaus['EKT']+0.01, data1[:,3], color='blue', ls='-', lw=lw )
    axs.plot( data2[:,0]/maxtaus['FS']+0.01, data2[:,3], color='blue', ls='--', lw=lw )
    axs.plot( data3[:,0]/maxtaus['no']+0.01, data3[:,3], color='blue', ls='-.', lw=lw )
    axs.plot( data4[:,0]/maxtaus['Duke']+0.01, data4[:,3], color='blue', ls=':', lw=lw )
    
    axs.plot( data1[:,0]/maxtaus['EKT']+0.01, data1[:,4], color='purple', ls='-', lw=lw )
    axs.plot( data2[:,0]/maxtaus['FS']+0.01, data2[:,4], color='purple', ls='--', lw=lw )
    axs.plot( data3[:,0]/maxtaus['no']+0.01, data3[:,4], color='purple', ls='-.', lw=lw )
    axs.plot( data4[:,0]/maxtaus['Duke']+0.01, data4[:,4], color='purple', ls=':', lw=lw )
    
    axs.plot( data1[:,0]/maxtaus['EKT']+0.01, data1[:,5], color='red', ls='-', lw=lw )
    axs.plot( data2[:,0]/maxtaus['FS']+0.01, data2[:,5], color='red', ls='--', lw=lw )
    axs.plot( data3[:,0]/maxtaus['no']+0.01, data3[:,5], color='red', ls='-.', lw=lw )
    axs.plot( data4[:,0]/maxtaus['Duke']+0.01, data4[:,5], color='red', ls=':', lw=lw )
    
    #l1, = axs.plot( data1[:,0]/maxtaus['EKT']+0.01, -1000.0+0.0*data1[:,5], color='blue' )
    l1 = axs.axhline( -1000.0, color='blue' )
    l2 = axs.axhline( -1000.0, color='purple' )
    l3 = axs.axhline( -1000.0, color='red' )
    lc1 = (l1, l2, l3)

    l4 = axs.axhline( -1000.0, color='black', ls='-' )
    l5 = axs.axhline( -1000.0, color='black', ls='--' )
    l6 = axs.axhline( -1000.0, color='black', ls='-.' )
    l7 = axs.axhline( -1000.0, color='black', ls=':' )
    lc2 = (l4, l5, l6, l7)
    
    #axs.legend(lc1, ['Causal', 'Indeterminate', 'Acausal'], loc=1)
    #axs.legend(lc1, ('Causal'), loc=1)
    legend1=axs.legend(lc1, ('Causal', 'Indeterminate', 'Acausal'), fontsize=16, loc=(0.47,0.6))
    axs.legend(lc2, ('EKT Kompost', 'FS Kompost', 'no Kompost', 'Duke'), fontsize=16, loc=(0.5,0.2))
    #axs.legend(lc2, ['EKT Kompost', 'FS Kompost', 'no Kompost', 'Duke'], loc=4)
    plt.gca().add_artist(legend1)

    axs.set_xlim([0,1])
    axs.set_ylim([0,1])
    axs.set_xlabel(r'$\tau/\tau_{\mathrm{max}}$', fontsize=16)
    axs.set_ylabel(r'Fraction', fontsize=16)
    #axs.legend( loc='best' )

    plt.show()
    #outfilename = path + '/cell_fractions_tau_dependence.pdf'
    #print('Saving to', outfilename)
    #fig.savefig(outfilename, bbox_inches='tight')
    #plt.close(fig)



#===============================================================================
def generate_fraction_time_dependence( data1, data2, data3, data4, lw ):
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
        ax.set_xlim([0,0.75])
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

    axs[2].axhline( -1000.0, color='black', ls='-', label=r'IP-Glasma + EKT Kompost' )
    axs[2].axhline( -1000.0, color='black', ls='--', label=r'IP-Glasma + FS Kompost' )
    axs[2].axhline( -1000.0, color='black', ls='-.', label=r'IP-Glasma + no Kompost' )
    axs[2].axhline( -1000.0, color='black', ls=':', label=r'Trento + FS' )
    axs[2].legend( loc='best', fontsize=14 )
    axs[0].set_ylabel(r'Fraction of total', fontsize=16)

    plt.show()
    #outfilename = path + '/cell_fractions_tau_dependence.pdf'
    #print('Saving to', outfilename)
    #fig.savefig(outfilename, bbox_inches='tight')
    #plt.close(fig)



#===============================================================================
if __name__ == "__main__":
    # import datasets
    IPGlasmaEKTKompostMUSIC = np.loadtxt(path + 'MUSIC_results_PbPb_EKTKompost/' \
                                         + 'cell_fractions_tau_dependence.dat')
    IPGlasmaFSKompostMUSIC = np.loadtxt(path + 'MUSIC_results_PbPb_FSKompost/' \
                                         + 'cell_fractions_tau_dependence.dat')
    IPGlasmanoKompostMUSIC = np.loadtxt(path + 'MUSIC_results_PbPb_noKompost/' \
                                         + 'cell_fractions_tau_dependence.dat')
    TrentoFSVishnu = np.loadtxt(path + 'OSUhydro_RESULTS_OPTIMAL_FINAL_TAUFS116_RS1/' \
                                         + 'cell_fractions_tau_dependence.dat')
    
    # generate individual cell fractions
    #generate_individual_fraction_time_dependence( IPGlasmaEKTKompostMUSIC )
    #generate_individual_fraction_time_dependence( IPGlasmaFSKompostMUSIC )
    #generate_individual_fraction_time_dependence( IPGlasmanoKompostMUSIC )
    #generate_individual_fraction_time_dependence( TrentoFSVishnu )

    # generate cell fraction comparisons
    #for i in range(1,6):
    #    generate_fraction_time_dependence( IPGlasmaEKTKompostMUSIC, IPGlasmaFSKompostMUSIC,
    #                                       IPGlasmanoKompostMUSIC, TrentoFSVishnu, i, 2,
    #                                       ['EKT Kompost', 'FS Kompost', 'no Kompost', 'Duke'] )

    generate_fraction_time_dependence( IPGlasmaEKTKompostMUSIC, IPGlasmaFSKompostMUSIC,
                                           IPGlasmanoKompostMUSIC, TrentoFSVishnu, 2 )
