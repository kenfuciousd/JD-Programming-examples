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
	# Reel of Reels [reel1[], reel2[], etc...]
	reels = []


# initialize:
	def __init__(self,filepath):
	# from excel, the following:
	self.filepath = filepath

	reel_data = pd.read_excel (r, sheet_name='Reels' ,'%s', filepath)
	# load reels info
	paytable_data = pd.read_excel (r, sheet_name='Reels' ,'%s', filepath)
# 			
# 	load paytables
# 	load paylines
# 
# adjust wallet: 
# 	update 
# 
# spin reels: 
# 	randomly 

class Simulator:
### simulator class
	def __init__(self):
#
# initialize: initial wallet input, number of plays, 
# 



if __name__ == '__main__':
# main class: take input and call the simulator. 
# any simulator head / ui will be here. 
	filepath = './PARishSheets.xlsx'


