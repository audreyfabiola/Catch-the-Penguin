import pygame
import random
from constant import *
from penguin import Penguin 

class Bomb(Penguin):
    def __init__(self):
        # Generate random size for the bomb
        random_size_value = random.uniform(BOMB_SIZE_RANDOMIZE[0], BOMB_SIZE_RANDOMIZE[1])
        size = (int(BOMB_SIZE[0] * random_size_value), int(BOMB_SIZE[1] * random_size_value))
        # Movement of the bomb
        moving_direction, start_position = self.define_spawn_position()
        # Sprite
        self.rect = pygame.Rect(start_position[0], start_position[1], size[0]//1.4, size[1]//1.4)
        self.images = [] # initialize the images list
        for nb in range(1, 7):
            image = pygame.image.load(f"Assets/Bomb/{nb}.png").convert_alpha()
            # Scale the image
            image = pygame.transform.smoothscale(image, size)
            # Flip the image if moving_direction is "left", because penguin image is facing to the right
            if moving_direction == "left": 
                image = pygame.transform.flip(image, True, False)
            self.images.append(image) # Append the image to the list
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_interval = 50

    def catch(self, active_objects): # Remove the active bombs from the list
        active_objects.remove(self)
        return -1 #-1 point from catching the bomb




  