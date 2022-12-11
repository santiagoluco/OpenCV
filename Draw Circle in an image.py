import cv2
import numpy as np

# Create a function based on a CV2 Event (Right button click)
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),5)

# Open the image
img = cv2.imread("dog_backpack.jpg")

# This names the window so we can reference it 
cv2.namedWindow(winname='my_dog')

# Connects the mouse button to our callback function
cv2.setMouseCallback('my_dog',draw_circle)

while True: #Runs forever until we break with Esc key on keyboard
    # Shows the image window
    cv2.imshow('my_dog',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()