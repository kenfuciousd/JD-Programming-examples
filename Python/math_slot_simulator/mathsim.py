# mathsim.py
# 
# requirements: 
#   input: excel file info here
# 
# python packages installed: openpyxl, (vaex?)

import sys
import os
import random
import pandas as pd

### slot machine class
class SlotMachine: 
	credits = 0

# initialize:
	def __init__(self,filepath, reels):
	self.filepath = filepath
	self.reels = reels
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
	reelpos1=random.randint(0,len(reel1)-1)
	reelpos2=random.randint(0,len(reel2)-1)
	reelpos3=random.randint(0,len(reel3)-1)

  	if(reels==5):
	 	reel4 = reel_data['Reel 4']
 		reelpos4=random.randint(0,len(reel4)-1)
	  	reel5 = reel_data['Reel 5']	
 		reelpos5=random.randint(0,len(reel5)-1)

	# 	load paytables
	paytable_data = pd.read_excel(filepath, sheet_name='Paytable')

	#	load paylines
	# load reel window, paylines 

	# create virtual window:
	game_window = [['gh1', 'gh2', 'gh3'], ['gh4', 'gh5', 'gh6'], ['gh7', 'gh8', 'gh8']]
	# meaning it's called like game_window[row][reel]
 	
# adjust credits: 
	def adjust_credits(value):
		# bets should be negative values, wins or deposits positive
		self.credits = self.credits + value
 
# spin reels: 
	def spin_reels():
		
		#STUB: remove wallet value: bet x paylines; check to see if player has enough

	# 	randomly choose reel positions for each of the reels
		reelpos1=random.randint(0,len(reel1)-1)
		reelpos2=random.randint(0,len(reel2)-1)
		reelpos3=random.randint(0,len(reel3)-1)
		# need to add 5 reel logic to the game window stuff later... going to leave this here as a reminder
	  	if(reels==5):
	 		reelpos4=random.randint(0,len(reel4)-1)
	 		reelpos5=random.randint(0,len(reel5)-1)
	 # sets the window positions (reminder, game_window[row][reel])
	 	#if reel1 pos == 0 (or reel's 2 or three), then set (game_window[0][reel]) as reelN[len(reel1)-1)
	 	# else use reelN[reelposN-1]
	 	if(reelpos1==0):
	 		game_window[0][0]=reel1[len(reel1-1)]
	 	else:
	 		game_window[0][0]=reel1[reelpos1-1]
	 	if(reelpos2==0):
	 		game_window[0][1]=reel2[len(reel2-1)]
	 	else:
	 		game_window[0][1]=reel2[reelpos2-1]
	 	if(reelpos3==0):
	 		game_window[0][2]=reel3[len(reel3-1)]
	 	else:
	 		game_window[0][2]=reel3[reelpos3-1]	 		
	 	#the middle row is always true
	 	game_window[1][0] = reel1[reelpos1]
	 	game_window[1][1] = reel2[reelpos2]
	 	game_window[1][2] = reel3[reelpos3]
	 	#if reel1 pos == len(reel1)-1 (or reel's 2 or three), then set (game_window[2][reel]) as reelN[0]
	 	# else use reelN[reelposN+1]
	 	if(reelpos1==len(reel1-1)):
	 		game_window[2][0]=reel1[0]
	 	else:
	 		game_window[2][0]=reel1[reelpos1+1] 
	 	if(reelpos2==len(reel2-1)):
	 		game_window[2][1]=reel2[0]
	 	else:
	 		game_window[2][1]=reel2[reelpos2+1] 
	 	if(reelpos3==len(reel3-1)):
	 		game_window[2][2]=reel3[0]
	 	else:
	 		game_window[2][2]=reel3[reelpos3+1] 
	#	
# call win determination (send each specified payline's values to check against the paytable, #operations are paylines times paytable rows)

class Simulator:
### simulator class
	def __init__(self):
#
# initialize: initial wallet input, number of plays, 
# 



if __name__ == '__main__':
# main class: take input and call the simulator. 
# any simulator head / ui will be here.
	#settings; from file load or UI, later. 
	reel_total = 3
	paylines = 9 

	# set the filepath - this is to be moved to the configuration file / ui input later. 
	filepath='/Users/jdyer/Documents/GitHub/JD-Programming-examples/Python/math_slot_simulator/PARishSheets.xlsx'
	# build slot machine with the filepath

	# start the simulator using the slot machine. 

