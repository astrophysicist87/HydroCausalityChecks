import numpy as np
import os, sys

# compute average zeta/s
def compute_average_zeta_by_s( data ):
    tau = data[0,0]
    [T,e,P,eta,zeta] = data[:,[3,4,5,7,8]]
    s = (e+P)/T
    eta_by_s = eta/s
    zeta_by_s = zeta/s
    average_T = np.average(T, weights=e)
    average_eta_by_s = np.average(eta_by_s, weights=e)
    average_zeta_by_s = np.average(zeta_by_s, weights=e)
    return tau, average_T, average_eta_by_s, average_zeta_by_s

#===============================================================================
if __name__ == "__main__":
    # load file
    filepath = sys.argv[1]
    path = os.dirname( filepath )
    filename = os.basename( filepath )
    data = np.loadtxt( filepath )
    
    tau, average_T, average_eta_by_s, average_zeta_by_s = compute_average_zeta_by_s( data )
    
    print(tau, average_T, average_eta_by_s, average_zeta_by_s)
