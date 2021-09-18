from flask import Flask, render_template, Response
import cv2
import threading
import numpy as np

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # use 0 for web camera
frame = None

def gen_frames():  # generate frame by frame from camera
# Capture frame-by-frame    
    global frame
    success, f = camera.read()  # read the camera frame
    if success:
        ret, buffer = cv2.imencode('.jpg', f)
        frame = buffer.tobytes()
    threading.Timer(0.03, gen_frames).start()

def feed_frame():
    while True:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(feed_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

if __name__ == '__main__':
    gen_frames()
    app.run(host='0.0.0.0', port=8848)