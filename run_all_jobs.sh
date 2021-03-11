#!/bin/bash
#----------

#for file in ../OSU_hydro/RESULTS_OPTIMAL_FINAL_NOFS/viscous_14_moments_evo.dat
#do
#	path=`readlink -e $file`
#	sbatch --export=ALL,file_to_check=`echo $path`,inGridScale=12.189,inGridSize=$[171**2],inEDecoupling=0.26511743083794326,inDXY=0.1434 run_all.sbatch
#done


for file in ../MUSIC/results_PbPb*Kompost/evolution_full.dat
do
        path=`readlink -e $file`
        sbatch --export=ALL,file_to_check=`echo $path`,inGridScale=20.48,inGridSize=$[512**2],inEDecoupling=0.3,inDXY=0.08 run_all.sbatch
done

