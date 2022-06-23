# mathsim.py
# 
# requirements: 
#   input: excel file with three sheets: 'Reels', "Paytable", ""Paylines"
#		Reels should have "Reel label" in row 1, and then each reel should have a set of symbols simulating the reel strip
#			each line should have only a one symbol abbreviation, reflected in the paytable
#		Paytable should have a "Reel label" in row 1, then each row should be a winning combonation
#		Paylines should have each payline with a parenthesis set of numbers, (reel,game-window-position), starting from zero. 
#			like: (0,1) | (1,2) | (2,1) which would look like a downward pointing arrow shape from the second row - _ -
# 
# python packages installed: openpyxl, (vaex?)

import sys
import os
import random
import pandas as pd
import matplotlib.pyplot as plt

### slot machine class
class SlotMachine: 
	"""Slot machine class, takes in the 'input' file as well as the reel # configured """ 

# initialize:
	def __init__(self,filepath, reels, paylines, bet, initial_credits):
		self.filepath = filepath
		self.reels = reels
		self.paylines = paylines
		self.credits = initial_credits 
		self.bet = bet
		#initialize data tp be used in the local object namespace, so it's able to be referenced. 
		game_window = []
		paytable = []
		reel1pos=0
		reel2pos=0
		reel3pos=0

		# currently setting this to excel formatting. If we decide to use another input format, this should become the "excel loader"
		# initialize reels, load reels info
	#	reel1 = []
	#	reel2 = []
	#	reel3 = []
	#	if(reels==5):
	#		reel4 = []
	#		reel5 = []
		reel_data = pd.read_excel(filepath, sheet_name='Reels')
		# accessed via reel_data['Reel #'][n] where n is the reel position
	 	#dataframe_var.shape to get dimensionality: (22,5)	.. so dataframe_var.shape[0] is the rows (depth) and [1] is the columns (width)
		reel1 = reel_data['Reel 1']
		reel2 = reel_data['Reel 2']
		reel3 = reel_data['Reel 3']
		# set random reel positions

	  	#if(reels==5):
		# 	reel4 = reel_data['Reel 4']
	 	#	reel4pos=random.randint(0,len(reel4)-1)
		#  	reel5 = reel_data['Reel 5']	
	 	#	reel5pos=random.randint(0,len(reel5)-1)

	 	# chooses the random positions for each of the reels, eventually add the total reel number to pass
		randomize()

		# 	load paytables
		paytable_data = pd.read_excel(filepath, sheet_name='Paytable')
		# this is where we will call the paytable loader with the data
		build_paylines()

		#	load paylines
		# load reel window, paylines 
		payline_data = pd.read_excel(filepath, sheet_name='Paylines')
		build_pay_table()

		if(reels == 3):
			# create virtual window:    (making up unused symbols to track values for deveopment)
			#game_window = [['gh1', 'gh4', 'gh7'], ['gh2', 'gh5', 'gh8'], ['gh3', 'gh6', 'gh9']]
			# meaning it's called like game_window[reel][row]
			build_game_window(reel1pos, reel2pos, reel3pos)
		elif(reels == 5):
	 		game_window = [['gh1', 'gh6', 'gh11', 'gh16', 'gh21'], ['gh2', 'gh7', 'gh12', 'gh17', 'gh22'], ['gh3', 'gh8', 'gh13', 'gh18', 'gh23'], ['gh4', 'gh9', 'gh14', 'gh19', 'gh24'], ['gh5', 'gh10', 'gh15', 'gh20', 'gh25']]
	 		#build_game_window(reel_pos_all)
		else:
	 		#output logging goes here. 
	 		print("Check settings. Choose 3 or 5 reels.")
	 		quit()

		#end initialization

	# adjust credits: 
	def adjust_credits(value):
		# bets should be negative values, wins or deposits positive
		print("Adjusting credits at " + value)
		self.credits = self.credits + value

	def return_credits():
 		return self.credits

 	# note will need to change these inputs, to allow for >3
	def build_game_window(reel1pos, reel2pos, reel3pos):
 		#for now: 3 reels, more logic later - like sending a list of the positions, so it's size agnostic. 
	 # sets the window positions (reminder, game_window[row][reel])
	 	#if reel1 pos == 0 (or reel's 2 or three), then set (game_window[reel][0]) as reelN[len(reel1)-1)
	 	# else use reelN[reelposN-1]
		if(reel1pos==0):
	 		game_window[0][0]=reel1[len(reel1-1)]
		else:
			game_window[0][0]=reel1[reel1pos-1]
		if(reel2pos==0):
			game_window[1][0]=reel2[len(reel2-1)]
		else:
			game_window[1][0]=reel2[reel2pos-1]
		if(reel3pos==0):
			game_window[2][0]=reel3[len(reel3-1)]
		else:
			game_window[2][0]=reel3[reel3pos-1]	 		
		#the middle row is always true
		game_window[0][1] = reel1[reel1pos]
		game_window[1][1] = reel2[reel2pos]
		game_window[2][1] = reel3[reel3pos]
		#if reel1 pos == len(reel1)-1 (or reel's 2 or three), then set (game_window[reel][2]) as reelN[0]
		# else use reelN[reelposN+1]
		if(reel1pos==len(reel1-1)):
			game_window[0][2]=reel1[0]
		else:
			game_window[0][2]=reel1[reel1pos+1] 
		if(reel2pos==len(reel2-1)):
			game_window[1][2]=reel2[0]
		else:
			game_window[1][2]=reel2[reel2pos+1] 
		if(reel3pos==len(reel3-1)):
			game_window[2][2]=reel3[0]
		else:
			game_window[2][2]=reel3[reel3pos+1] 
		##handling for reels 4 and 5 could be here, when configured. If reels==5, do the same thing as above for all three positions, but for 5x5


	def build_pay_table():
		#to replace with loading it in...  so in excel, 4 columns, reelNum text fields followed by the win amount
		#accessible in object with:  paytable[each_win_line from 0 to len-1][0 to len-1 for each symbol and the value]
		paytable = 	[
			('W','W','W',100),
			('B7','B7','B7',20),
			('R7','R7','R7',20),
			('*7','*7','*7',10),
			('3B','3B','3B',6),
			('2B','2B','2B',2),
			('1B','1B','1B',1),
			('*B','*B','*B',0.4)
		]

	def build_paylines():
		#first payline: middle line; the 'reel positions'
#		paylines=[(0,1),(1,1),(2,1)]

		# this is what should be loaded from the excel sheet later
		#referenced by paylines[full-payline][payline-item-number][either 0 for reel, or 1 for position]
		#so paylines[0][2] is the third reel position to check at game_window[2][0], [2]reel three, [0]top position.
		paylines=[
			[(0,0),(1,0),(2,0)],
			[(0,1),(1,1),(2,1)],
			[(0,2),(1,2),(2,2)],
			[(0,0),(1,1),(2,2)],
			[(0,2),(1,1),(2,0)],
			[(0,0),(1,1),(2,0)],
			[(0,1),(1,2),(2,1)],
			[(0,1),(1,0),(2,1)],
			[(0,2),(1,1),(2,2)]
		]

	# call win determination (send each specified payline's values to check against the paytable, #operations are paylines times paytable rows)
		# did they win? 
		# this should cycle the payline list, (each line pulling the 3 coordinates) 
		# then testing each of those against each paytable line
		# ... with special consideration for wilds, denoted *
	def isAWin():
		#check payline from the reels, sending over the gamewindow array

		# so..  for each payline, grab the symbols from the game window compare to the whole paytable win list 
		#if it matches one of those lines (wild logic here), then pull the len-1 entry for that line
		for line in paylines:
			symbols=[]
			for reel_pos in line:
				symbols.append(game_window[reel_pos[0]][reel_pos[1]])
			#print(str(symbols))  # this is pulling game window correctly
 			#test against paytable
			for payline in paytable:
				#print(str(payline) + " ...")
				#from here: do the symbols for each reel spot match? so symbol[]
				for reelnum in range(reels-1):
					# TODO: will need to add logic for "wilds" ***
					if(symbols[reelnum] != payline[reelnum]):
						#if they do not match at any time, return false 
						return false
					else:
						#payout is the last entry on the payline
						adjust_credits(payline[len(payline)-1])
						return true


	def debug_win_jackpot():
		# only for testing, REMOVE BEFORE ANY PRODUCTION LEVEL TESTING
		build_game_window(2, 2, 2)

	# spin reels: 
	def spin_reels():
		if(self.credits < (self.bet * self.paylines)):
			# return "not enough credits!" or something and be done. -- needs a little work
			print("Not enough credits")
			quit()
			#.. later: when we run out of credits, but want to test a total # of runs..  a cash injection? 

		adjust_credits((self.bet * self.paylines * -1))
		#STUB: remove wallet value: bet x paylines; check to see if player has enough

	# 	randomly choose reel positions for each of the reels
		randomize()
		build_game_window(reel1pos, reel2pos, reel3pos)

	def randomize():
		reel1pos=random.randint(0,len(reel1)-1)
		reel2pos=random.randint(0,len(reel2)-1)
		reel3pos=random.randint(0,len(reel3)-1)
		# need to add 5 reel logic to the game window stuff later... going to leave this here as a reminder
	  	#if(reels==5):
	 	#	reelpos4=random.randint(0,len(reel4)-1)
	 	#	reelpos5=random.randint(0,len(reel5)-1)


class Simulator:
	""" simulator class: takes in the SlotMachine class object, does stuff and tracks it. """
	def __init__(self, sm):
#
# initialize: initial wallet input, number of plays, and keeps records for printing for now
# 



if __name__ == '__main__':
 """ main class: take input and call the simulator. """
	# any simulator head / ui will be here.

	#settings; from file load or UI, later. 
	reel_total = 3
	paylines = 9
	bet = .25 
	initial_credits= 1000
	#initially, each bet is 2.25

	# set the filepath - this is to be moved to the configuration file / ui input later.  literally the worst way to do this atm: 
	filepath='/Users/jdyer/Documents/GitHub/JD-Programming-examples/Python/math_slot_simulator/PARishSheets.xlsx'
	# build slot machine with the filepath
	sm = SlotMachine(filepath, reel_total, paylines, bet, initial_credits)
	# start the simulator using the slot machine. 

