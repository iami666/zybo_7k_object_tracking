"""
# Created by viv at 22.10.18

This script will simply check that camera and pygame is working correctly or not by simply displying image of
camera into display
"""
import os
import sys
import cv2
import imutils
import numpy as np
# from tkinter import *
# import tkinter as tk

import pygame
from pygame.locals import *

import sys



sys.path.append("../")

## my modules ##
from definition import define
from tasks.face_recog import face_recog
from lib.vision.vision import Vision



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

def _cam_loop(screen, fps_clock, title):

    print("[INFO] cam_loop starts...")

    # vid_window = "/dev/fb3"
    # env_setup(vid_window)

    vid = Vision()
    print("[INFO] cam object created...")

    try:
        while vid.is_camera_connected():
            # screen.fill(WHITE)
            ret, frame = vid.get_video()
            resize_frame = cv2.resize(frame, (define.HORIZ_PIXELS_SMALL, define.VERT_LINES_SMALL))
            frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2RGB)


            front = cv2.FONT_HERSHEY_SIMPLEX
            name = "vivek"
            color = (255, 0, 0)
            # width of text
            stroke = 2

            cv2.putText(frame, name[::-1], (100, 100), front, 1.0, color, stroke)
            # cv2.putText(frame, name, (100, 100), front, 1.0, color, stroke, cv2.LINE_AA)
            frame = np.rot90(frame)
            frame = pygame.surfarray.make_surface(frame)

            screen.blit(title, (200, 25))
            screen.blit(frame, (50, 100)) # x, y

            # pygame.display.flip()
            pygame.display.update()

            if cv2.waitKey(FPS) & 0xFF == ord("q"):
                break

    except Exception as error:
        print(error)
        pygame.quit()
        vid.video_cleanUp()
        sys.exit(-1)

    vid.video_cleanUp()



""" cam_loop """ ##############################################################

def cam_loop(screen, fps_clock, title):

    print("[INFO] cam_loop starts...")

    # vid_window = "/dev/fb3"
    # env_setup(vid_window)

    vid = imutils.video.VideoStream(src=0).start()
    print("[INFO] cam object created...")

    try:
        while True:
            # screen.fill(WHITE)
            frame = vid.read()
            resize_frame =imutils.resize(frame, (define.HORIZ_PIXELS_SMALL))
            frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2GRAY)


            front = cv2.FONT_HERSHEY_SIMPLEX
            name = "vivek"
            color = (255, 0, 0)
            # width of text
            stroke = 2

            cv2.putText(frame, name[::-1], (100, 100), front, 1.0, color, stroke)
            # cv2.putText(frame, name, (100, 100), front, 1.0, color, stroke, cv2.LINE_AA)
            frame = np.rot90(frame)
            frame = pygame.surfarray.make_surface(frame)

            screen.blit(title, (200, 25))
            screen.blit(frame, (50, 100)) # x, y

            pygame.display.flip()
            # pygame.display.update()

            if cv2.waitKey(FPS) & 0xFF == ord("q"):
                break

    except Exception as error:
        print(error)
        pygame.quit()
        cv2.destroyAllWindows()
        vid.stop()
        raise

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vid.stop()


# Main game loop
def game_loop(screen, fps_clock, root=None):
    cam = imutils.video.VideoStream(src=0)

    # cam.set(cv2.CAP_PROP_MODE, cv2.CAP_MODE_YUYV)
    # pygame.display.set_caption("opencv cam")
    # screen = pygame.display.set_mode([WIDTH - MARGIN, HEIGHT - MARGIN])
    screen.fill(WHITE)
    try:
        while True:
            frame = cam.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = pygame.surfarray.make_surface(frame)
            screen.blit(frame, (50, 50))
            # root.update()
            # pygame.display.update()
            fps_clock.tick(FPS)
            # checkVar2.set(2)
            # for event in pygame.event.get():
            #     if event.type == KEYDOWN:
            #         sys.exit(0)
            pygame.display.flip()

            key = cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
    except Exception as error:
        print(error)
        pygame.quit()
        cv2.destroyAllWindows()
        # root.destroy()
        sys.exit(-1)

    # do a bit of cleanup
    cv2.destroyAllWindows()
    cam.stop()




""" main """ ###########################################################################################################
def main():
    """
    """
    # env_setup()

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

    cam_loop(screen, fps_clock, title)



if __name__ == '__main__':

    main()

