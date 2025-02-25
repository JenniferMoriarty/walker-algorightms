import pygame
import random
pygame.init()#initializes Pygame
pygame.display.set_caption("random walk")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
xpos = 400 #start point for x
ypos = 400 #start point for y
xdir = 1
ydir = 1


#render section---------------------------------------------
    
for i in range(5000): #loop a bunch of times
    xRoll = random.randrange(1, 50) #change x direction if you generate a 1 
    yRoll = random.randrange(1, 50) #change y direction if you generate a 1  

    if xRoll == 1:
        xdir *= -1
        xpos += xdir
    else:
        xpos += xdir
        
    if yRoll == 1:
        ydir*=-1
        ypos += ydir
    else:
        ypos += ydir
        
    #start back in the middle if you go off the screen
    if xpos > 800 or xpos <0:
        xpos = 400
    if ypos > 800 or ypos< 0:
        ypos = 400

    pygame.draw.ellipse(screen, (100, 100, 200), (xpos,ypos, 8, 8))

    pygame.display.flip()


while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #close game window
        break

#end game loop##############################################
pygame.quit()
