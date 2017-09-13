#!/bin/bash

hostname=`hostname -f`

eval `curl -s {{ serverUrl }}client/jobs/$hostname`
for files in "${logs[@]}"
do

	filename=$(echo $files | cut -f1 -d:)
	projectID=$(echo $files | cut -f2 -d:)

	# echo "files: $filenames projectID: $projectID"
	for file in $filenames
		do
		# echo "Sending $file"
		filename=`basename $file`
		curl -X POST -F fileup=@${file} -F filename=$filename -F projectID=$projectID -F hostname=$hostname {{ serverUrl }}upload
    done
done
