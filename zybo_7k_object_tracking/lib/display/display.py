# Created by viv at 26.10.18


import os
import cv2

import numpy as np

from tkinter import *
import tkinter as tk

import pygame
from pygame.locals import *


import display_gui, colors
sys.path.append("../../")
from definition import define

from lib.display import colors




# Frames per second
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 500
HEIGHT = 500
MARGIN = 60

RECT_SIZE = (10, 10)
SMALL_BUTTON = (5, 5, 100, 50)
BIG_BUTTON = (5, 5, 200, 50)


PROJECT_TITLE = 'Closed Loop Object Tracking based on Image Recognition'
btn_done = None



def start_btn_action():

    print("start bnt click")


def stop_btn_action():
    global btn_done
    print("stop bnt click")
    btn_done = True

def forward_btn_action():

    print("forward bnt click")

def backward_btn_action():

    print("backward bnt click")

def face_recog_btn_action():

    print("face_recog bnt click")

def object_tracking_btn_action():

    print("object tracking bnt click")


def test_loop():
    global btn_done
    btn_done = False
    img_path = "1.jpg"
    if not os.path.isfile(img_path):
        print("[ERROR] image does not exist {}".format(img_path))
    img = cv2.imread(img_path, 1)
    size = (define.HORIZ_PIXELS_SMALL, define.VERT_LINES_SMALL)
    resize_frame = cv2.resize(img, size)
    frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)

    disply = display_gui.Menu()
    screen = disply.display_init()
    disply.display_color()

    # fonts = pygame.font.SysFont("Comic Sans MS", 40)
    # title = fonts.render('Closed Loop Object Tracking based on Image Recognition', False, (0, 0, 255))
    title = display_gui.Menu.Text(text=PROJECT_TITLE, font=display_gui.Font.Medium)
    img_title_str = "Panda"

    image_title = display_gui.Menu.Text(text=img_title_str, font=display_gui.Font.Medium)
    task_info = "Vivek, John Snow, khalisi"
    # info  = display_gui.Menu.Text(text=task_info, font=display_gui.Font.Small)
    # pygame.draw.rect(info, )
    start_btn = display_gui.Menu.Button(text="START", rect=SMALL_BUTTON)
    start_btn.Command = start_btn_action

    stop_btn = display_gui.Menu.Button(text="STOP", rect=SMALL_BUTTON)
    stop_btn.Command = stop_btn_action

    forward_btn = display_gui.Menu.Button(text=">>", rect=SMALL_BUTTON)
    forward_btn.Command = forward_btn_action

    backward_btn = display_gui.Menu.Button(text="<<", rect=SMALL_BUTTON)
    backward_btn.Command = backward_btn_action

    face_recog_btn = display_gui.Menu.Button(text="Face Recognition", rect=BIG_BUTTON)
    face_recog_btn.Command = face_recog_btn_action

    obj_tracking_btn = display_gui.Menu.Button(text="Object Tracking", rect=BIG_BUTTON)
    obj_tracking_btn.Command = object_tracking_btn_action

    # btn_start.Left = display_gui.SCREEN_HEIGHT/2 - btn_start.Left*2
    frame_center = (50 + define.HORIZ_PIXELS_SMALL)/2
    frame_end = 60 + define.HORIZ_PIXELS_SMALL

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # check for left mouse click
                    # handle button click events
                    for btn in display_gui.Menu.Button.All:
                        if btn.Rolling: # mouse is over button
                            if btn.Command() != None: # do button event
                                btn.Command()

                            btn.Rolling = False
                            break

            if btn_done:
                done = True
        # 144 is upper y value of the picture frame
        start_btn.Render(screen, pos=(60 + define.HORIZ_PIXELS_SMALL, 144))
        #  length of small button  + 10 pixel (50  + 10) = 60
        stop_btn.Render(screen, pos=(60 + define.HORIZ_PIXELS_SMALL , 144 + 60))
        # 574 is lower y value of frame
        forward_btn.Render(screen, pos=(60 + define.HORIZ_PIXELS_SMALL , 574))
        backward_btn.Render(screen, pos=(60 + define.HORIZ_PIXELS_SMALL , 574 - 60))

        face_recog_btn.Render(screen, pos=(280 + define.HORIZ_PIXELS_SMALL, 144))

        obj_tracking_btn.Render(screen, pos=(280 + define.HORIZ_PIXELS_SMALL, 144 + 60))

        screen.blit(frame, (50, 150))

        title.Render(to=screen, pos=display_gui.TITLE_POSTION)
        image_title.Render(to=screen, pos=(frame_center , 100))
        pygame.display.flip()
    else:
        print("done")

def main():
    fb3 = "/dev/fb0"
    os.putenv("SDL_FBDEV", fb3)
    # set up audio driver to avoid alisa lib erros
    os.environ['SDL_AUDIODRIVER'] = "dsp"

    # os.environ['SDL_VIDEODRIVER'] = fb3
    # os.environ["SDL_FBDEV"] = fb3
    define.platform_init()


    # pygame.init()
    # root = setup_tkinter()
    # fps_clock = pygame.time.Clock()

    # WIDTH =  define.VERTICAL_LINES
    # HEIGHT = define.HORIZONTAL_PIXELS
    # # screen = pygame.display.set_mode((1240, 1010))
    # size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    #
    # print("Framebuffer size set {} x {}".format(size[0],size[1]))
    #
    # screen = pygame.display.set_mode((1265, 1015), pygame.FULLSCREEN)
    # while True:
    #     screen.fill(BLACK)

    # game_loop(screen, fps_clock)
    test_loop()


if __name__ == '__main__':
    main()

