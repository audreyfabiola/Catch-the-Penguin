import pygame
from constant import *

class Hand:
    def __init__(self):
        self.original_image = pygame.image.load("Assets/Hand/hand1.png").convert_alpha() #Opened hand. Using 'self.original_image', allowing original image to be used as a base for creating new scaled images
        self.original_image = pygame.transform.smoothscale(self.original_image, (HAND_SIZE, HAND_SIZE)) #Scales the image to size specified by the HAND_SIZE
        self.image = self.original_image.copy() #Creates a copy of the image
        self.smaller_image = pygame.image.load("Assets/Hand/hand2.png").convert_alpha() #Closed hand
        self.smaller_image = pygame.transform.smoothscale(self.smaller_image, (HAND_SIZE - 60, HAND_SIZE - 60))
        self.rect = pygame.Rect(0, 0, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1]) #To determine whether hand is colliding with any other objects in the game

    # Draw a visual representation of the hand's collision box (hitbox)
    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect) #Draw rect on the surface using orange color with self.rect as its size and position
    
    def draw(self, surface):
        # Draw the image using the self.rect as its position
        surface.blit(self.image, self.rect)
        if DRAW_HITBOX:
            self.draw_hitbox(surface)

    def on_object(self, objects): 
        # Return a list with all objects that are colliding with the hand's hitbox
        return [object for object in objects if self.rect.colliderect(object.rect)]

    def catch_objects(self, objects, score, sounds): 
        if self.left_click: 
            # Get a list of objects that are colliding with the hand
            caught_objects = self.on_object(objects)
            # If colliding
            if caught_objects:
                sounds["grab"].play()
                for object in caught_objects:
                    object_score = object.catch(objects)
                    score += object_score
                    # If the object's score is negative
                    if object_score < 0:
                        sounds["explosion"].play()
        else:
            self.left_click = False
        # Return the updated score
        return score


