# -*- coding: utf-8 -*-
# @Author: vivekpatel99
# @Date:   2018-10-06 15:43:12
# @Last Modified by:   vivekpatel99
# @Last Modified time: 2018-10-06 16:43:29

"""

ptr_frbuf, ptr_frbuf_2, ptr_frbuf_3, ptr_frbuf_4, ptr_vdma, ptr_vdma_2, ptr_vdma_3, ptr_vdma_4
"""
import os
import sys
import cv2

import numpy as np
# from tkinter import *
# import tkinter as tk

import pygame
from pygame.locals import *

from definition import define


# from gui import gui
from lib.display import display
# from lib._Time import timecount
from lib.vision.vision import Vision
# from lib._logger import logging
from gui import gui


""" constants declaration  """

SCREEN_SIZE = (1265, 1015) # width, height
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Frames per second
FPS = 60


""" env_setup """ ############################################################
def env_setup(fbpath="/dev/fb0"):

    # os.putenv("SDL_FBDEV", fbpath)
    os.environ["SDL_FBDEV"] = fbpath

    # set up audio driver to avoid alisa lib erros
    os.environ['SDL_AUDIODRIVER'] = "dsp"
    # os.environ['SDL_VIDEODRIVER'] = "svgalib"
  

""" cam_loop """ ############################################################

def cam_loop(screen, fps_clock, title):

    cam = cv2.VideoCapture(0)
    print("[INFO] cam object created...")
    screen.fill(WHITE)

    try:
        while True:
            ret, frame = cam.read()

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = pygame.surfarray.make_surface(frame)

            screen.blit(frame, (50, 100)) # x, y
            screen.blit(title, (200,25))
            # fps_clock.tick(FPS)
            pygame.display.flip()

            if cv2.waitKey(30) & 0xFF == ord("q"):
                break
    except Exception as error:
        print(error)
        pygame.quit()
        cv2.destroyAllWindows()
        # root.destroy()
        sys.exit(-1)

""" main """ ##########################################################################################################
def main():
    """
    """
    env_setup()

    fram_bfs, vdma_bfs = define.platform_init()


    try:
        pygame.init()
    except Exception as error:
        print(error)

    # title fonts
    fonts = pygame.font.SysFont("Comic Sans MS", 40)
    title = fonts.render('Closed Loop Object Tracking based on Image Recongnition', False, (0, 0, 255))
    print("[INFO] title set up done...")
    fps_clock = pygame.time.Clock()


    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)

    cam_loop(screen, fps_clock, title)


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








def _main():
    """
    """
    fram_bfs, vdma_bfs = define.platform_init()

    fps = 5
    white = (255,255,255)
    black = (0,0,0)




if __name__ == '__main__':

    main()

