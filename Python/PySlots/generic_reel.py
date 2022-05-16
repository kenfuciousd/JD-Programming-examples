import random

# this reel assumes, for now, the generic basics outlined in the requirements. ... this may need to be reformatted...
### to choose a better behavior pattern. 
 my_reel = {
	'Lucky7_rainbow': ['./assets/Lucky7_rainbow.png', 1],
	'Lucky7': ['./assets/Lucky7.png', 7],
	'bar3': ['./assets/bar3.png', 16],
 	'bar2': ['./assets/bar2.png', 25],
	'bar1': ['./assets/bar1.png', 50],
	'heart_rainbow': ['./assets/heart_rainbow.png', 40],
	'heart': ['./assets/heart.png', 40],
	'clover': ['./assets/clover.png', 40],
	'bell': ['./assets/bell.png', 50],
	'horseshoe': ['./assets/horseshoe.png', 50],
	'cherries': ['./assets/cherries.png', 67],
	'melon': ['./assets/melon.png', 67],
	'lemon': ['./assets/lemon.png', 67], 
}

def spin_reel():
	""" how do I choose to build the pay table? """
	


def randomizer():
	return random.randint(1, 500)

# 			Lucky7_rainbow(1/500), 
#			Lucky7 (7/500), 
#			bar3(16/500), 
#			bar2 (25/500), 
#			bar1(30/500), 
#			heart_rainbow(40/500), heart(40/500), clover(40/500), 
#			bell (50/500), horseshoe (50/500),  
#			cherries(67/500), lemon(67/500), melon(67/500)
#
#		>> each value should be successively add up to 100% chance, corresponding to the paytable in frequency..
#		- the current percentages are a reasonable approximation of good chances, coorelating to the following paytable:
#
#	Rough Paytable outline for Generic Slot Title, per credit bet:
#		Paytable			x1		x3 (only pays more for JP, otherwise just bet value)
#		3 Rainbow 7s: 		500		10,000
#		3 Red 7s:			100		300
#		3 Bar3:				30  	90
#		1 any 7:			25 		75
#		3 bar2: 			20 		40
#		3 bar1: 			10 		30
#		2 any bar: 			5 		15
#		3x heart, clover: 	4 		12
#		3x of any metal		3 		9
#		1 any bar,3x fruit:	2 		6