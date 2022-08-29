
import pygame
from pygame.locals import *

#Global variables for the game
gameWidth = 300                         #Game window gameWidth
gameHeight = 530                        #Game window gameHeight
FPS = 60                                #Frames per second

birdHeight = 35                              #Height of the bird
birdWidth = 48                               #Width of the bird
jumpSteps = 15                               #Pixels to move
jumpPixels = 4                               #Pixels per frame
dropPixels = 3                               #Pixels per frame

groundHeight = 73                            #Height of the ground

pixelsFrame = 2                              #Pixels per frame (spped)


pygame.init()                                #Initialize pygame

screenResolution = pygame.display.Info()     #Get screen resolution

pygame.quit()                                #Close pygame

gameScores = 0                                #Game gameScore
waitClick = True                         
