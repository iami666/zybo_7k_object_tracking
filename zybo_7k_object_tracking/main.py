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

    face_recog.face_recog_pygm(screen, FPS,  title)

if __name__ == '__main__':

    main()

