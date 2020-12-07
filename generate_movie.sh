#!/usr/bin/env bash
#------------------

cwd=`pwd`

filePath=`readlink -e $1`
fileDirec=`dirname $filePath`
fileName=`basename $filePath`

(
	cd $fileDirec
	rm -rf frames slides out.mp4
	mkdir frames
	mkdir slides

	# assuming same number of lines for each tau...
	split --lines=$3 -d --suffix-length=3 $fileName frames/frame
	nFiles=`\ls -1 frames/frame* | wc -l`
	#for ((i=$nFiles; i<=$[nFiles+10]; i++))
	for i in $(seq -f "%03g" $nFiles $[nFiles+10])
	do
		echo > frames/frame${i}
	done
	for file in frames/frame*
	do
		mv $file $file".dat"
	done
)
	i=`\ls -1 $fileDirec/frames/frame* | wc -l`
	echo 'Executing python generate_frames.py '$2' 0 '$i' '$fileDirec'/frames '$fileDirec'/slides'
	python generate_frames.py $2 0 $i $fileDirec/frames $fileDirec/slides

(
	cd $fileDirec
	framesPerSecond=60
	pngs2mp4 $framesPerSecond slides/slide%03d.png out.mp4  
        framesPerSecond=5
        pngs2mp4 $framesPerSecond slides/slide_wReg%03d.png out_wReg.mp4
)
