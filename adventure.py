# Use this as a template to code your own adventure!

def main():
	introduction = ''  #insert some text to introduce your game!
	print(introduction)
	
	name = get_player_info()
	player = Player(name)
	play(player)

	print('The End.')


def get_player_info():
	x = input('Enter your name: ')
	return x


def play(player):
	while (player.get_life() >= 1):
		x = input('Do you wish to continue? (y/n): ')
		if x == 'y':
			level_one()
		else:
			break


def level_one():
	#add a new level and story
	story = ''
	print(story)


'''
Here is the player class that creates an object with a name, 3 lives, and 0 points
You can use this class to keep track of lives throughout the game and gain and lose points
'''
class Player:
	def __init__(self, name):
		self.name = name
		self.lives = 3
		self.points = 0

	def get_name(self):
		return self.name

	def get_life(self):
		return self.lives

	def lose_life(self):
		self.lives -= 1

	def gain_life(self):
		self.lives += 1

	def get_points(self):
		return self.points

	def lose_points(self):
		self.points -= 1

	def gain_points(self):
		self.points += 1


if __name__ == "__main__":
	main()