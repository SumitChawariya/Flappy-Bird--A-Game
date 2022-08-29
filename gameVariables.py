
import pygame
from pygame.locals import *

#Global variables for the game
gameWidth = 1200                         #Game window gameWidth
gameHeight = 700                        #Game window gameHeight
FPS = 400                                #Frames per second

birdHeight = 35                              #Height of the bird
birdWidth = 48                               #Width of the bird
jumpSteps = 15                               #Pixels to move
jumpPixels = 4                               #Pixels per frame
dropPixels = 5                               #Pixels per frame

groundHeight = 95                            #Height of the ground
pipeWidth = 30                               #Width of a pipe
pipeHeight = 310                             #Max Height of a pipe
pipesSpace = 5 * birdHeight                  #Space between pipes
pipesAddInterval = 2000                      #Milliseconds


getNewPipe = USEREVENT + 4                   #Custom event

pygame.init()                                #Initialize pygame

screenResolution = pygame.display.Info()     #Get screen resolution

pygame.quit()                                #Close pygame

gameScores = 0                                #Game gameScore

if(gameScores>=0 & gameScores<10):
    pixelsFrame = 3                              #Pixels per frame (spped)
if(gameScores>=10 & gameScores<20):
    pixelsFrame = 3                              #Pixels per frame (spped)
else:
    pixelsFrame = 3                              #Pixels per frame (spped)
waitClick=True