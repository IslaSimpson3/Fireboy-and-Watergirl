import pygame
from pygame.locals import *  
import time


class Player():
	def __init__(self, x, y): #creating player 
		img = pygame.image.load('./iceCube_part2_player1.png')
		self.image = pygame.transform.scale(img, (40, 80))
		self.rect = self.image.get_rect()
		self.rect.x = x #x agrument and y agrument for players measurments  
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.vel_y = 0  #velocity for then the character jumps, gravity pulls it down 
		self.jumped = False
	#self function is a represents the instance of class (refers to the character)

	def update(self):
	#delta x and delta y, when the user presses a key the dx or dy are decreased or increased by 5. records change 
		dx = 0
		dy = 0

		#get keypresses for moving player 
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE] and self.jumped == False:
			self.vel_y = -15
			self.jumped = True
		if key[pygame.K_SPACE] == False:
			self.jumped = False
		if key[pygame.K_LEFT]:
			dx -= 5
		if key[pygame.K_RIGHT]:
			dx += 5


		#add gravity
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		dy += self.vel_y

		#check for collision
		for tile in world.tile_list:
			#check for collision in y direction 
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				#check if below the ground i.e. jumping 
				if self.vel_y < 0:
					dy = tile[1].bottom - self.rect.top
					self.vel_y = 0
				#check if above the ground i.e. falling 
				elif self.vel_y >= 0:
					dy = tile[1].top - self.rect.bottom
					self.vel_y = 0


		#update player coordinates
		self.rect.x += dx
		self.rect.y += dy

		if self.rect.bottom > screen_height:
			self.rect.bottom = screen_height
			dy = 0

		#draw player onto screen
		print("draw player", self.rect, screen_height)
		screen.blit(self.image, self.rect)
		pygame.draw.rect(screen,(255, 255, 255), self.rect, 2)



class World():
	def __init__(self, data):
		self.tile_list = [] #list is empty, then goes thriugh the for loop and recreates the world data list

		#load images
		steps_img = pygame.image.load('/Users/islasim2004gmail.com/Library/CloudStorage/OneDrive-Personal/CCI year 1/Kenneth-coding/images_2playerGame/steps.png')
#goes through each of the items in the world data list via a for loop 
		row_count = 0
		for row in data:
			collum_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(steps_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = collum_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				collum_count += 1
			row_count += 1
#the items in the list are drawn onto the screen 
	def draw(self): 
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])
			pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)


#each number in the list = a tile. if one the tile has the steps image displayed 
world_data = [  
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1], 
[1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1], 
[1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 1, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]



if __name__ == "__main__":
	pygame.init()   #to get pygame inicilised 

	print("hello")
	#layout of game's screen 
	screen_width = 1000
	screen_height = 1000

	screen = pygame.display.set_mode((screen_width, screen_height)) 
	pygame.display.set_caption('Platformer')

	#define game variables
	tile_size = 50


	#load images
	bg_img = pygame.image.load('./jungleBackground.png')


	player = Player(100, 100) #x and y arguments for player 
	world = World(world_data)

	run = True
	while run:   #code of game keeps looping 

		screen.blit(bg_img, (0, 0)) #shows background image onto the screen

		world.draw()

		player.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT: #closes the game 
				run = False

		pygame.display.update()

	pygame.quit() 