#!/usr/bin/env bash
#SBATCH -t 16:00:00                  # Job run time (hh:mm:ss)
#SBATCH -N 1                        # Number of nodes
#SBATCH -J serial_job            # Name of batch job
#SBATCH -A qgp
#SBATCH -p qgp
#SBATCH -o serial.o%j              # Name of batch job output file
#SBATCH -e serial.e%j              # Name of batch job output file

#chmod +x generate_ecc_plots.sh

echo 'Starting...'
bash generate_ecc_plots.sh $e2file $gridSize $eDecoupling
echo 'Finished!'
