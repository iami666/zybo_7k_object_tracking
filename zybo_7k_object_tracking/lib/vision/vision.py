""" The vision script contains all the function regarding video capture form wabcam"""

import os
import numpy as np
import cv2
import sys
from imutils.video import VideoStream
import imutils
import time
import logging

from definition import define

log = logging.getLogger("main." + __name__)

# minimum size (in pixel) for a region of image to be considered actual "motion"
MIN_AREA = 500
CAM_NUM = 0


# ------------------------------------------------------------------------------
# """ Vision """
# ------------------------------------------------------------------------------
class Vision:
    """ Vision class capture image for video and process it """

    def __init__(self, cam_num=CAM_NUM):
        """ """

        log.info("setting up the video capture ......")
        # print("[INFO] setting up the video capture ......")

        self.cam_num = cam_num
        self.cap = cv2.VideoCapture(cam_num)

    # -----------------------------------------------
    """ is_camera_connected """

    def is_camera_connected(self):
        """ check camera is connected or not """

        return self.cap.isOpened()

    # -----------------------------------------------
    """ get_video """

    def get_video(self):
        """ capture video form cam object """

        ret, frame = self.cap.read()

        try:  # check if it is really a frame
            self.frame = frame.copy()

        except:
            print("[ERROR] frame  is not captured")

        if not ret:  # check if there was no frame captured
            print("[ERROR] while capturing frame")

        return ret, frame

    # -----------------------------------------------
    """ frame_resize """

    def resize_frame(self, frame, size=define.VID_FRAME_SIZE):
        """ resize the frame from given size parameter """

        resize_frame = cv2.resize(frame, size)

        return resize_frame

    # -----------------------------------------------
    """ img_read """

    def img_read(self, image_path, mode=1):
        """ reading image from image path """

        if not os.path.isfile(image_path):
            log.error("image does not exist {}".format(image_path))
            # print("[ERROR] image does not exist {}".format(image_path))
            sys.exit(-1)

        image = cv2.imshow(image_path, mode)

        return image

    # -----------------------------------------------
    """ display """

    def display(self, window, frame):
        """ display image on window """

        cv2.imshow(window, frame)

    # -----------------------------------------------
    """ video_cleanUp """

    def video_cleanUp(self):
        """ clean up video object and windows """

        self.cap.release()
        cv2.destroyAllWindows()


# ----------------------------------------------------------------------------------------------------------------------
# """ test  """
# ----------------------------------------------------------------------------------------------------------------------
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
