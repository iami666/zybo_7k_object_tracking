# -*- coding: utf-8 -*-
# @Author: vivekpatel99
# @Date:   2018-10-06 15:43:12
# @Last Modified by:   vivekpatel99
# @Last Modified time: 2018-10-06 16:43:29

"""

ptr_frbuf, ptr_frbuf_2, ptr_frbuf_3, ptr_frbuf_4, ptr_vdma, ptr_vdma_2, ptr_vdma_3, ptr_vdma_4
"""
import sys
import cv2
import ctypes.util
import ctypes
import time
from definition import define
import pygame

# from PyQt5.QtWidgets import QApplication
#
# from lib._Time import timecount
# from lib.vision.vision import Vision
# from lib._logger import logging
# from gui import gui
import  os

def main():
    """
    """
    fram_bfs, vdma_bfs = define.platform_init()

    # vid = Vision(cam_num=0)
    # vid.is_camera_connected()
    cap = cv2.VideoCapture(0)
    time.sleep(5)
    out = cv2.VideoWriter("out.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25, (640,480))
    os.putenv(fram_bfs.fd_frbuf_2)
    pygame.display.init()
    while True:
        # ret, frame = vid.get_video()
        #vid.display('img', frame)
        ret, frame = cap.read()



        if cv2.waitKey(300) & 0xFF == ord("q"):
            break

    # vid.video_cleanUp()


if __name__ == '__main__':

    main()

    # app = QApplication(sys.argv)
    # a_winow = gui.Window()
    # sys.exit(app.exec_())