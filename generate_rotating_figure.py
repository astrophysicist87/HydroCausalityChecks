###############################################################################
# A code to generate an animation of the freeze-out hypersurface in 3D for
# different values of K_T
##############################
# Author: Christopher Plumberg
##############################
# Date: 01/13/2015
##############################
###############################################################################
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import sys
from subprocess import call

# Set-up
eps = 0.000001
anglemin, anglemax = 0, 360
KTvec = np.linspace(0,2,3)

# Read in command-line arguments
#localpT = float(sys.argv[1])		# Value of p_T to be used in calculations
fileToProcess = sys.argv[1]		# Full path to file to be processed
processingFolder = sys.argv[2]		# Directory to hold output files
ebsvalue = sys.argv[3]			# value of eta/s to use

# Load data
data = np.loadtxt(fileToProcess)

# Set-up figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plotfontsize = 18
transparency = 0.5
symbolscale = 20.0
minimumSymbolSize = 2.5
xlower, xupper = -10.0, 10.0
ylower, yupper = -10.0, 10.0
zlower, zupper = 0.0, 12.0
dummylower, dummyupper = 0.0, 0.0

# Process data and generate basic plot for localpT
pT = data[:,0]
for ilocalpT in xrange(len(KTvec)):
	localpT = KTvec[ilocalpT]
	KTstring = "%0.1f" % localpT
	tau = data[(np.where(abs(pT-localpT) <= eps))[0],1]
	xT = data[(np.where(abs(pT-localpT) <= eps))[0],2]
	yT = data[(np.where(abs(pT-localpT) <= eps))[0],3]
	avgS = data[(np.where(abs(pT-localpT) <= eps))[0],4]
	#rT = np.sqrt(xT**2 + yT**2)
	
	# set vertical position from which to view rotating figure
	vertpos=20.0

	# Set-up figure
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	
	ax.scatter(xT, yT, tau, s=(symbolscale*((avgS-min(avgS))/(max(avgS)-min(avgS)))+minimumSymbolSize), c=((avgS-min(avgS))/(max(avgS)-min(avgS))), alpha=transparency, edgecolor='')
	ax.plot(np.array([dummylower, dummyupper]),np.array([dummylower, dummyupper]),np.array([zlower, zupper]), color='black')
	ax.plot(np.array([dummylower, dummyupper]),np.array([ylower, yupper]),np.array([dummylower, dummyupper]), color='black')
	ax.plot(np.array([xlower, xupper]),np.array([dummylower, dummyupper]),np.array([dummylower, dummyupper]), color='black')
	ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
	ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
	ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
	ax.w_xaxis.gridlines.set_color('black')
	ax.w_yaxis.gridlines.set_color('black')
	ax.w_zaxis.gridlines.set_color('black')
	ax.set_aspect('equal', 'box')
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_zticks([])
	#ax.set_xlabel('x (fm)', {'fontsize': plotfontsize-5})
	#ax.set_ylabel('y (fm)', {'fontsize': plotfontsize-5})
	#ax.set_zlabel(r'$\tau$ (fm/$c$)', {'fontsize': plotfontsize-5})
	ax.axis([xlower, xupper, ylower, yupper])
	ax.set_axis_off()
	
	#plt.show()
	#ax.text2D(0.2, 0.85, '$K_T = $' + KTstring + ' GeV', transform=ax.transAxes, fontsize=plotfontsize + 4)
	#ax.text2D(0.6, 0.85, '$\eta/s = $' + ebsvalue, transform=ax.transAxes, fontsize=plotfontsize + 4)
	ax.text2D(0.105, 0.825, '$K_T = $' + KTstring + ' GeV', transform=ax.transAxes, fontsize=plotfontsize + 4)
	ax.text2D(0.575, 0.825, '$\eta/s = $' + ebsvalue, transform=ax.transAxes, fontsize=plotfontsize + 4)
	ax.text2D(0.15, 0.5, '$\\tau$', transform=ax.transAxes, fontsize=plotfontsize + 4)
	ax.annotate('', xy=(0.17, 0.7), xycoords='axes fraction', xytext=(0.17, 0.55), textcoords='axes fraction', arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
	#ax.text(15, 0, 0, '$x$', fontsize=plotfontsize + 4)
	#ax.text(0, 15, 0, '$y$', fontsize=plotfontsize + 4)
	
	for angle in range(anglemin,anglemax):
		ax.view_init(elev=vertpos, azim=angle)
		temp = angle + ilocalpT*(anglemax-anglemin)
		anglestring="%04d" % temp
		plt.savefig(processingFolder + '/movie_ALL_KT_viewingangle_' + anglestring + '.png', bbox_inches='tight', pad_inches=-0.5)
		print '   --> Completed angle =', temp
	
# Finally, convert *.png files to mp4 and zip them up
framerate = 30							# in frames/second
outputFilename = processingFolder + '/out_ALL_KT.mp4'		# ext., '.mp4'
zipFilename = processingFolder + '/movie_ALL_KT_files.zip'
framesFilepattern = processingFolder + '/*.png'
frameFilename = processingFolder + '/movie_ALL_KT_viewingangle_' + '%04d.png'

convertCommandString = 'pngs2mp4 ' + str(framerate) + ' ' + frameFilename + ' ' + outputFilename
zipCommandString = 'zip -r ' + zipFilename + ' ' + framesFilepattern
cleanCommandString = 'rm ' + framesFilepattern

return_code = call(convertCommandString, shell=True)
return_code = call(zipCommandString, shell=True)
return_code = call(cleanCommandString, shell=True)

# End of file
