#!/bin/bash
#----------

cwd=`pwd`

filePath=`readlink -e $1`
fileDirec=`dirname $filePath`
fileName=`basename $filePath`

(
	cd $fileDirec
	mkdir frames
	mkdir slides

	i=0
	j=0
	for t in $(seq 0.6 0.02 20)
	do
		printf "Generating frame %d at t=%f..." $i $t
		awk -v tau=$t '$3==tau' $fileName > frames/frame`echo $i`.dat
		nlines=`wc -l frames/frame${i}.dat | awk '{print $1}'`
		if [ "$nlines" -eq "0" ]; then
			j=$[j+1]
		fi
		if [ "$j" -gt "10" ]; then
			break
		fi

		i=$[i+1]
		printf "done!\n"
	done

	python $cwd/generate_frames.py $2 0 $i `readlink -e frames` `readlink -e slides`

	framesPerSecond=60
	pngs2mp4 $framesPerSecond slides/slide%03d.png out.mp4  
)
