#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:49:12 2019

@author: pi
"""
import RPi.GPIO as GPIO
import cv2
import time

start, end = 0, 0

while True:
    start = time.time()
    time.sleep(3)
    end = time.time()
    print("proslo je:")
    print(end-start)