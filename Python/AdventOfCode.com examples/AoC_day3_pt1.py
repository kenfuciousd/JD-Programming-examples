#AoC_day3_pt1.py

import re

def main():
	print("STARTING Advent of Code Day 3 - adding special-symbol adjacent numbers from file ")

	runningCount = 0

	inFile = './day3_input.txt'
	myFile = open(inFile, '+r').readlines()
	prevLine = ''
	nextLine = ''
	print(len(myFile))
#	with open(inFile) as myFile:
	for num, line in enumerate(myFile, 0):
		#print('## num is ' + str(num) )
		# enumerating from 0 means list-friendly counting 
		if(num>0):
			prevLine = myFile[num-1]
		#print('for sorting nextLine, len(myFile) looks like ' + str(len(myFile)) + ' and num is ' + str(num))
		if(len(myFile) > num+1):
			nextLine = myFile[num+1]
		else:
			nextLine = ''

		print('\n Previous Line is         ' + prevLine)
		print('Current line ' + str(num) + " reading: " + line)
		print(' Next Line is             ' + nextLine + '\n')

		#tests for regex pattern matching go here -
		digitPattern = '\d+'
		symbolPattern = '\p{S}'
		#m = re.match(digitPattern, line)
		#print (m)
		# seems like we'd want match instead of findall... 

		foundNumbers = re.findall(digitPattern, line)
		for foundNum in foundNumbers:
			print("-+-+-+ found " + str(foundNum) )#+ " at " + foundNum.start() + " to " + foundNum.end())
			regexFind = re.search(foundNum, line)
			# do we need to do error checking for digts that match/repeat?  i.e. ....390.....390....
			#print(regexFind.span())
			#print(regexFind.group())
			#print(regexFind.start())
			#print(type(regexFind.end()))
			print(" -- at -- " + regexFind.span() + " starting at " + str(regexFind.start()) + " and ending at " + str(regexFind.end()))
				# use the foundNum to search where it is within the line, get the start/finish
			checkStart = regexFind.start() - 1
			checkEnd = regexFind.end() + 1
				# expand those numbers by +/- 1 and look for a symbolPattern within the prevLine, line, and nextLines"
				# if true, add it to the running count

			runningCount += int(foundNum)

	print(" ++ and finally, the runningCount at the end is: " + str(runningCount))

if __name__ == "__main__":
	main()