#day1

#https://adventofcode.com/2023/day/1
#https://adventofcode.com/2023/day/1/input

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

#main function
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