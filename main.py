from flask import Flask, render_template, Response
from camera import VideoCamera

import subprocess

import RPi.GPIO as GPIO

off_pin = 18
btn_pin = 15

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(off_pin, GPIO.OUT)
GPIO.output(off_pin, True)

app = Flask(__name__)

@app.route('/')
def index():
    print("index")
    return render_template('index.html')

def gen(camera):
    print("gen")
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    print("video_feed")
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/open', methods=["POST"])
def open():
    subprocess.Popen(["python", "lock.py"])
    return index()  

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

