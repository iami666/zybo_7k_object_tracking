"""
# Created by viv at 22.10.18

This script will simply check that camera and pygame is working correctly or not by simply displying image of
camera into display
"""
import os
import sys
import cv2
import time
import numpy as np
# from tkinter import *
# import tkinter as tk

import pygame
import pygame.camera
from pygame.locals import *
from imutils.video import FPS
import sys



sys.path.append("../")

## my modules ##
from definition import define
#from tasks.face_recog import face_recog
from lib.vision.vision import Vision
#from lib._Time.timecount import Time


""" constants declaration  """
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)  # width, height

#SCREEN_SIZE = (1265, 1015) # width, height
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# # Frames per second
# FPS = 30


""" env_setup """ ############################################################
def env_setup(fbpath='/dev/fb1'):


    #os.environ["svgalic"] = fbpath

    # set up audio driver to avoid alisa lib erros
    #os.environ['SDL_AUDIODRIVER'] = "dsp"
    os.putenv('SDL_VIDEODRIVER', "fbcon")
    os.putenv('SDL_FBDEV', fbpath)
    os.environ['SDL_FBDEV'] = fbpath
    # os.putenv('SDL_FBDEV', fbpath)
    print("#########################")
    print(os.getenv("SDL_FBDEV"))

""" cam_loop """ ##############################################################

def cam_loop_pygm(screen, fps_clock):

    print("[INFO] cam_loop starts...")

    cam = pygame.camera.Camera("/dev/video0", (define.HORIZ_PIXELS_SMALL, define.VERT_LINES_SMALL), "RBG")

    print("[INFO] cam object created...")

    fps = FPS().start()
    t = time.time()
    cam.start()

    while True:
        # frame = cam.get_image(screen)
        frame = cam.get_image()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        screen.blit(frame, (0, 0)) # x, y

        pygame.display.update()

        # update the FPS  Counter
        fps.update()
        # fps_clock.tick(30)
        t2 = time.time()
        if int(t2-t) > 60:
            break

    # stop the time and display FPS Information
    fps.stop()
    cam.stop()
    pygame.quit()
    # log.info("Elapsed Time: {: 2f}".format(fps.elapsed()))
    print("Elapsed Time: {: 2f}".format(fps.elapsed()))
    print("Approx FPS: {: 2f}".format(fps.fps()))




""" cam_loop """ ##############################################################

def cam_loop(screen, fps_clock, title):

    print("[INFO] cam_loop starts...")

    # vid_window = "/dev/fb3"
    # env_setup(vid_window)

    vid = Vision()
    print("[INFO] cam object created...")
    fps = FPS().start()
    t = time.time()
    # try:
    while vid.is_camera_connected():
        # screen.fill(WHITE)
        ret, frame = vid.get_video()
        frame = cv2.resize(frame, (define.HORIZ_PIXELS_SMALL, define.VERT_LINES_SMALL))
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


        # front = cv2.FONT_HERSHEY_SIMPLEX
        # name = "vivek"
        # color = (255, 0, 0)
        # # width of text
        # stroke = 2
        #
        # cv2.putText(frame, name[::-1], (100, 100), front, 1.0, color, stroke)
        # cv2.putText(frame, name, (100, 100), front, 1.0, color, stroke, cv2.LINE_AA)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)

        # screen.blit(title, (200, 25))
        # screen.blit(frame, (50, 100)) # x, y
        screen.blit(frame, (0, 0)) # x, y

        # pygame.display.flip()
        pygame.display.update()

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        # update the FPS  Counter
        fps.update()
        fps_clock.tick(30)
        t2 = time.time()
        if int(t2-t) > 60:
            break
    # except Exception as error:
    #     print(error)
    #     pygame.quit()
    #     vid.video_cleanUp()
    #     sys.exit(-1)

    # stop the time and display FPS Information
    fps.stop()
    # log.info("Elapsed Time: {: 2f}".format(fps.elapsed()))
    print("Elapsed Time: {: 2f}".format(fps.elapsed()))
    print("Approx FPS: {: 2f}".format(fps.fps()))

    vid.video_cleanUp()




""" main """ ###########################################################################################################
def main():
    """
    """

    define.platform_init()
    # env_setup()

    try:
        pygame.display.init()
        pygame.camera.init()
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
    screen.set_alpha(None) # do not need transparency
    # screen.fill(WHITE)

    cam_loop(screen, fps_clock, title)
    # cam_loop_pygm(screen, fps_clock)


if __name__ == '__main__':

    main()

