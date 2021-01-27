import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

path = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/tmp/"

file1 = path + "Charged_eta_integrated_vndata.dat"
file2 = path + "Charged_eta_vndata.dat"

integratedVn = np.loadtxt(file1)
differentialVn = np.loadtxt(file2)
#print integratedVn.shape
#print differentialVn.shape

fig, ax = plt.subplots( nrows=1, ncols=1 )

ax.plot(differentialVn[:,0], 0.0*differentialVn[:,11]+integratedVn[2,-1],'--', color='red')
ax.plot(differentialVn[:,0], 0.0*differentialVn[:,11]+integratedVn[3,-1],'--', color='blue')
ax.plot(differentialVn[:,0], 0.0*differentialVn[:,11]+integratedVn[4,-1],'--', color='green')

ax.plot(differentialVn[:,0], differentialVn[:,8], 'ro-', label=r'$n=2$')
ax.plot(differentialVn[:,0], differentialVn[:,11], 'bs-', label=r'$n=3$')
ax.plot(differentialVn[:,0], differentialVn[:,14], 'g*-', label=r'$n=4$')
ax.plot(differentialVn[:,0], 0.0*differentialVn[:,11], '-', color='black')


ax.set_xlim(left=0.0, right=2.0)
ax.set_ylim(top=0.075)
ax.set_xlabel(r'$p_T$ (GeV)', fontsize=16)
ax.set_ylabel(r'$v_n(p_T)$', fontsize=16)

ax.legend(loc='upper left', fontsize=14, facecolor='white', framealpha=1)    


#plt.show()
outfilename = path + '/plot.pdf'
fig.savefig(outfilename, bbox_inches='tight')
plt.close(fig)
