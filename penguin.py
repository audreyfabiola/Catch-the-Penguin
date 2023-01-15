import pygame
import random
from constant import *

class Penguin:
    def __init__(self):
        # Generate random size for the penguin
        random_size_value = random.uniform(PENGUIN_SIZE_RANDOMIZE[0], PENGUIN_SIZE_RANDOMIZE[1])
        size = (int(PENGUIN_SIZE[0] * random_size_value), int(PENGUIN_SIZE[1] * random_size_value))
        # Movement of the penguin
        moving_direction, start_position = self.define_spawn_position()
        # Sprite
        self.rect = pygame.Rect(start_position[0], start_position[1], size[0]//1.4, size[1]//1.4) #Takes in x, y, width, height arguments
        self.images = [] # initialize the images list
        for nb in range(1, 7):
            image = pygame.image.load(f"Assets/Penguin/{nb}.png").convert_alpha()
            # Scale the image
            image = pygame.transform.smoothscale(image, size)
            # Flip the image if moving_direction is "left", because penguin image is facing to the right
            if moving_direction == "left": 
                image = pygame.transform.flip(image, True, False)
            self.images.append(image) # Append the image to the list
        self.current_frame = 0 #Setting the starting frame of the animation to the first image in the list
        self.animation_timer = 0 #Used to synchronize the animation with other events in the game
        self.animation_interval = 50 #Interval

    def define_spawn_position(self):
        velocity = random.uniform(PENGUIN_MOVE_SPEED["min"], PENGUIN_MOVE_SPEED["max"])
        # Choose a random direction for the penguin to move in
        moving_direction = random.choice(("right", "left", "up", "down"))

        # Generate a random starting position
        offset = 50 # Spawns at least 50 pixels away from the edges of the screen
        start_x = random.uniform(offset, SCREEN_WIDTH - offset)
        start_y = random.uniform(offset, SCREEN_HEIGHT - offset)
        start_position = (start_x, start_y)

        # Set the velocity of the penguin based on the moving direction
        if moving_direction == "right":
            self.velocity = [velocity, 0]

        if moving_direction == "left":
            self.velocity = [-velocity, 0]

        if moving_direction == "up":
            self.velocity = [0, -velocity]
        
        if moving_direction == "down":
            self.velocity = [0, velocity]

        return moving_direction, start_position

    # Move the penguin based on its current velocity
    def move(self):
        # Update the rect based on the velocity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    # Updates the frame of the penguin animation based on the elapsed time since the last frame
    def animate(self): 
        self.animation_timer += 1
        if self.animation_timer >= ANIMATION_SPEED:
            self.animation_timer = 0 #Reset the animation timer
            self.current_frame += 1 #Increment the current frame
            
            if self.current_frame >= len(self.images):
                self.current_frame = 0

    # Draw a visual representation of the penguin's collision box (hitbox)
    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect) #Draw rect on the surface using orange color with self.rect as its size and position

    # Draw elements on the game screen
    def draw(self, surface):
        self.animate()
        self.image = self.images[self.current_frame]
        # Draw the image using the self.rect as its position
        surface.blit(self.image, self.rect)
        if DRAW_HITBOX: #The draw_hitbox constant is set to 'False', making it invisible to the player
            self.draw_hitbox(surface)

    # Remove the penguin object from the list of active penguins when it is caught by the player
    def catch(self, active_objects): #using active_objects as parameter, representing a list of penguin objects that represents all of the active penguins in the game.
        active_objects.remove(self) 
        return 1 #+1 point from catching the penguin



