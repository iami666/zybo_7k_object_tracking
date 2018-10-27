import os

import numpy as np
import cv2
import sys
from imutils.video import VideoStream
import imutils
import time

from definition import define

# minimum size (in pixel) for a region of image to be considered actual "motion"
MIN_AREA = 500
CAM_NUM = 0

""" Vision """  ##########################################################################


class Vision:
    def __init__(self, cam_num=0):

        print("[INFO] setting up the video capture ......")

        self.cam_num = cam_num
        self.cap = cv2.VideoCapture(cam_num)

    """ is_camera_connected """  #####################################

    def is_camera_connected(self):
        return self.cap.isOpened()

    """ get_video """  ###############################################

    def get_video(self):

        ret, frame = self.cap.read()

        try:  # check if it is really a frame
            self.frame = frame.copy()

        except:
            print("[ERROR] frame  is not captured")

        if not ret:  # check if there was no frame captured
            print("[ERROR] while capturing frame")

        return ret, frame

    """ frame_resize """  #############################################

    def resize_frame(self, frame, size=define.VID_FRAME_SIZE):

        resize_frame = cv2.resize(frame, size)

        return resize_frame

    """ display """  ##################################################

    def img_read(self, image_path, mode=1):

        if not os.path.isfile(image_path):
            print("[ERROR] image does not exist {}".format(image_path))
            sys.exit(-1)

        image = cv2.imshow(image_path, mode)

        return image

    """ display """  ##################################################

    def display(self, window, frame):
        cv2.imshow(window, frame)

    """ video_cleanUp """  #############################################

    def video_cleanUp(self):
        self.cap.release()
        cv2.destroyAllWindows()


""" frame_resize """  ##################################################################################################


def test():
    vid = Vision()
    vid.isCameraConnected()

    while True:
        ret, frame = vid.getVideo()
        vid.display('img', frame)

        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

    vid.videoCleanUp()


if __name__ == '__main__':
    test()
