import pygame
import pygame.event
from src.ship import Ship
import sys

def gameExit():
    pygame.quit()
    sys.exit()

def main():
	#Setup basic variables and methods for pygame
	pygame.init()
	windowWidth = 800
	windowHeight = 700
	fps = 45
	clock = pygame.time.Clock()
	gameWindow = pygame.display.set_mode((windowWidth, windowHeight))
	pygame.display.set_caption("Asteroids")
	surface = pygame.Surface((50,50))
	
	#Key press variables
	leftDown = False
	rightDown = False

	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	rotate = 0
	#SHIP POSITION
	shipX = windowWidth/2
	shipY = windowWidth/2
	while not False:       

		for event in pygame.event.get():
			# ________________________________________
			if event.type == pygame.QUIT:
				gameExit()
		rotate = 0
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP]: shipY -= 2
		if pressed[pygame.K_DOWN]: shipY += 2
		if pressed[pygame.K_LEFT]: shipX -= 2
		if pressed[pygame.K_RIGHT]: shipX += 2
		if pressed[ord('a')]: rotate = pygame.transform.rotate(surface,-20)
		if pressed[ord('d')]: rotate= pygame.transform.rotate(surface, 20)
		gameWindow.fill(BLACK)		
		#Possible bounding box for initial ship
		pygame.draw.ellipse(gameWindow, WHITE, (shipX, shipY,20,30))
		pygame.draw.rect(surface, WHITE, pygame.Rect(20,20,60,60))
		gameWindow.blit(surface, [0,0])
		# 'flip' display - always after drawing...
		pygame.display.flip()
		#Monitor the FPS of the game
		clock.tick(fps)

if __name__ == '__main__':
    main()
