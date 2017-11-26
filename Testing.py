import sys
import cv2
import numpy as np
from Log import Log

Points = []

def GetPoints(Event, X, Y, Flags, Parameter):
    global MouseX, MouseY
    global Points
    if Event == cv2.EVENT_LBUTTONDOWN:
        Points.append((X, Y))

cv2.namedWindow("Select the vertices of the target in order.")
cv2.setMouseCallback("Select the vertices of the target in order.", GetPoints)

File = "Test_Moon_1.png" # Change this as needed. Will be better in future...
print("Welcome to the VisionSystem object creator.\r\nPlease draw an outline around the object, by clicking on each verticy, in order. (Clockwise or counterclockwise.)\r\nPress enter to save the outline, press delete to remove the last point, and press escape to exit this program.\r\nIMPORTANT: Your image of the object must be taken in a \"neutral\" pose: with proper lighting, and at 0° rotation in all three planes; facing the camera.")
Log("Loading file \"" + File + "\"...")
Frame = cv2.imread("TestImages/" + File)

while True:
    NewFrame = Frame.copy()
    N = 0
    for Pair in Points:
        X, Y = Pair
        cv2.circle(NewFrame, (X, Y), 7, (0, 0, 0), -1)
        cv2.circle(NewFrame, (X, Y), 5, (0, 255, 0), -1)
        N += 1
    cv2.imshow("Select the vertices of the target in order.", NewFrame)
    k = cv2.waitKey(20) & 0xFF
    if k == 13: # Enter key.
        print("Are you sure this is the outline you want to use to create the object? Type \"Y\" to continue; type \"N\" to return to the outliner.")
        Input = input()
        if Input.upper() == "Y":
            Log("Saved outline!\r\n" + str(Points)) # Temp
            break
        else:
            print("Returning to outliner window.")
    if k == 27: # Escape Key.
        print("Bye!")
        sys.exit()
    if k == 8: # Delete Key.
        Points = Points[:-1]
cv2.destroyAllWindows()

print("One more thing... How far away, in inches, was the object in the image from the camera?")
Input = input()
print("Thanks! Distance was: " + str(Input) + " inches.")