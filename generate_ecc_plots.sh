#!/usr/bin/env bash
#------------------

cwd=`pwd`

filePath=`readlink -e $1`
fileDirec=`dirname $filePath`
fileName=`basename $filePath`

eDec=$3

regenerateFrames=true
if [ "$regenerateFrames" = true ]
then
(
	cd $fileDirec
	rm -rf ecc_frames
	mkdir ecc_frames

	awk 'NR>1' $filename > newFileNoHeader.dat

	# assuming same number of lines for each tau...
	split --lines=$2 -d --suffix-length=4 newFileNoHeader.dat ecc_frames/frame
	echo 'Length:' `wc -l newFileNoHeader.dat`
	rm newFileNoHeader.dat

	nFiles=`\ls -1 ecc_frames/frame* | wc -l`
	for i in $(seq -f "%04g" $nFiles $[nFiles+10])
	do
		echo > ecc_frames/frame${i}
	done
	for file in ecc_frames/frame*
	do
		mv $file $file".dat"
	done

	# generate the files from which to compute ecc at each time step
	cd ecc_frames/
	for file in frame*.dat
	do
		paste ../frames/$file $file | column -t > ecc_${file}
	done

	cd ..
)
fi

# Get total number of frames
i=`\ls -1 $fileDirec/ecc_frames/ecc_frame*.dat | wc -l`

# This generates frames for the animations
echo 'Executing python3 generate_ecc_plots.py 0 '$i' '$fileDirec'/ecc_frames '$3
python3 generate_ecc_plots.py 0 $i $fileDirec/ecc_frames $3


