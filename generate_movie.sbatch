#!/bin/bash
#SBATCH -t 16:00:00                  # Job run time (hh:mm:ss)
#SBATCH -N 1                        # Number of nodes
#SBATCH -J serial_job            # Name of batch job
#SBATCH -A qgp
#SBATCH -p qgp
#SBATCH -o serial.o%j              # Name of batch job output file
#SBATCH -e serial.e%j              # Name of batch job output file

echo 'Starting...'
./generate_movie.sh ../iEBE-Plumberg/PlayGround_EA_AuAu_C50-60%/job-1/VISHNew/results/causality_check.dat 13
echo 'Finished!'
