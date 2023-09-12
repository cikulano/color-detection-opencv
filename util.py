import numpy as np
import cv2

def get_limits(color):
    # Convert the color from BGR to HSV color space
    hsv_color = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)
    
    # Extract the hue value from the HSV color
    hue = hsv_color[0][0][0]
    
    # Calculate the lower and upper limits for the hue value
    lower_limit = np.array([hue - 10, 100, 100])
    upper_limit = np.array([hue + 10, 255, 255])

    return lower_limit, upper_limit
