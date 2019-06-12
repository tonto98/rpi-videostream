import RPi.GPIO as GPIO
import time

on_pin, off_pin = 17, 18
buzzer = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(off_pin, GPIO.OUT)
GPIO.setup(on_pin, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)

# otkljucaj na 5 sekundi
GPIO.output(off_pin, False)
for i in range(25):
    GPIO.output(on_pin, True)
    GPIO.output(buzzer, True)
    time.sleep(0.1)
    GPIO.output(on_pin, False)
    GPIO.output(buzzer, False)
    time.sleep(0.1)
    
GPIO.output(off_pin, True)
GPIO.output(on_pin, False)
