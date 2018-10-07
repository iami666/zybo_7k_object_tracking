# -*- coding: utf-8 -*-
# @Author: vivekpatel99
# @Date:   2018-10-06 15:43:12
# @Last Modified by:   vivekpatel99
# @Last Modified time: 2018-10-06 16:43:29

"""
"""
import sys
import cv2
from PyQt5.QtWidgets import QApplication

from lib._Time import timecount
from lib.vision.vision import Vision
from lib._logger import logging
from gui import gui

def main():
    """
    """
    vid = Vision(cam_num=0)
    vid.is_camera_connected()

    while True:
        ret, frame = vid.get_video()
        vid.display('img', frame)

        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

    vid.video_cleanUp()


if __name__ == '__main__':
    print("{:#08x}".format(255))
    # main()
    # app = QApplication(sys.argv)
    # a_winow = gui.Window()
    # sys.exit(app.exec_())