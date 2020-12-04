#!/bin/bash
#SBATCH -t 16:00:00                  # Job run time (hh:mm:ss)
#SBATCH -N 1                        # Number of nodes
#SBATCH -J serial_job            # Name of batch job
#SBATCH -A qgp
#SBATCH -p qgp
#SBATCH -o serial.o%j              # Name of batch job output file
#SBATCH -e serial.e%j              # Name of batch job output file

echo 'Running ./check_causality' $file_to_check
./check_causality $file_to_check 1> `dirname $file_to_check`/causality_check.dat 2> `dirname $file_to_check`/causality_check.err
#    && cd `dirname $file_to_check` \
#    && zip viscous_14_moments_evo.zip viscous_14_moments_evo.dat \
#    && rm viscous_14_moments_evo.dat \
#    && cd -
echo 'Finished running ./check_causality' $file_to_check
