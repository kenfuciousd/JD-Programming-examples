#day2.py
#https://adventofcode.com/2023/day/1#part2
import re

def findFirst(inString):
	#print("@ now looking for the First digit")
	inString = convertAlphaToNum(inString)	
	for i in inString:
		#print ("  -  testing " + i + " inside of " + inString)
		if(i.isdigit()):
			#print("  ---  found " + i + " as a digit")
			firstDigi = i
			break
	print("! FOUND First is " + firstDigi + " in: " + inString)
	return firstDigi

def findLast(inString):
	#print("@ now looking for the Last digit")
	reString = convertAlphaToNum(inString)
	reString = reString[::-1]
	for i in reString:
		#print ("  -  testing " + i + " inside of " + reString)
		if(i.isdigit()):
			#print("  ---  found " + i + " as a digit")
			lastDigi = i
			break
	print("! FOUND Last is " + lastDigi + " rev: " + reString)
	return lastDigi

def convertAlphaToNum(inString):
	#noting --- so, the input has overlapping numbers to catch this kind of replace all method. 
	# the solution is to implement it "lookahead" style (?)
	#digitMap = {
	#	'one': '1',
	#	'two': '2',
	#	'three': '3',
	#	'four': '4',
	#	'five': '5',
	#	'six': '6',
	#	'seven': '7',
	#	'eight': '8',
	#	'nine': '9',		
	#}

	#pattern = re.compile(r"[0-9]|one|two|three|four|five|six|seven|eight|nine")
	#pattern = re.compile(r"\b(?:' + '|'.join(digitMap.keys()) + r')(?:(?=\s*\w)|(?=$))", re.IGNORECASE)
	#result = pattern.sub(lambda match: digitMap[match.group(0).lower()], inString)
	#return result

#	print(matches.group())
#	for match in matches:
		#s = match.start()
		#e = match.end()
#		word = str(match.group(1))
#		print("from Numberfier, found " + word)

	# this is the sanitization version - it's not as good as using a solid regex, but the above piece didn't work
	inString = inString.replace("one", "onee")
	inString = inString.replace("two", "twoo")		
	inString = inString.replace("three", "threee")
	inString = inString.replace("four", "fourr")
	inString = inString.replace("five", "fivee")
	inString = inString.replace("six", "sixx")
	inString = inString.replace("seven", "sevenn")
	inString = inString.replace("eight", "eightt")
	inString = inString.replace("nine", "ninee")		

	inString = inString.replace("one", "1")
	inString = inString.replace("two", "2")		
	inString = inString.replace("three", "3")
	inString = inString.replace("four", "4")
	inString = inString.replace("five", "5")
	inString = inString.replace("six", "6")
	inString = inString.replace("seven", "7")
	inString = inString.replace("eight", "8")
	inString = inString.replace("nine", "9")		

	#inString = inString.lower()
	#inString = inString.replace("eleven", "11")
	#inString = inString.replace("twelve", "12")
	#inString = inString.replace("thirteen", "13")
	#inString = inString.replace("fourteen", "14")
	#inString = inString.replace("fifteen", "15")
	#inString = inString.replace("sixteen", "16")
	#inString = inString.replace("seventeen", "17")
	#inString = inString.replace("eighteen", "18")
	#inString = inString.replace("nineteen", "19")
	#inString = inString.replace("twenty", "20")	
	#inString = inString.replace("thirty", "30")	
	#inString = inString.replace("fourty", "40")	
	#inString = inString.replace("fifty", "50")	
	#inString = inString.replace("sixty", "60")	
	#inString = inString.replace("seventy", "70")	
	#inString = inString.replace("eighty", "80")	
	#inString = inString.replace("ninty", "90")	
	#inString = inString.replace("hundred", "00")		
	#inString = inString.replace("zero", "0")
	## does not work - misses a couple of them like "twone" = 21

	#print("!== returning numerified: " + inString)
	return inString

def main():
	print("STARTING ANALYSIS")
	firstDigi = 0
	lastDigi = 0
	inString = 0
	runningCount = 0

	inFile = open('./day1_input.txt', 'r')
	inLines = inFile.readlines()

	for line in inLines:
		line = line.strip()
		print("!! file read, line read is: " + line)
		firstDigi = findFirst(line)
		lastDigi = findLast(line)
		print(" - endline -  ---- found " + str(firstDigi) + str(lastDigi))
		runningCount += (int(firstDigi) * 10) + int(lastDigi)
		print("runningCount is: " + str(runningCount))
	print(" ++ and finally, the runningCount at the end is: " + str(runningCount))

if __name__ == "__main__":
	main()