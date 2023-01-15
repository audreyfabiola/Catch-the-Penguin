import pygame
from constant import *

def draw_text(surface, text, position, color, font=FONTS["medium"], position_mode="top_left",
                shadow=False, shadow_color=(0,0,0), shadow_offset=5):
    label = font.render(text, 0, color) #The 0 is ignored, as the size is used from the constant
    label_rect = label.get_rect() #To position the text
    # Set the position of the text on the surface
    if position_mode == "top_left":
        label_rect.x, label_rect.y = position
    elif position_mode == "center":
        label_rect.center = position
    # Make the shadow
    if shadow:  #Checks if shadow parameter is set to True
        label_shadow = font.render(text, 0, shadow_color)
        shadow_rect = label_rect.copy()
        shadow_rect.x -= shadow_offset
        surface.blit(label_shadow, shadow_rect)

    surface.blit(label, label_rect) # draw the text

def button(surface, position_y, text=None, click_sound=None):
    button_rect = pygame.Rect((SCREEN_WIDTH//2 - BUTTONS_SIZES[0]//2, position_y), BUTTONS_SIZES)

    # Check if the mouse cursor is currently hovering over the button or not
    on_button = False
    if button_rect.collidepoint(pygame.mouse.get_pos()): #If it is on the button, get the current mouse position
        color = COLORS["buttons"]["hover"] #Change the button color
        on_button = True
    else:
        color = COLORS["buttons"]["default"]

    # Draw the shadow rectangle
    pygame.draw.rect(surface, COLORS["buttons"]["shadow"], (button_rect.x - 8, button_rect.y - 8, button_rect.w, button_rect.h))
    
    # Draw the rectangle
    pygame.draw.rect(surface, color, button_rect) 

    # Draw the text
    if text is not None:
        draw_text(surface, text, button_rect.center, COLORS["buttons"]["text"], position_mode="center",
                    shadow=True, shadow_color=COLORS["buttons"]["shadow"])

    if on_button and pygame.mouse.get_pressed()[0]: # if the user press on the button using the left mouse button
        if click_sound is not None: # play the sound if needed
            click_sound.play()
        return True
