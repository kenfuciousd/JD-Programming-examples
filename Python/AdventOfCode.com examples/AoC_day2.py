#AoC_day2.py
#https://adventofcode.com/2023/day/2
import re

def isPossible(inString):
	#parameters: only 12 red cubes, 13 green cubes, and 14 blue cubes
	# takes in a string, each line of a file, in the form "game ##: X green, X blue, X red; ..."
	redCubes = 12
	greenCubes = 13
	blueCubes = 14
	gameList = []
	isTrue = True
	# here we start from the position assuming it's true unless we find it is impossible
	# because one falsehood invalidates the whole line. 

	#Parse the line, after colen to semicolon, then to next semicolon. 
	firstSplit = inString.split(':')
	gamesString = str(firstSplit[1:]) # This pulls off the "Game ##:" piece, since we only want a list of games
	gamesList = gamesString.split(';')
	print(" and the games list looks like: " + str(gamesList))
	for game in gamesList:
		greenTotal = 0 
		redTotal = 0
		blueTotal = 0
		game = game.lower() # just to sanitize in case there's weird cases
		greenType = re.search('\d+ green', game)
		#print("%s %s", greenTotal.group(0), type(greenTotal))
		if(greenType is not None):
			greenTotal = re.search('\d+', str(greenType.group(0))).group(0)
		#print(greenTotal)
		redType = re.search('\d+ red', game)
		#print(type(redTotal), redTotal)
		if(redType is not None):
			redTotal = re.search('\d+', str(redType.group(0))).group(0)
		#print(redTotal)
		blueType = re.search('\d+ blue', game)
		if(blueType is not None):
			blueTotal = re.search('\d+', str(blueType.group(0))).group(0)
		#print(blueTotal)
		# each total should be 0 already from initialization, so if they aren't found, then it's still zero
		if(int(greenTotal) > greenCubes or int(redTotal) > redCubes or int(blueTotal) > blueCubes):
			print(" !!!! Total expected cubes green " + str(greenCubes) + " and red " + str(redCubes) + " and blue " + str(blueCubes) + " in the bag")
			print(" !!!! Found a falsehood at green " + str(greenTotal) + " and red " + str(redTotal) + " and blue " + str(blueTotal))
			return False
		else:
			print("The game ->" + game + "<- is possible, therefore TRUE")
	# if it makes it through the full list without finding falsehood, then it must be true
	if isTrue is False:
		return False
	else: 
		return True

def main():
	print("STARTING Advent of Code Day 2 - cube counter ")

	runningCount = 0
	gameNumber = 0
	gameRegex = '\d+:'

	inFile = open('./day2_input.txt', 'r')
	inLines = inFile.readlines()

	for line in inLines:
		line = line.strip()
		#print("!! file read, line read is: " + line)

		# strip out the game numbe3r
		gameNumber = re.search(gameRegex, line).group(0).replace(':','')
		print("\n### GAME Number is: " + str(gameNumber))
		print("Reminder: max GREEN 13, RED 12, BLUE 14")
		#print(str(isPossible(line)) + "\n \n \n")
		if(isPossible(line)):
			#isPossible takes a string in, spits out a boolean True/False
			print(" TRUTH FOUND, adding starting runningCount " + str(runningCount) + " and game# " + gameNumber)
			runningCount += int(gameNumber)
			print("runningCount now " + str(runningCount))
		#print("runningCount is: " + str(runningCount))
		print("The RUNNINGCOUNT AFTER THE LINE IS " + str(runningCount))
	print(" ++ and finally, the runningCount at the end is: " + str(runningCount))

if __name__ == "__main__":
	main()