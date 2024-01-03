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
		print('num is ' + str(num) )
		# enumerating from 0 means list-friendly counting 
		if(num>0):
			prevLine = myFile[num-1]
		print('for sorting nextLine, len(myFile) looks like ' + str(len(myFile)) + ' and num is ' + str(num))
		if(len(myFile) > num+1):
			nextLine = myFile[num+1]
		else:
			nextLine = ''

		print('\n Previous Line is       ' + prevLine)
		print('Current line ' + str(num) + " reading: " + line)
		print(' Next Line is       ' + nextLine + '\n')

		#tests for regex pattern matching go here -
		digitPattern = '\d+'
		symbolPattern = '\p{S}'
		#m = re.match(digitPattern, line)
		#print (m)
		# seems like we'd want match instead of findall... 

		foundNumbers = re.findall(digitPattern, line)
		for foundNum in foundNumbers:
			print("-1-1-1 found " + str(foundNum) + " at " + foundNum.start() + " to " + foundNum.end())
			#if the found number has a symbol near it return true

			runningCount += int(foundNum)

	print(" ++ and finally, the runningCount at the end is: " + str(runningCount))

if __name__ == "__main__":
	main()