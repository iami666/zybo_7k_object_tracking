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
# from concurrent.futures import thread
import _thread
import cv2

import numpy as np
# from tkinter import *
# import tkinter as tk

import pygame
from pygame.locals import *

from definition import define
from tasks.face_recog import face_recog

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
FPS = 30


""" env_setup """ ############################################################
def env_setup(fbpath="/dev/fb0"):

    # os.putenv("SDL_FBDEV", fbpath)
    os.environ["SDL_FBDEV"] = fbpath

    # set up audio driver to avoid alisa lib erros
    os.environ['SDL_AUDIODRIVER'] = "dsp"
    # os.environ['SDL_VIDEODRIVER'] = "svgalib"
    # os.putenv['SDL_VIDEODRIVER'] = "fbcon"


""" cam_loop """ ##############################################################

def cam_loop(screen, fps_clock):

    print("[INFO] cam_loop starts...")

    # vid_window = "/dev/fb3"
    # env_setup(vid_window)

    vid = Vision()
    print("[INFO] cam object created...")
    # screen = pygame.display.set_mode((define.HORIZ_PIXELS_SMALL, define.VERT_LINES_SMALL))
    # screen.fill(WHITE)

    try:
        while vid.is_camera_connected():
            # screen.fill(WHITE)
            ret, frame = vid.get_video()
            resize_frame = cv2.resize(frame, (define.HORIZ_PIXELS_SMALL, define.VERT_LINES_SMALL))
            frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2RGB)


            frame = np.rot90(frame)
            frame = pygame.surfarray.make_surface(frame)

            # screen.blit(frame, (50, 100)) # x, y
            screen.blit(frame, (50, 50)) # x, y

            # fps_clock.tick(FPS)
            pygame.display.flip()

            if cv2.waitKey(FPS) & 0xFF == ord("q"):
                break

    except Exception as error:
        print(error)
        pygame.quit()
        vid.video_cleanUp()
        # root.destroy()
        sys.exit(-1)

    vid.video_cleanUp()

""" main_frame_loop """ ##############################################################

def main_window_loop(screen, title):

    env_setup(fbpath="/dev/fb0")

    print("[INFO] main_window_loop starts...")

    screen.fill(WHITE)

    screen.blit(title, (200, 25))

    pygame.display.flip()




""" main """ ###########################################################################################################
def main():
    """
    """
    env_setup()

    define.platform_init()


    try:
        pygame.init()
    except Exception as error:
        print(error)

    # title fonts
    fonts = pygame.font.SysFont("Comic Sans MS", 40)
    title = fonts.render('Closed Loop Object Tracking based on Image Recognition', False, (0, 0, 255))
    print("[INFO] title set up done...")

    fps_clock = pygame.time.Clock()

    # making mouse invisible
    pygame.mouse.set_visible(False)

    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)

    screen.fill(WHITE)

    # cam_loop(screen, fps_clock, title)
    face_recog.face_recog_pygm(screen, title)
    # try:
    #     # _thread.start_new_thread(cam_loop, (screen, fps_clock))
    # cam_loop(screen, fps_clock)
    # except Exception as error:
    #     print(error)

if __name__ == '__main__':

    main()

