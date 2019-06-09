import cv2
import time
import RPi.GPIO as GPIO

btn_pin = 15

GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
bordersize = 25


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        self.start = 0
        self.end = 0
        #start, end = 0, 0
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        
        if GPIO.input(btn_pin) == GPIO.HIGH:
            #print("stisnut")
            self.start = time.time()
        
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        self.end = time.time()
        diff = int(self.end-self.start)
        
        if self.end-self.start < 10 and diff % 2 == 0:
            image = cv2.copyMakeBorder(image, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize, borderType=cv2.BORDER_CONSTANT, value=(0,0,255))
        else:
            image = cv2.copyMakeBorder(image, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize, borderType=cv2.BORDER_CONSTANT, value=(255,255,255))
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
