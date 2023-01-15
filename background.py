import pygame
from constant import *

class Background:
    def __init__(self): 
        self.image = pygame.image.load("Assets/background.jpg").convert() #Load the image file and convert() is used to improve the game's speed
        self.image = pygame.transform.smoothscale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT)) #Scaling the image to fit the window's size

    # Drawing the background image onto the window's screen, game evolves here inside
    def draw(self, surface): 
        surface.blit(self.image, (0, 0)) #blit function is used to draw one image onto another






