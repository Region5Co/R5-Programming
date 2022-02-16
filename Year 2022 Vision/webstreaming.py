#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 19:20:42 2022

@author: user
"""

import numpy
import cv2
from imutils.video import WebcamVideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import time


# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
outputFrame = None
lock = threading.Lock()

# initialize a flask object
app = Flask(__name__)

# initialize the video stream and allow the camera sensor to
# warmup
# vs = VideoStream(usePiCamera=1).start()
vs = WebcamVideoStream(src=0).start()
time.sleep(2.0)
try:

    @app.route("/")
    def index():
        # return the rendered template
        return render_template("index.html")

    def generate():
        # loop over frames from the output stream
        while True:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            outputFrame = vs.read()
            if outputFrame is None:
                continue

            # encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

            # ensure the frame was successfully encoded
            if not flag:
                continue

            # yield the output frame in the byte format
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + bytearray(encodedImage) + b"\r\n"
            )

    @app.route("/video_feed")
    def video_feed():
        # return the response generated along with the specific media
        # type (mime type)
        return Response(
            generate(), mimetype="multipart/x-mixed-replace; boundary=frame"
        )

    if __name__ == "__main__":
        # construct the argument parser and parse command line arguments
        ap = argparse.ArgumentParser()
        ap.add_argument(
            "-i", "--ip", type=str, required=True, help="ip address of the device"
        )
        ap.add_argument(
            "-o",
            "--port",
            type=int,
            required=True,
            help="ephemeral port number of the server (1024 to 65535)",
        )
        ap.add_argument(
            "-f",
            "--frame-count",
            type=int,
            default=32,
            help="# of frames used to construct the background model",
        )
        args = vars(ap.parse_args())

        # start the flask app
        app.run(
            host=args["ip"],
            port=args["port"],
            debug=True,
            threaded=True,
            use_reloader=False,
        )
except ():
    pass
# release the video stream pointer
# cv.destroyAllWindows()
vs.stop()
vs.stream.release()
