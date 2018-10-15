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
import time
import  os
import pygame

from PyQt5.QtWidgets import QApplication



from definition import define
# from lib.display import display as dsp
# from lib._Time import timecount
# from lib.vision.vision import Vision
# from lib._logger import logging
from gui import gui



def main():
    """
    """
    fram_bfs, vdma_bfs = define.platform_init()

    # print(vdma_bfs)

    os.environ["SDL_FBDEV"] = fram_bfs.fd_frbuf_3







#     cap = cv2.VideoCapture(0)
#     # time.sleep(5)
#
#
#     while True:
#         # ret, frame = vid.get_video()
#         #vid.display('img', frame)
#         ret, frame = cap.read()
#         # HORIZ_PIXELS_SMALL = 640
#         # VERT_LINES_SMALL = 480
#         resized_frame = cv2.resize(frame,(define.HORIZ_PIXELS_SMALL, define.VERT_LINES_SMALL))
#
#         fram_bfs.fd_frbuf_3.write(str(frame))
#
#
#         if cv2.waitKey(300) & 0xFF == ord("q"):
#             break
#
# #     # vid.video_cleanUp()


if __name__ == '__main__':

    main()

    # app = QApplication(sys.argv)
    # a_winow = gui.Window()
    # sys.exit(app.exec_())