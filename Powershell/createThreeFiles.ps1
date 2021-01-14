# createThreeFiles.ps1 is a quick script to fulfill a technical requirements test
# Author Jason Dyer
#  dec 21 2020
#  for Exclamation Labs technical requirements test. 

$filenames = 'puppy.txt', 'monkey.txt', 'baby.txt'
$filecontent = 'Lassie', 'George', 'Maggie'

#for each file, and each line of content, create file and add content 
foreach ($file in $filenames) { 
	#if the file doesn't exist, create it and add contents
	if (!([System.IO.File]::Exists($file))){
		New-Item "./$file" -ItemType File 
		foreach ($content in $filecontent) { 
			Add-Content "./$file" $content	
		}  
	}
	else { Write-Output "$file found, no additional creation necessary"}
}  

#now, read the files, print their contents
foreach ($file in $filenames){
	Write-Output "Retrieving the content of $file"
	Get-Content $file
}
