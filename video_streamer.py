from flask import Response, Flask, render_template, request
import threading
import argparse
import datetime
import imutils
from imutils.video import VideoStream
import time
import cv2

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
#outputFrame = None
#lock = threading.Lock()

# Initialize Flask object
app = Flask(__name__)

# initialize the video stream and allow the camera sensor to warmup
# vs = VideoStream(usePiCamera=1).start()

#vs = VideoStream(src=0).start()
#time.sleep(2.0)

@app.route("/")
def index():
    # returns the rendered template
    return render_template("index.html")

