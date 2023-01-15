import pygame
from constant import *
from background import Background
import ui
import sys

class Menu:
    def __init__(self, surface):
        self.surface = surface
        # Create a background object as an attribute
        self.background = Background()
        # Create a Pygame sound object as an attribute
        self.click_sound = pygame.mixer.Sound(f"Assets/Sounds/click.mp3")
    
    def draw(self):
        self.background.draw(self.surface)
        # Draw the game title
        ui.draw_text(self.surface, GAME_TITLE, (SCREEN_WIDTH//2, 180), COLORS["title"], font=FONTS["big"],
                    shadow=True, shadow_color=(255,255,255), position_mode="center")

    def update(self):
        # Draw the menu to the screen
        self.draw()
        # If the 'Start' button was clicked
        if ui.button(self.surface, 320, "START", click_sound=self.click_sound):
            return "game"

        # If the 'Quit' button was clicked
        if ui.button(self.surface, 455, "QUIT", click_sound=self.click_sound):
            # Close the Pygame window and exit the program
            pygame.quit()
            sys.exit()