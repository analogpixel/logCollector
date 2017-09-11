#!/bin/bash

hostname=`hostname -f`

eval `curl -s {{ serverUrl }}client/jobs/$hostname`
for files in "${logs[@]}"
do

	filenames=${files%:*}
	projectID=${files#*:}
	# echo "files: $filenames projectID: $projectID"
	for file in $filenames
		do
		# echo "Sending $file"
		filename=`basename $file`
		curl -X POST -F fileup=@${file} -F filename=$filename -F projectID=$projectID -F hostname=$hostname {{ serverUrl }}upload
    done
done
