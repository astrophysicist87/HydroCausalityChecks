#!/bin/bash
#SBATCH -t 16:00:00                  # Job run time (hh:mm:ss)
#SBATCH -N 1                        # Number of nodes
#SBATCH -J serial_job            # Name of batch job
#SBATCH -A qgp
#SBATCH -p qgp
#SBATCH -o serial.o%j              # Name of batch job output file
#SBATCH -e serial.e%j              # Name of batch job output file

outfile=`dirname $file_to_check`/causality_check.dat
errfile=`dirname $file_to_check`/causality_check.err

sbatch --export=ALL,causality_check_file=$outfile,gridScale=$inGridScale,gridSize=$inGridSize,eDecoupling=$inEDecoupling,dxy=$inDXY generate_movie.sbatch
