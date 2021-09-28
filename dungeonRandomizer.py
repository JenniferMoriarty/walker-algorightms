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


    
for i in range(5000): #loop this whole process 100,000 times(or more)
    xRoll = random.randrange(1, 50)#randomly generate a 1 or 2
    yRoll = random.randrange(1, 50)#randomly generate another 1 or 2  
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
        
    if xpos > 800 or xpos <0:
        xpos = 400
    if ypos > 800 or ypos< 0:
        ypos = 400

    pygame.draw.ellipse(screen, (100, 100, 100), (xpos,ypos, 8, 8))

    pygame.display.flip()


while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #close game window
        break

#end game loop##############################################
pygame.quit()






