#day2.py
#https://adventofcode.com/2023/day/1#part2

def findFirst(inString):
	print("@ now looking for the last digit")
	for i in inString:
		print ("  -  testing " + i + " inside of " + inString)
		if(i.isdigit()):
			print("  ---  found " + i + " as a digit")
			firstDigi = i
			break
	print("! FOUND First is " + firstDigi)
	return firstDigi

def findLast(inString):
	print("@ now looking for the last digit")
	inString = inString[::-1]
	for i in inString:
		print ("  -  testing " + i + " inside of " + inString)
		if(i.isdigit()):
			print("  ---  found " + i + " as a digit")
			lastDigi = i
			break
	print("! FOUND Last is " + lastDigi)
	return lastDigi

def convertAlphaToNum(inString):
	inString = inString.toLower()
	match inString:
		case "one":
			print ("found ONE, converting")
			return 1
		case "two":
			print ("found TWO, converting")
			return 2
		case "three":
			print ("found THREE, converting")
			return 3
		case "four":
			print ("found FOUR, converting")
			return 4	
		case "five":
			print ("found FIVE, converting")
			return 5
		case "six":
			print ("found SIX, converting")
			return 6
		case "seven":
			print ("found SEVEN, converting")
			return 7
		case "eight":
			print ("found EIGHT, converting")
			return 8
		case "nine":
			print ("found NINE, converting")
			return 9
		case "zero":
			print ("found ZERO, converting")
			return 0

def main():
	firstDigi = 0
	lastDigi = 0
	inString = 0
	runningCount = 0

	inFile = open('./day1_input.txt', 'r')
	inLines = inFile.readlines()

	for line in inLines:
		print("!! file read, line read is: " + line)
		firstDigi = findFirst(line)
		lastDigi = findLast(line)
		print(" - endline -  ---- found " + str(firstDigi) + " and " + str(lastDigi))
		runningCount += (int(firstDigi) * 10) + int(lastDigi)
		print("runningCount is: " + str(runningCount))
	print(" ++ and finally, the runningCount is: " + str(runningCount))

if __name__ == "__main__":
	main()