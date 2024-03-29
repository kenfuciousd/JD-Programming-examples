import sys
import pygame

from settings import Settings

class Slots: 
	"""The main class for the game."""

	def __init__(self):
		"""initialize game"""
		pygame.init();
		# get the settings
		self.settings = Settings()

		# display settings
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Goosey Slots")

	def run_game(self):
		"""Main Game Loop"""
		while True:
			# watch for keyboard/mouse events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# redraw during each pass
			self.screen.fill(self.settings.bg_color)

			# updates the full display, most recently drawn screen
			pygame.display.flip()

class Reel:
	""" each reel should handle itself, as it's a logical unit of division within the Slot Machine """
	def __init__(self):
		# build the reel: first iteration it'll need a symbol upon instantiation
		# initialize symbols - pull from a separate reel input.
		# It should know it's symbol, and the paytable percentage 

	def spin:
		#return a new symbol, calling the randomizer



if __name__ == '__main__':
	#create an instance of, and run the game
	my_slots = Slots()
	my_slots.run_game()