# createbashfiles.sh is a quick script to fulfill a technical requirements test
# Author Jason Dyer
#  dec 21 2020
#  for Exclamation Labs technical requirements test. 

#!/usr/local/bin/bash

declare -a FILENAMES
declare -a FILEENTRIES

FILENAMES=("puppy.txt" "monkey.txt" "baby.txt")
FILEENTRIES=("Lassie" "George" "Maggie")

echo "Creating 3 Files"
for FN in ${FILENAMES[*]} 
do
# this section that is commented is the attempt to check to see if files existed first.
# currently throwing an error. 
#	if [[-f "./$FN"]];
#	then
#		echo $FN "exists and does not need to be added."
#	else
		echo "Adding the file:" $FN
		touch $FN
		#Append the text entries into the files
		for FE in ${FILEENTRIES[*]} 
		do
			echo $FE >> $FN
		done
#		echo "Viewing contents of" $FN ":"
#		cat $FN
#	fi
done
	
#check to see what was done.
LS -lisa

# pulling out the content viewing piece, if that was desired:
for FN in ${FILENAMES[*]} 
do
	echo "Contents of File" $FN "are:"
	cat $FN
done

#object cleanup during testing
#for FN in ${FILENAMES[*]}
#do
#	echo "we are removing" $FN
#	rm $FN
#done

#check to see if the files were removed
#LS -lisa