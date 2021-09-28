import pygame
import random
pygame.init()#initializes Pygame
pygame.display.set_caption("random walk")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((0, 0, 250))
xpos = 400 #start point for x
ypos = 400 #start point for y
#render section---------------------------------------------


#desert
for j in range (4):
    xpos = 400 #start point for x
    ypos = 400 #start point for y
    for i in range(500000): #loop this whole process 100,000 times(or more)
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

        pygame.draw.ellipse(screen, (200, 200, 0), (xpos,ypos, 10, 10))

    pygame.display.flip()

#grass
for j in range (2):
    xpos = 400 #start point for x
    ypos = 400 #start point for y
    for i in range(100000): #loop this whole process 100,000 times(or more)
        xdir = random.randrange(1, 3)#randomly generate a 1 or 2
        ydir = random.randrange(1, 3)#randomly generate another 1 or 2  
        if xdir == 1:#if we generated a 1, go left, otherwise go right
            xpos +=3
        else:
            xpos -=3
        if ydir == 1:#if we generated a 1 the second time, go up, otherwise go down
            ypos +=3
        else:
            ypos -=3

        pygame.draw.ellipse(screen, (50, 150, 0), (xpos,ypos, 8, 8))

    pygame.display.flip()


#forest
for j in range (4):
    xpos = 400 #start point for x
    ypos = 400 #start point for y
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

        pygame.draw.ellipse(screen, (0, 50, 0), (xpos,ypos, 8, 8))

    pygame.display.flip()



#water again
for j in range (5):
    xpos = 400 #start point for x
    ypos = 400 #start point for y
    for i in range(1000): #loop this whole process 100,000 times(or more)
        xdir = random.randrange(1, 3)#randomly generate a 1 or 2
        ydir = random.randrange(1, 3)#randomly generate another 1 or 2  
        if xdir == 1:#if we generated a 1, go left, otherwise go right
            xpos +=3
        else:
            xpos -=3
        if ydir == 1:#if we generated a 1 the second time, go up, otherwise go down
            ypos +=3
        else:
            ypos -=3

        pygame.draw.ellipse(screen, (0, 0, 250), (xpos,ypos, 8, 8))

    pygame.display.flip()

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #close game window
        break

#end game loop##############################################
pygame.quit()






