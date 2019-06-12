import cv2
import time
import RPi.GPIO as GPIO

btn_pin = 15

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
bordersize = 25


class VideoCamera(object):
    def __init__(self):
        
        self.video = cv2.VideoCapture(0)
        self.start = 0
        self.end = 0
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        
        if GPIO.input(btn_pin) == GPIO.HIGH:
            self.start = time.time()
        
        success, image = self.video.read()
        
        self.end = time.time()
        diff = int(self.end-self.start)
        
        if self.end-self.start < 10 and diff % 2 == 0:
            image = cv2.copyMakeBorder(image, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize, borderType=cv2.BORDER_CONSTANT, value=(0,0,255))
        else:
            image = cv2.copyMakeBorder(image, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize, borderType=cv2.BORDER_CONSTANT, value=(255,255,255))
        
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
