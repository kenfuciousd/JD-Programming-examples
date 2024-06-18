#AoC_day3_pt1.py

import re

def main():
	print("STARTING Advent of Code Day 3 - adding special-symbol adjacent numbers from file ")

	runningCount = 0

	inFile = './day3_input.txt'
#	inFile = './day3_testinput.txt'
	myFile = open(inFile, '+r').readlines()
	prevLine = ''
	nextLine = ''
	#tests for regex pattern matching go here -
	digitPattern = '\d+'
	#symbolPattern = "!@#$%^&*()-+?_=,<>/"
	specialString = "!\"#$%&'()*+,-/:;<=>?@[\]^_`{|}~" # removed period from the list because we want to ignore it

	#print(len(myFile))
	for num, line in enumerate(myFile, 0):
		#print('## num is ' + str(num) )
		# enumerating from 0 means list-friendly counting 
		line = line.strip()
		if(num>0):
			prevLine = myFile[num-1].strip()
		#print('for sorting nextLine, len(myFile) looks like ' + str(len(myFile)) + ' and num is ' + str(num))
		if(len(myFile) > num+1):
			nextLine = myFile[num+1].strip()
		else:
			nextLine = ''

		print('\nLast Line ' + str(num-1) + ' is\t>' + prevLine)
		print('This Line ' + str(num) + ' is\t>' + line)
		print('Next Line ' + str(num+1) + ' is\t>' + nextLine)
		foundNumbers = re.findall(digitPattern, line)
		for foundNum in foundNumbers:
			symbolFound = 0
			#print("\n -+-+-+ found " + str(foundNum) )#+ " at " + foundNum.start() + " to " + foundNum.end())
			regexFind = re.search(foundNum, line)
			# do we need to do error checking for digts that match/repeat?  i.e. ....390.....390....
			#print(regexFind.span())
				# use the foundNum to search where it is within the line, get the start/finish
			if (regexFind.start() == 0):
				checkStart = regexFind.start()
			else:
				checkStart = regexFind.start() - 1
			if(regexFind.end() > len(line)):
				checkEnd = regexFind.end()
			else:
				checkEnd = regexFind.end() + 1
			for thisLine in (prevLine[checkStart:checkEnd], line[checkStart:checkEnd], nextLine[checkStart:checkEnd]):
				print(thisLine)
				if(any(c in specialString for c in thisLine)):
					symbolFound = 1
			if(symbolFound == 1):
				runningCount += int(foundNum)
				print(" !! found " + str(foundNum) + " had a symbol next to it and now runningCount is " + str(runningCount))

	print("Finally, the runningCount at the end is: " + str(runningCount))

if __name__ == "__main__":
	main()