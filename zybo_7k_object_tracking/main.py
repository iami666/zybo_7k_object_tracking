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
import pygame
from pygame.locals import *


""" modules """


from definition import define
from tasks.face_recog import face_recog
sys.path.append("/lib/display")
from lib.display import display_gui



# from lib._logger import logging


PROJECT_TITLE = 'Closed Loop Object Tracking based on Image Recognition'
""" constants declaration  """

SCREEN_SIZE = (1265, 1015) # width, height
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Frames per second
FPS = 30


TASK_INDEX = 0

""" env_setup """ ############################################################
def env_setup(fbpath="/dev/fb0"):

    # os.putenv("SDL_FBDEV", fbpath)
    os.environ["SDL_FBDEV"] = fbpath

    # set up audio driver to avoid alisa lib erros
    os.environ['SDL_AUDIODRIVER'] = "dsp"
    # os.environ['SDL_VIDEODRIVER'] = "svgalib"
    # os.putenv['SDL_VIDEODRIVER'] = "fbcon"



""" main """ ###########################################################################################################
def main_():
    """
    """
    global TASK_INDEX

    TASK_INDEX = 0

    env_setup()

    define.platform_init()


    try:
        pygame.init()
    except Exception as error:
        print(error)

    # title fonts
    fonts = pygame.font.SysFont("Comic Sans MS", 40)
    title = fonts.render(PROJECT_TITLE, False, (0, 0, 255))
    print("[INFO] title set up done...")

  
    # making mouse invisible
    pygame.mouse.set_visible(False)

    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)

    screen.fill(WHITE)

    while True:

        if TASK_INDEX is 0:
            # cam_test.main()
            pass
        if TASK_INDEX is 1:
            face_recog.face_recog_pygm(screen, FPS,  title)


""" main """  ###########################################################################################################


def main():
    """
    """
    global TASK_INDEX

    TASK_INDEX = 0

    env_setup()

    define.platform_init()

    disp = display_gui.Menu()
    disp.display_init()
    disp.screen()
    while True:
        disp.render()
    # title fonts
    # fonts = pygame.font.SysFont("Comic Sans MS", 40)
    # title = fonts.render('Closed Loop Object Tracking based on Image Recognition', False, (0, 0, 255))
    # print("[INFO] title set up done...")

if __name__ == '__main__':

    main()

