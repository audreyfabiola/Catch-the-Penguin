import pygame
from constant import *
from game import Game
from menu import Menu
from penguin import *
import sys

# Initialize Pygame
pygame.init()

# Create Window/Display
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Control frame rate of the game
clock = pygame.time.Clock()

# Music
pygame.mixer.music.load("Assets/Sounds/Komiku_Glouglou.mp3") #Loads background music
pygame.mixer.music.set_volume(MUSIC_VOLUME)
pygame.mixer.music.play(-1) #Loop the music indefinitely

# Set initial state of the game to menu screen
state = "menu"

# State of the game, if it's on game or menu
game = Game(SCREEN)
menu = Menu(SCREEN)

# Handle user input events (pressing escape key on keyboard or closing the game window)
def user_events(): 
    for event in pygame.event.get(): #Get events
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: #If the pressed key is the escape key
                pygame.quit()
                sys.exit()

# Update the game state and display
def update():
    global state # The variable can be accessed and modified from anywhere within the program.
    if state == "menu":
        if menu.update() == "game":
            game.reset() # Reset all necessary variables to start a new game
            state = "game"
    elif state == "game":
        if game.update() == "menu":
            state = "menu"
    pygame.display.update()

    # Set FPS
    clock.tick(FPS)

# Main Loop
while True:
    user_events()
    update()

