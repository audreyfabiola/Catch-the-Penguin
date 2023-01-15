import pygame
# Constants 

# Window
WINDOW_NAME = "Catch the Penguin"
GAME_TITLE = WINDOW_NAME
SCREEN_WIDTH, SCREEN_HEIGHT = 1100, 600

# FPS
FPS = 90
DRAW_FPS = True

# Animation
ANIMATION_SPEED = 0.08 # The frame of the objects will change every 0.08 seconds

# Penguin
PENGUIN_SIZE = (60, 60)
PENGUIN_SIZE_RANDOMIZE = (1.2, 2) # For each new penguin, it will multiply the size with an random value between 1.2 and 2
PENGUIN_MOVE_SPEED = {"min": 2, "max": 5}
PENGUIN_SPAWN_TIME = 1

# Collision Box
DRAW_HITBOX = False 

# Bomb
BOMB_SIZE = (100, 80)
BOMB_SIZE_RANDOMIZE = (1, 1.5)
BOMB_PENALITY = 1 # Will remove X of the score of the player (if capture a bomb)

# Hand 
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)

# Game 
GAME_DURATION = 60 #The game will last 60s

# UI
pygame.font.init() #Initializes the pygame font module so that we can use it to render text
FONTS = {}
FONTS["medium"] = pygame.font.Font("Assets/04B_30__.ttf", 35)
FONTS["big"] = pygame.font.Font("Assets/04B_30__.ttf", 68)

# Button Sizes
BUTTONS_SIZES = (240, 90)

# Colors
COLORS = {"title": (38, 61, 39), 
          "score": (38, 61, 39), 
          "timer": (38, 61, 39),
          "buttons": {"default": (6, 67, 200), "hover":  (87, 99, 255), "text": (255, 255, 255), "shadow": (46, 54, 163)}} 
          #Hover is the color when the mouse if hovering over the button

# Sounds
MUSIC_VOLUME = 0.16 
SOUNDS_VOLUME = 1
