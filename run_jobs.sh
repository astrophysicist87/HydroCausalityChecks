#!/bin/bash
#----------

for file in ../iEBE-Plumberg/PlayGround_*/job-1/VISHNew/results/viscous_14_moments_evo.dat
do
	path=`readlink -e $file`
	sbatch --export=ALL,file_to_check=`echo $path` run.sbatch
done
