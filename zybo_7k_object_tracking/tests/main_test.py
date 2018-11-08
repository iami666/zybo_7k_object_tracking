# Created by patelviv at 2018-10-18

import os
import cv2
import imutils
import numpy as np

from tkinter import *
import tkinter as tk

import pygame
from pygame.locals import *


sys.path.append("../")
from definition import define
from lib.display import display_gui, colors
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



def setup_tkinter():
    root = tk.Tk()

    embed = tk.Frame(
        root, width=WIDTH + MARGIN + 150,
        height=HEIGHT + MARGIN + 150)
    embed.grid(
        columnspan=WIDTH + MARGIN + 150,
        rowspan=HEIGHT + MARGIN + 150)

    # embed.pack()
    global checkVar2
    checkVar1 = IntVar()
    checkVar2 = IntVar()

    c1 = Radiobutton(root, text="Music", variable=checkVar1, value=1)
    c2 = Radiobutton(root, text="video", variable=checkVar2, value=2)
    c1.grid(row=50, column=600)
    c2.grid(row=60, column=600)

    # os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
    # The following line should be commented out on Linux
    # os.environ['SDL_VIDEODRIVER'] = 'windib'

    # os.environ["SDL_FBDEV"] = fb3
    return root


# Main game loop
def game_loop(screen, fps_clock, root=None):
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_MODE, cv2.CAP_MODE_YUYV)
    # pygame.display.set_caption("opencv cam")
    # screen = pygame.display.set_mode([WIDTH - MARGIN, HEIGHT - MARGIN])
    screen.fill(WHITE)
    try:
        while True:
            ret, frame = cam.read()
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
    except Exception as error:
        print(error)
        pygame.quit()
        cv2.destroyAllWindows()
        # root.destroy()
        sys.exit(-1)

    # random_pos = (
    #     randint(MARGIN, WIDTH - MARGIN),
    #     randint(MARGIN, HEIGHT - MARGIN))
    #
    # rect = Rect(random_pos, RECT_SIZE)
    # pygame.draw.rect(screen, BLACK, rect)
    #
    # pygame.display.update()
    # root.update()
    # fps_clock.tick(FPS)
    #
    # for event in pygame.event.get():
    #     if event.type == QUIT:
    #         pygame.quit()
    #         root.destroy()
    #         sys.exit()


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
    img = cv2.imread(img_path, 0)
    size = (define.HORIZ_PIXELS_SMALL, define.VERT_LINES_SMALL)
    # resize_frame = cv2.resize(img, size)
    frame = cv2.resize(img, size)
    # frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2RGB)
    # frame = np.mean(frame, -1) # gray conversion
    # frame = np.dot(frame[..., :3], [0.299, 0.587, 0.114])
    # frame = cv2.cvtColor(resize_frame, cv2.COLOR_HSV2RGB)
    # frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.flip(frame, 1) # flip image vertically
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame[..., ::-1, :]) # flip image vertically (optimized)

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

        title.Render(to=screen, pos=display_gui.TITLE_POSITION)
        image_title.Render(to=screen, pos=(frame_center , 100))
        pygame.display.flip()
    else:
        print("done")


def main():

    import time

    fb3 = "/dev/fb3"
    print(fb3)
    define.platform_init()
    # os.putenv("SDL_FBDEV", fb3)

    # set up audio driver to avoid alisa lib errors
    # os.environ['SDL_AUDIODRIVER'] = "dsp"

    # pygame.init()
    # # # root = setup_tkinter()
    fps_clock = pygame.time.Clock()
    # # #
    #
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    # # size = (define.HORIZ_PIXELS_SMALL, define.VERT_LINES_SMALL)
    #
    # # print("Framebuffer size set {} x {}".format(size[0],size[1]))
    # #
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
    #
    # #     pygame.display.flip()
    game_loop(screen, fps_clock)
    # test_loop()


if __name__ == '__main__':
    main()

