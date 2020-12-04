#!/bin/bash
#----------

filePath="$1"
fileDirec=`dirname $filePath`
fileName=`basename $filePath`

(
	cd $fileDirec
	mkdir slides

	python generate_frames.py $2 
)
