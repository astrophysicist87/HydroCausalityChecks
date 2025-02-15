import numpy as np
import os, sys

hbarC = 0.19733

#====================================================

# compute average zeta/s
def compute_averages( data ):
    tau = data[0,0]
    [T,e,P,eta,zeta] = data[:,[3,4,5,7,8]].T
    s = (e+P)/T
    eta_by_s = eta/s
    zeta_by_s = zeta/s
    average_T = np.average(T, weights=e)
    average_eta_by_s = np.average(eta_by_s, weights=e)
    average_zeta_by_s = np.average(zeta_by_s, weights=e)
    return tau, hbarC*average_T, average_eta_by_s, average_zeta_by_s

#===============================================================================
if __name__ == "__main__":
    # load file
    filepath = sys.argv[1]
    path = os.path.dirname( filepath )
    filename = os.path.basename( filepath )
    data = np.loadtxt( filepath )
    
    tau, average_T, average_eta_by_s, average_zeta_by_s = compute_averages( data )
    
    print(tau, average_T, average_eta_by_s, average_zeta_by_s)
