# import the necessary packages
from collections import deque
import numpy as np
import cv2
from imutils.video import VideoStream
import imutils
import time

DARK_GREEN=(29, 86, 6)
LIGHT_GREEN=(64, 255, 255)

class Camera(object):
    def __init__(self, targetColor=(DARK_GREEN, LIGHT_GREEN), minSize=20, render=True):
        self.targetColor = targetColor
        self.minSize = minSize
        self.render_enabled = render
        print("[INFO] Initializing camera...")
        self.stream = VideoStream(usePiCamera=True, resolution=(640, 480))
        time.sleep(2)
        print("[INFO] Camera initialized!")
    
    def start(self):
        self.stream = self.stream.start()

    def get_position(self):
        frame = self.stream.read()

        frame = imutils.resize(frame, width=600)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        
        darker, lighter = self.targetColor
        mask = cv2.inRange(hsv, darker, lighter)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        center = None

        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            position = cv2.minEnclosingCircle(c)
            ((x, y), radius) = position
            print("Coordinates: ", x, y, " Size: ", radius)
            if self.render_enabled:
                self.render_camera(frame, c, position)
            return ((x,y), radius), True
        else:
            if self.render_enabled:
                self.show_image(frame)
            return (((0.0,0.0), 0.0), False)


    def render_camera(self, frame, c, position):
        ((x, y), radius) = position
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > self.minSize:
            cv2.circle(frame, (int(x), int(y)), int(radius),
                    (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
        self.show_image(frame)

    def show_image(self, frame):
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

    def stop(self):
        self.stream.stop()

    def __del__(self):
        cv2.destroyAllWindows()
