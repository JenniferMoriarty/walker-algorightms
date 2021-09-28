import pygame
import random
pygame.init()#initializes Pygame
pygame.display.set_caption("random walk")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((0, 150, 0))
xpos = 400 #start point for x
ypos = 400 #start point for y
#render section---------------------------------------------

for i in range(100000): #loop this whole process 100,000 times(or more)
    xdir = random.randrange(1, 3)#randomly generate a 1 or 2
    ydir = random.randrange(1, 3)#randomly generate another 1 or 2  
    if xdir == 1:#if we generated a 1, go left, otherwise go right
        xpos +=1
    else:
        xpos -=1
    if ydir == 1:#if we generated a 1 the second time, go up, otherwise go down
        ypos +=1
    else:
        ypos -=1

    pygame.draw.ellipse(screen, (200, 200, 0), (xpos,ypos, 8, 8))

    pygame.display.flip()


#while True:
#    event = pygame.event.wait()
#    if event.type == pygame.QUIT: #close game window
#        break

#end game loop##############################################
pygame.quit()





