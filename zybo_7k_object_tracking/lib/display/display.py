# Created by viv at 14.10.18

"""

"""


import os
import sys
import pygame
import time

# path = os.path.abspath(os.path.join("../../", "definition"))
#
# if not os.path.exists(path):
#     print("[ERROR] define module can not import, path does not exist")
# sys.path.append(path)
# import define


class display:
    """

    """
    def __init__(self):
        "Initializes a new pygame screeen using the frambuffer"

        # check which frame buffer drivers are availabel
        # start with fbcon since dirtectfb hangs with composite output
        fb3 = "/dev/fb1"
        os.putenv("SDL_FBDEV", fb3)
        os.environ["SDL_FBDEV"] = fb3
        try:
            pygame.display.init()
        except Exception as error:
            print(error)


        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

        print("Framebuffer size set {} x {}".format(size[0],size[1]))

        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

        # clean the screen to start
        self.screen.fill((0 , 0, 0))

        # initialise fron support
        pygame.font.init()

        # render the screen
        pygame.display.update()

    def __def__(self):
        "Destructor to make sure pygame shutdown "


    def test(self):
        "fill the screen with red"
        red = (255,255, 255)
        self.screen.fill(red)

        pygame.display.update()





def main():
    scope = display()
    scope.test()
    time.sleep(10)




if __name__ == "__main__":
    main()

    # pass