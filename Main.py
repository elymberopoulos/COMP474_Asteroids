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
    fps = 30
    clock = pygame.time.Clock()
    gameWindow = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption("Asteroids")

    #Key press variables
    leftDown = False
    rightDown = False
    moveUp = False
    moveDown = False

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #SHIP POSITION
    shipX = windowWidth/2
    shipY = windowWidth/2
    shipSpeed = 2

    gameLoopRunning = True
    while(gameLoopRunning):


        #Possible bounding box for initial ship
        pygame.draw.ellipse(gameWindow, WHITE, (shipX, shipY, 20, 30))

        #Draw Triangle
        # pygame.draw.lines(gameWindow, WHITE, True, ((400, 350), (450, 400), (350, 400), 1))
        pygame.display.update()

        #Monitor the FPS of the game
        clock.tick(fps)



        #Check for user input to quit the game
        for event in pygame.event.get():
            # ________________________________________
            # check keyboard events - keydown
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftDown = True

                if event.key == pygame.K_RIGHT:
                    rightDown = True

                if event.key == pygame.K_UP:
                    moveUp = True

                if event.key == pygame.K_DOWN:
                    moveDown = True

#Check to see if key is pressed and animate movement if True
            if leftDown:
                shipX -= shipSpeed
                if shipX < 0.0:
                    shipX += shipSpeed

            if rightDown:
                shipX += shipSpeed
                if shipX > windowWidth:
                    shipX -= shipSpeed

            if moveUp:
                shipY -= shipSpeed
                if shipY < 0.0:
                     shipY += shipSpeed

            if moveDown:
                shipY += 2
                if shipY > windowHeight:
                    shipY -= shipSpeed
#End of animate boolean check

# check keyboard events - keyup
# If key released then the boolean is set to false and player stops moving
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftDown = False
                if event.key == pygame.K_RIGHT:
                    rightDown = False
                if event.key == pygame.K_UP:
                    moveUp = False
                if event.key == pygame.K_DOWN:
                    moveDown = False;


        # ________________________________________
            if event.type == pygame.QUIT:
                gameExit()

        gameWindow.fill(BLACK)
        # 'flip' display - always after drawing...
        pygame.display.flip()


if __name__ == '__main__':
    main()