import cv2
import mediapipe as mp
from constant import *

# Source code: https://google.github.io/mediapipe/solutions/hands.html

# Import modules for drawing hand annotations and for hand tracking
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

class HandTracking:
    def __init__(self):
        self.hand_tracking = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=1) #To detect and track hand, with the maximum number of hand on camera is set to 1
        self.hand_x = 0
        self.hand_y = 0
        self.results = None
        self.hand_closed = False

    # Scans the frame for any hands and returns the frame with the hand position marked
    def scan_hands(self, image):
        # Flip the image horizontally for a later selfie-view display, and convert the BGR image to RGB
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # Resize the image
        image = cv2.resize(image, (350, 200))

        # To improve performance, optionally mark the image as not writeable to pass by reference
        image.flags.writeable = False
        # Process the image and track hands within the image
        self.results = self.hand_tracking.process(image)

        # Draw the hand annotations on the image
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) #Image is converted back to BGR so that it can be saved using OpenCv

        self.hand_closed = False

        if self.results.multi_hand_landmarks: #multi_hand_landmarks = collection of detected/tracked hands, each hand represented as a list of 21 hand landmarks
            for hand_landmarks in self.results.multi_hand_landmarks:
                x, y = hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y #9th landmark = MIDDLE_FINGER_MCP
                
                # Convert coordinates to screen coordinates
                self.hand_x = int(x * SCREEN_WIDTH)
                self.hand_y = int(y * SCREEN_HEIGHT)

                x1, y1 = hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y #12th landmark = MIDDLE_FINGER_TIP

                if y1 > y:  #If the 12th landmark is below than the 9th landmark
                    self.hand_closed = True  #the program will detect that the hand is closed
                else: 
                    self.hand_closed = False

                # Draw the hand landmarks and connections on the 'image' object
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        return image

    # Return the current position of the hand
    def get_hand_position(self):
        return (self.hand_x, self.hand_y)

    # Display the image with the hand annotations on the screen
    def display_hand(self):
        cv2.imshow("image", self.image)
        cv2.waitKey(1) #Waits for 1ms before the next frame to create illusion of a live video stream

