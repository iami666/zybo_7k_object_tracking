# -*- coding: utf-8 -*-
# @Author: vivekpatel99
# @Date:   2018-10-06 15:43:12
# @Last Modified by:   vivekpatel99
# @Last Modified time: 2018-10-06 16:43:29

"""

ptr_frbuf, ptr_frbuf_2, ptr_frbuf_3, ptr_frbuf_4, ptr_vdma, ptr_vdma_2, ptr_vdma_3, ptr_vdma_4
"""
import base64
import sys
import cv2
import time
import  os
import pygame
import numpy as np
from random import *

from PyQt5.QtWidgets import QApplication



from definition import define
# from gui import gui
from lib.display import display
# from lib._Time import timecount
from lib.vision.vision import Vision
# from lib._logger import logging
from gui import gui


def main():
    """
    """
    fram_bfs, vdma_bfs = define.platform_init()
    # print(vdma_bfs)
    # display.main()
    fb3 = "/dev/fb1"
    os.putenv("SDL_FBDEV", fb3)
    os.environ["SDL_FBDEV"] = fb3
    try:
        pygame.display.init()
    except Exception as error:
        print(error)

    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

    print("Framebuffer size set {} x {}".format(size[0],size[1]))

    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    gui.main()
    pygame.display.update()

    # vid = Vision()
    #
    # # cap = cv2.VideoCapture(0)
    # # time.sleep(5)
    #
    # while vid.is_camera_connected():
    #
    #     ret, frame = vid.get_video()
    #     vid.display('img', frame)
    #
    #     resized_frame = cv2.resize(frame, (define.HORIZ_PIXELS_SMALL, define.VERT_LINES_SMALL))
    #
    #     fram_bfs.fd_frbuf_3.write(bytes(000000))
    #
    #     if cv2.waitKey(300) & 0xFF == ord("q"):
    #         break
    #
    #
    # vid.video_cleanUp()

def img_disply():
    fram_bfs, vdma_bfs = define.platform_init()
    # print(vdma_bfs)
    # display.main()
    fb3 = "/dev/fb0"
    os.putenv("SDL_FBDEV", fb3)
    os.environ["SDL_FBDEV"] = fb3
    try:
        pygame.display.init()
    except Exception as error:
        print(error)

    w = 640
    h = 480
    size = (w, h)

    screen = pygame.display.set_mode(size)
    img_name = "1.jpg"
    print(img_name)
    img = pygame.image.load(img_name)
    screen.blit(img, (0,0))
    pygame.display.flip()
    time.sleep(10)







def _main():
    """
    """
    fram_bfs, vdma_bfs = define.platform_init()

    fps = 5
    white = (255,255,255)
    black = (0,0,0)

    width =


if __name__ == '__main__':
    img_disply()
    # main()

    # app = QApplication(sys.argv)
    # a_winow = gui.Window()
    # sys.exit(app.exec_())