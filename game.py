import pygame
import time
import random
from constant import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
from penguin import Penguin
from bomb import Bomb
import cv2
import ui

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.capture = cv2.VideoCapture(0) # Load camera using the default camera (0)
        self.sounds = {}
        self.sounds["grab"] = pygame.mixer.Sound(f"Assets/Sounds/grab.mp3")
        self.sounds["grab"].set_volume(SOUNDS_VOLUME)
        self.sounds["explosion"] = pygame.mixer.Sound(f"Assets/Sounds/explosion.wav")
        self.sounds["explosion"].set_volume(SOUNDS_VOLUME-0.6)
        self.sounds["click"] = pygame.mixer.Sound(f"Assets/Sounds/click.mp3")
        self.sounds["click"].set_volume(SOUNDS_VOLUME)

    # Reset all the needed variables when a new game starts
    def reset(self): 
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.objects = []
        self.objects_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()

    def spawn_objects(self):
        t = time.time() #Gets the current time in seconds
        if t > self.objects_spawn_timer:
            self.objects_spawn_timer = t + PENGUIN_SPAWN_TIME #A new penguin will be spawned every 1 second

            # Increase the probability that the object will be a bomb over time
            # nb = number of bombs
            nb = (GAME_DURATION-self.time_left)/GAME_DURATION * 100 / 2  #Increase from 0 to 50 during all the game (linear)

            # Add randomness and unpredictability to the game
            if random.randint(0, 100) < nb:
                self.objects.append(Bomb())
            else:
                self.objects.append(Penguin())

            # Spawn additional bomb and penguin after the half of the game to increase difficulty
            if self.time_left < GAME_DURATION/2:
                self.objects.append(Bomb())

            if self.time_left < GAME_DURATION/2:
                self.objects.append(Penguin())

    # Keep track of the remaining time in the game 
    def update_game_time(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0) #The result is 1 decimal place, with the maximum value between the result and 0 

    # Capture single frame from the camera
    def load_camera(self):
        _, self.frame = self.capture.read() #method to read the next frame from the camera
        # '_' used to unpack tuple returned by the method, containing boolean whether frame was read successfully
        # frame assigned to the self.frame

    # Track player's hand in real-time
    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame) #Scanning the hands in the frame
        (x, y) = self.hand_tracking.get_hand_position() 
        self.hand.rect.center = (x, y) #Sets the hand object position on the screen to match the position of the hand in the webcam frame
                                        # thus hand object positioned on the screen at the same location as hand in the webcam frame

    # Drawing elements of the game on the screen
    def draw(self):
        self.background.draw(self.surface) #Draw the background
        for object in self.objects: #Draw the objects
            object.draw(self.surface)
        self.hand.draw(self.surface) #Draw the hand
        ui.draw_text(self.surface, f"Score : {self.score}", (5, 5), COLORS["score"], font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255)) #Draw the score
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"] #Change the text color remaining time less than 5s
        ui.draw_text(self.surface, f"Time left : {self.time_left}", (SCREEN_WIDTH//2, 5),  timer_text_color, font=FONTS["medium"],
                    shadow=True, shadow_color=(255,255,255)) #Draw the remaining time

    # Update the game's state
    def update(self):
        self.load_camera() 
        self.set_hand_position() 
        self.update_game_time()
        self.draw()

        if self.time_left > 0:
            self.spawn_objects()
            (x, y) = self.hand_tracking.get_hand_position()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.hand_closed #Sets the mouse left click to hand closing
            # print("Hand closed", self.hand.left_click)
            if self.hand.left_click: #If hand is closed
                self.hand.image = self.hand.smaller_image.copy() #Use the hand closed image that has been scaled smaller
            else: 
                self.hand.image = self.hand.original_image.copy() #Use the hand opened image
            self.score = self.hand.catch_objects(self.objects, self.score, self.sounds)
            for object in self.objects:
                object.move() #Updates its position on the screen

        else: # When the game is over
            if ui.button(self.surface, 400, "BACK", click_sound=self.sounds["click"]):
                return "menu"

        cv2.imshow("Frame", self.frame) #Shows webcam frame on the screen
        cv2.waitKey(1) #Waits for 1ms before the next frame to create illusion of a live video stream


