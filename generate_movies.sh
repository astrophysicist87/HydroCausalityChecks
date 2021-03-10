#!/usr/bin/env bash
#------------------

#for file in ../iEBE-Plumberg/PlayGround_PbPb*/job-1/VISHNew/results/causality_check.dat
#do
#	sbatch --export=ALL,causality_check_file=$file,gridScale=20,gridSize=$[401**2] generate_movie.sbatch
#done

for file in ../iEBE-Plumberg/PlayGround_AuAu*/job-1/VISHNew/results/causality_check.dat
do
        sbatch --export=ALL,causality_check_file=$file,gridScale=13,gridSize=$[261**2] generate_movie.sbatch
done

#for file in ../iEBE-Plumberg/PlayGround_pp*/job-1/VISHNew/results/causality_check.dat
#do
#        sbatch --export=ALL,causality_check_file=$file,gridScale=10,gridSize=$[201**2] generate_movie.sbatch
#done






#for file in ../iEBE-Plumberg/PlayGround_EA_PbPb_C*%/job-1/VISHNew/results/causality_check.dat
#do
#	#echo 'Submitting' $file
#	sbatch --export=ALL,causality_check_file=$file,gridScale=20,gridSize=$[401**2] generate_movie.sbatch
#done
#
#for file in ../iEBE-Plumberg/PlayGround_EA_AuAu_C*%/job-1/VISHNew/results/causality_check.dat
#do
#        #echo 'Submitting' $file
#        sbatch --export=ALL,causality_check_file=$file,gridScale=20,gridSize=$[401**2] generate_movie.sbatch
#done
#
#for file in ../iEBE-Plumberg/PlayGround_EA_pPb_C*%/job-1/VISHNew/results/causality_check.dat
#do
#        #echo 'Submitting' $file
#        sbatch --export=ALL,causality_check_file=$file,gridScale=15,gridSize=$[301**2] generate_movie.sbatch
#done
#
#for file in ../iEBE-Plumberg/PlayGround_EA_pp_C*%/job-1/VISHNew/results/causality_check.dat
#do
#        #echo 'Submitting' $file
#        sbatch --export=ALL,causality_check_file=$file,gridScale=10,gridSize=$[201**2] generate_movie.sbatch
#done
