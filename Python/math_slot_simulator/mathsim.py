# mathsim.py
# 
# requirements: 
#   input: excel file with three sheets: 'Reels', "Paytable", ""Paylines"
#        Reels should have "Reel label" in row 1, and then each reel should have a set of symbols simulating the reel strip
#            each line should have only a one symbol abbreviation, reflected in the paytable
#        Paytable should have a "Reel label" in row 1, then each row should be a winning combonation
#        Paylines should have each payline with a parenthesis set of numbers, (reel,game-window-position), starting from zero. 
#            like: (0,1) | (1,2) | (2,1) which would look like a downward pointing arrow shape from the second row - _ -
# 
# python packages installed: openpyxl, (vaex?)

import sys
import os
import random
import numpy as np        # random number generator, rounding
import pandas as pd     # for reading Excel
import matplotlib.pyplot as plt  # for displaying math 
import tkinter as tk    # for the gui
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
from tkinter import *
#import pygame

### slot machine class
class SlotMachine: 
    """Slot machine class, takes in the 'input' file as well as the reel # configured """ 
    # initialize, setting allowances to settings:
    def __init__(self,filepath, reels, paylines, bet, initial_credits):
        self.filepath = filepath
        self.reels = reels
        self.paylines = paylines
        self.game_credits = initial_credits 
        self.bet = bet
        #initialize data to be used in the local object namespace, so it's able to be referenced. 
        self.game_window = []
        self.paytable = []
        self.reel1pos=0
        self.reel2pos=0
        self.reel3pos=0
        self.wildsymbols = []

        reel_data = pd.read_excel(filepath, sheet_name='Reels')
        # dataframe_var.shape to get dimensionality: (22,5)    .. so dataframe_var.shape[0] is the rows (depth) and [1] is the columns (width)
        ### the reels, here, are the reel strips. 
        self.reel1 = reel_data['Reel 1']
        self.reel2 = reel_data['Reel 2']
        self.reel3 = reel_data['Reel 3']
        #if(reels==5):
        #     reel4 = reel_data['Reel 4']
        #    reel4pos=random.randint(0,len(reel4)-1)
        #      reel5 = reel_data['Reel 5']    
        #    reel5pos=random.randint(0,len(reel5)-1)

        # chooses the random positions for each of the reels, eventually add the total reel number to pass
        self.randomize_reels()

        # load paytables
        paytable_data = pd.read_excel(filepath, sheet_name='Paytable3')
        # this is where we will call the paytable loader with the data
        self.build_paylines()

        # load reel window, paylines 
        payline_data = pd.read_excel(filepath, sheet_name='Paylines9')
        self.build_pay_table()

        if(reels == 3):
            #print("in initialize: three reels")
            # create virtual window:    (making up unused symbols to track values for deveopment) - also, setting the initial array depth to avoid index errors
            self.game_window = [['gh1', 'gh4', 'gh7'], ['gh2', 'gh5', 'gh8'], ['gh3', 'gh6', 'gh9']]
            # meaning it's called like game_window[reel][row]
            self.build_game_window(self.reel1pos, self.reel2pos, self.reel3pos)
        elif(reels == 5):
            self.game_window = [['gh1', 'gh6', 'gh11', 'gh16', 'gh21'], ['gh2', 'gh7', 'gh12', 'gh17', 'gh22'], ['gh3', 'gh8', 'gh13', 'gh18', 'gh23'], ['gh4', 'gh9', 'gh14', 'gh19', 'gh24'], ['gh5', 'gh10', 'gh15', 'gh20', 'gh25']]
            #build_game_window(reel_pos_all)
        else:
            #output logging goes here. 
            print("Check settings. Choose 3 or 5 reels.")
            quit()
        #end initialization

    def randomize_reels(self):
        #print("before randomize: " + str(self.reel1pos) + " " + str(self.reel2pos) + " " + str(self.reel3pos))
        self.reel1pos=random.randint(0,len(self.reel1)-1)
        self.reel2pos=random.randint(0,len(self.reel2)-1)
        self.reel3pos=random.randint(0,len(self.reel3)-1)
        # need to add 5 reel logic to the game window stuff later... going to leave this here as a reminder
        #if(reels==5):
        #    reelpos4=random.randint(0,len(reel4)-1)
        #    reelpos5=random.randint(0,len(reel5)-1)
        #print("after randomization, reel positions: " + str(self.reel1pos) + " " + str(self.reel2pos) + " " + str(self.reel3pos))

    def adjust_credits(self,value):
         # bets should be negative values, wins or deposits positive
        #print("Adjusting credits at " + str(value))
        self.game_credits = np.round(self.game_credits + value, 2)
        #print("Adjusting credits, now: " + str(self.game_credits))

    def return_credits(self):
         return self.game_credits

    def reset_wildsymbols(self):
        """this function is used to reset the wildsymbols list, to assist the 'is_a_win' function, so that "any bars" or "any 7s", etc, don't get 'stuck' in the test """
        self.wildsymbols = ['W']
        #print("resetting wildsymbols: " + str(self.wildsymbols))

    # note will need to change these inputs, to allow for >3
    def build_game_window(self, reel1pos, reel2pos, reel3pos):
        #for now: 3 reels, more logic later - like sending a list of the positions, so it's size agnostic. 
        #     sets the window positions (reminder, game_window[row][reel])
        #if reel1 pos == 0 (or reel's 2 or three), then set (game_window[reel][0]) as reelN[len(reel1)-1)
        # else use reelN[reelposN-1]
        #print(str(reel1pos) + " " + str(reel2pos) + " " + str(reel3pos) + " " + str(len(self.reel1)-1) + " " + str(self.reel1[len(self.reel1)-1]))
        if(self.reel1pos==0):
            self.game_window[0][0]=self.reel1[len(self.reel1)-1]
        else:
            self.game_window[0][0]=self.reel1[self.reel1pos-1]
        if(self.reel2pos==0):
            self.game_window[1][0]=self.reel2[len(self.reel2)-1]
        else:
            self.game_window[1][0]=self.reel2[self.reel2pos-1]
        if(self.reel3pos==0):
            self.game_window[2][0]=self.reel3[len(self.reel3)-1]
        else:
            self.game_window[2][0]=self.reel3[self.reel3pos-1]             
        #the middle row is always true
        self.game_window[0][1] = self.reel1[self.reel1pos]
        self.game_window[1][1] = self.reel2[self.reel2pos]
        self.game_window[2][1] = self.reel3[self.reel3pos]
        #if self.reel1 pos == len(self.reel1)-1 (or self.reel's 2 or three), then set (self.game_window[self.reel][2]) as self.reelN[0]
        # else use self.reelN[self.reelposN+1]
        if(self.reel1pos==len(self.reel1)-1):
            self.game_window[0][2]=self.reel1[0]
        else:
            self.game_window[0][2]=self.reel1[self.reel1pos+1] 
        if(self.reel2pos==len(self.reel2)-1):
            self.game_window[1][2]=self.reel2[0]
        else:
            self.game_window[1][2]=self.reel2[self.reel2pos+1] 
        if(self.reel3pos==len(self.reel3)-1):
            self.game_window[2][2]=self.reel3[0]
        else:
            self.game_window[2][2]=self.reel3[self.reel3pos+1]
        ##handling for reels 4 and 5 could be here, when configured. If reels==5, do the same thing as above for all three positions, but for 5x5
        #print(self.game_window)

    def build_pay_table(self):
        #to replace with loading it in...  so in excel, 4 columns, reelNum text fields followed by the win amount
        #accessible in object with:  paytable[each_win_line from 0 to len-1][0 to len-1 for each symbol and the value]
        self.paytable = [
            ('W','W','W',100),
            ('B7','B7','B7',20),
            ('R7','R7','R7',20),
            ('*7','*7','*7',10),
            ('3B','3B','3B',6),
            ('2B','2B','2B',2),
            ('1B','1B','1B',1),
            ('*B','*B','*B',0.4)
        ]
        # determine baseline wilds, which will always apply when encounterd
        self.wildsymbols = ['W']

    def build_paylines(self):
        #first payline: middle line; the 'reel positions'
#        paylines=[(0,1),(1,1),(2,1)]

        # this is what should be loaded from the excel sheet later
        #referenced by paylines[full-payline][payline-item-number][either 0 for reel, or 1 for position]
        #so paylines[0][2] is the third reel position to check at game_window[2][0], [2]reel three, [0]top position.
        self.paylines=[
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
    def is_a_win(self):
        #check payline from the reels, sending over the gamewindow array
        # so..  for each payline, grab the symbols from the game window compare to the whole paytable win list 
        #if it matches one of those lines (wild logic here), then pull the len-1 entry for that line
        for line in self.paylines:
            symbols=[]
            winbreak = 0
            for reel_pos in line:
                symbols.append(self.game_window[reel_pos[0]][reel_pos[1]])
            #print("testing symbols: " + str(symbols) )  # this is pulling game window correctly
            #test against paytable
            self.reset_wildsymbols()
            for payline in self.paytable:
                #######  this is where it needs reworked ######
                #print(".. against payline" + str(payline) + " ...")
                #from here: do the symbols for each reel spot match? so symbol[]
                for reelnum in range(0, self.reels):
                    # reworking logic..
                    #print(" - testing reel: " + str(reelnum+1) + " for " + str(symbols[reelnum]) + " versus " + str(payline[reelnum]))
                    # TODO: will need to add logic for "wilds" ***   ***   ***   ***   ***   ****\

                    if "*" in str(payline[reelnum]):
                        #print("Found an Any Type Symbol")
                        if payline[reelnum] == '*B':
                            for sym in ['B7', '1B','2B', '3B']:
                            # eventually, logic to include the right ones from the reel.
                                self.wildsymbols.append(sym)
                            #print(" - appended Bars")
                        elif payline[reelnum] == '*7':
                            for sym in ['B7','R7']:
                                self.wildsymbols.append(sym)
                            #print(" - appended 7s")

                    # win logic                     ### NOTE: Winning logic is *HERE* 
                    if((symbols[reelnum] == payline[reelnum]) or (symbols[reelnum] in self.wildsymbols)):
                        #if they do not match at any time, return false 
                        #print("Match: " + symbols[reelnum]  + " vs " + payline[reelnum] + " on reelnum: " + str(reelnum+1)) # + " and testing reels: " + str(self.reels))
                        #payout is the last entry on the payline
                        if(reelnum + 1 == self.reels):
                            self.reset_wildsymbols()
                            print("WIN! winning: " + str(payline[len(payline)-1]) + " credits, and the payline: " + str(symbols))
                            self.adjust_credits(payline[len(payline)-1])
                            winbreak = 1
                            #return True
                    else:
                        self.reset_wildsymbols()
                        break
                        #else, if it's the last reel, and it didn't match, 
                ##### double check above
                # this is to not give double rewards to the same line - in python, the test is nested, and break doesn't work inside of it due to logic. 
                if(winbreak == 1):
                    winbreak = 0
                    break

    def debug_win_jackpot(self):
        # only for testing, REMOVE BEFORE ANY PRODUCTION LEVEL TESTING
        self.build_game_window(2, 2, 2)

    # spin reels: 
    def spin_reels(self):
        total_bet = self.bet * float(paylines_total)
        if(self.game_credits < total_bet):
            # return "not enough credits!" or something and be done. -- needs a little work
            print("Not enough credits, $" + str(total_bet) + " is required.")
            quit()
            #.. later: when we run out of credits, but want to test a total # of runs..  a cash injection? 
        #print("betting: " + str(total_bet*-1))
        self.adjust_credits(total_bet * -1)
        #STUB: remove wallet value: bet x paylines; check to see if player has enough

    #     randomly choose reel positions for each of the reels
        self.randomize_reels()
        #self.debug_win_jackpot()
        self.build_game_window(self.reel1pos, self.reel2pos, self.reel3pos)
        self.is_a_win()


class Simulator():
    """ simulator class: takes in the SlotMachine class object, does stuff and tracks it. """
    def __init__(self, sm, simnum):
        for iteration in range(simnum):
            #print("spinning")
            sm.spin_reels()
            print("spin " + str(iteration) + " and credits $" + str(sm.return_credits()))
        # initialize: initial wallet input, number of plays, and keeps records for printing for now

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.slot_ready = False
        self.geometry("400x300")
        #self.frame = ttk.Frame(self)
        #self.frame.pack()

        # default text/value entries
        self.reel_total = 3
        self.paylines_total = 9 
        self.bet = 0.25
        # so, initially, each total bet is 2.25
        # .. simulator settings: 
        self.initial_credits = 1000
        self.simruns = 10
        self.filepath='/Users/jdyer/Documents/GitHub/JD-Programming-examples/Python/math_slot_simulator/PARishSheets.xlsx'
        self.label_bet = tk.Label(self, text="Filepath")
        self.label_bet.pack( side = LEFT)
        # UI element values
        self.file_entry = ttk.Entry(self)
        self.file_entry.insert(0,"./PARishSheets.xlsx")
        self.file_entry.pack(padx = 15, pady = 15, side = RIGHT)
        #input file...
        #filepath='/Users/jdyer/Documents/GitHub/JD-Programming-examples/Python/math_slot_simulator/PARishSheets.xlsx'
        #button entries
        self.label_bet = tk.Label(self, text="Bet")
        self.label_bet.pack( side = LEFT)
        self.bet_entry = ttk.Entry(self, width = 8)
        self.bet_entry.insert(0,self.bet)
        self.bet_entry.pack(padx = 15, pady = 15, side = RIGHT)
        self.label_cred = tk.Label(self, text="Starting Credits")
        self.label_cred.pack( side = LEFT)
        self.credit_entry = ttk.Entry(self, width = 8)
        self.credit_entry.insert(0,self.initial_credits)
        self.credit_entry.pack(padx = 15, pady = 15, side = RIGHT)
        self.label_build_sim = tk.Label(self, text="1. Build the Virtual Slot ")
        self.label_build_sim.pack( side = LEFT)
        self.run_button = ttk.Button(self, text="Build Virtual Slot")
        self.run_button['command'] = self.sim_button_clicked       
        self.label_simruns = tk.Label(self, text="Simulator Runs")
        self.label_simruns.pack( side = LEFT)
        self.simrun_entry = ttk.Entry(self, width = 10)
        self.simrun_entry.insert(0,self.simruns)
        self.simrun_entry.pack(padx = 15, pady = 15, side = RIGHT)
        #Run Button
        self.run_button = ttk.Button(self, text="2. Run Simulation ")
        self.run_button['command'] = self.sim_button_clicked
        self.mainloop()

    def build_slot(self, filepath, reels, paylines, bet, initial_credits):
        self.sm = SlotMachine(self.filepath, self.reel_total, self.paylines_total, self.bet, self.initial_credits)
        self.slot_ready = True

    def sim_button_clicked(self):
        #start simulation here...
        print("buttonpress")
        if(self.slot_ready == True):
            sim = Simulator(self.sm, self.simruns)
        else:
            print("Slot needs to be loaded first.")

if __name__ == '__main__':
    """ main class: take input and call the simulator. """
    # any simulator head / ui will be here.
    #settings; from file load or UI, later. 
    reel_total = 3
    paylines_total = 9

    # UI Values 
    bet = 0.25
    # so, initially, each total bet is 2.25
    # .. simulator settings: 
    initial_credits = 1000
    simruns = 10

    # set the filepath - this is to be moved to the configuration file / ui input later.  literally the worst way to do this atm: 
    filepath='/Users/jdyer/Documents/GitHub/JD-Programming-examples/Python/math_slot_simulator/PARishSheets.xlsx'

    # GUI call here
    sim_gui = Gui()
    #sim_gui.mainloop()

    # build slot machine with the filepath
    sm = SlotMachine(filepath, reel_total, paylines_total, bet, initial_credits)
    # start the simulator using the slot machine. 
    sim = Simulator(sm, simruns)