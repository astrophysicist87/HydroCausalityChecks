#!/bin/bash
#----------

#for file in ../OSU_hydro/RESULTS_OPTIMAL_FINAL_TAUFS116_RS1/viscous_14_moments_evo.dat
#do
#	path=`readlink -e $file`
#	sbatch --export=ALL,file_to_check=`echo $path`,inGridScale=16.7778,inGridSize=$[235**2],inEDecoupling=0.26511743083794326,inDXY=0.1434 run_all.sbatch
#done


#for file in ../MUSIC/results_PbPb*Kompost/evolution_full.dat
#do
#        path=`readlink -e $file`
#        #sbatch --export=ALL,file_to_check=`echo $path`,inGridScale=20.48,inGridSize=$[512**2],inEDecoupling=0.3,inDXY=0.08 run_all.sbatch
#        sbatch --export=ALL,file_to_check=`echo $path`,inGridScale=20.48,inGridSize=$[512**2],inEDecoupling=0.3,inDXY=0.08 run_frame_generation_only.sbatch
#done


#=======================================================================
# generate eccentricity plots here
for file in ../MUSIC/results_PbPb*Kompost/momentum_anisotropy_grid_eta_-0.5_0.5.dat
do
        path=`readlink -e $file`
        sbatch --export=ALL,e2file=`echo $path`,gridSize=$[512**2],eDecoupling=0.3 generate_ecc_plots.sbatch
done

