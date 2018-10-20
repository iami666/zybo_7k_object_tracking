# Created by patelviv at 2018-10-18

import os
import sys
import cv2


import numpy as np
from random import *

from tkinter import *
import tkinter as tk

import pygame
from pygame.locals import *

from definition import define

# Frames per second
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 500
HEIGHT = 500
MARGIN = 60

RECT_SIZE = (10, 10)


# I have no idea how this works,but it
# embeds a pygame window in a Tkinter frame.
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


# Main game loopq
def game_loop(screen, fps_clock, root=None):
    cam = cv2.VideoCapture(0)

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

def test_loop():

    pygame.init()
    screen = pygame.display.set_mode((1265, 1015))
    screen.fill(WHITE)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done =True

        pygame.draw.rect(screen, (0,128,255), pygame.Rect(30,30,30,30))

        pygame.display.flip()


def main():
    fram_bfs, vdma_bfs = define.platform_init()
    fb3 = "/dev/fb0"
    # os.putenv("SDL_FBDEV", fb3)
    # set up audio driver to avoid alisa lib erros
    os.environ['SDL_AUDIODRIVER'] = "dsp"

    # os.environ['SDL_VIDEODRIVER'] = fb3
    os.environ["SDL_FBDEV"] = fb3

    pygame.init()
    # root = setup_tkinter()
    fps_clock = pygame.time.Clock()

    # WIDTH =  define.VERTICAL_LINES
    # HEIGHT = define.HORIZONTAL_PIXELS
    # screen = pygame.display.set_mode((1240, 1010))
    # size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

    # print("Framebuffer size set {} x {}".format(size[0],size[1]))

    screen = pygame.display.set_mode((1265, 1015), pygame.FULLSCREEN)


    # while True:
    # game_loop(screen, fps_clock)
    test_loop(screen, fram_bfs)

if __name__ == '__main__':
    # main()
    test_loop()
