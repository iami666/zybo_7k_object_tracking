# Created by viv at 14.10.18

"""

"""


import os
import sys
import time
import pygame

sys.path.append(os.path.dirname(__file__))
from colors import *

pygame.init()

# path = os.path.abspath(os.path.join("../../", "definition"))
#
# if not os.path.exists(path):
#     print("[ERROR] define module can not import, path does not exist")
# sys.path.append(path)
# import define

""" Font """###################################################################
class Font:
    Default = pygame.font.SysFont("Comic Sans MS", 20)
    Small = pygame.font.SysFont("Verdana", 15)
    Medium = pygame.font.SysFont("Verdana", 40)
    Large = pygame.font.SysFont("Verdana", 60)
    Scanner = pygame.font.SysFont("Verdana", 30)


""" constants declaration  """
SCREEN_WIDTH = 1265
SCREEN_HEIGHT = 1015
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)  # width, height
TITLE_POSTION = (200, 25)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


""" display """###################################################################
# class display:
#     """
#
#     """
#     def __init__(self):
#         "Initializes a new pygame screeen using the frambuffer"
#
#         # check which frame buffer drivers are availabel
#         # start with fbcon since dirtectfb hangs with composite output
#         fb3 = "/dev/fb1"
#         os.putenv("SDL_FBDEV", fb3)
#         os.environ["SDL_FBDEV"] = fb3
#         try:
#             pygame.display.init()
#         except Exception as error:
#             print(error)
#
#
#         size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
#
#         print("Framebuffer size set {} x {}".format(size[0],size[1]))
#
#         self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
#
#         # clean the screen to start
#         self.screen.fill((0 , 0, 0))
#
#         # initialise fron support
#         pygame.font.init()
#
#         # render the screen
#         pygame.display.update()
#
#     def __def__(self):
#         "Destructor to make sure pygame shutdown "
#
#
#     def test(self):
#         "fill the screen with red"
#         red = (255,255, 255)
#         self.screen.fill(red)
#
#         pygame.display.update()



""" MouseOver """###############################################################
def MouseOver(rect):
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > rect[0] and mouse_pos[0] < rect[0] + rect[2] and mouse_pos[1] > rect[1] and mouse_pos[1] < rect[
        1] + rect[3]:
        return True
    else:
        return False




""" display """######################################################################################
class Menu:

    def __init__(self):

        self.screen = None
        try:
            pygame.init()
            print("[INFO] pygame initialisation done ")
        except Exception as error:
            print(error)

    def display_init(self, size=SCREEN_SIZE, flags=pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF):
        print("[INFO] display initialisation done ")
        self.screen = pygame.display.set_mode(size, flags)

        return self.screen

    def display_color(self, color=WHITE):
        self.screen.fill(color)

    def render(self):
        pygame.display.update()

    """ Button """  #########################################################
    class Button:

        All = []

        def __init__(self, text, rect, bg=Color.Gray, fg=Color.White, bgr=Color.CornflowerBlue, font=Font.Default, tag=("menu", None)):
            self.Text = text
            self.Left = rect[0]
            self.Top = rect[1]
            self.Width = rect[2]
            self.Height = rect[3]
            self.Command = None
            self.Rolling = False
            self.Tag = tag

            # NORMAL BUTTON
            self.Normal = pygame.Surface((self.Width, self.Height), pygame.HWSURFACE | pygame.SRCALPHA)
            self.Normal.fill(bg)
            RText = font.render(text, True, fg)  # text, antialiasing, color
            txt_rect = RText.get_rect()
            self.Normal.blit(RText, (self.Width / 2 - txt_rect[2] / 2, self.Height / 2 - txt_rect[3] / 2))

            # HIGHLIGHTED BUTTON
            self.High = pygame.Surface((self.Width, self.Height), pygame.HWSURFACE | pygame.SRCALPHA)
            self.High.fill(bgr)
            self.High.blit(RText, (self.Width / 2 - txt_rect[2] / 2, self.Height / 2 - txt_rect[3] / 2))

            # SAVE BUTTON
            Menu.Button.All.append(self)

        """ Render """  ##################################
        def Render(self, to, pos=(0, 0)): # pos = x, y
            if MouseOver((self.Left + pos[0], self.Top + pos[1], self.Width, self.Height)):
                to.blit(self.High, (self.Left + pos[0], self.Top + pos[1]))
                self.Rolling = True
            else:
                to.blit(self.Normal, (self.Left + pos[0], self.Top + pos[1]))
                self.Rolling = False

    """ Text """  ###################################################################
    class Text:

        All = []

        def __init__(self, text, font=Font.Default, color= Color.Black, bg=None):
            self.Text = text
            self.LastText = text
            self.Font = font
            self.Color = color
            self.Left = 0
            self.Top = 0
            self.Bg = bg

            bitmap = font.render(text, True, color)
            self.Bitmap = pygame.Surface(bitmap.get_size(), pygame.SRCALPHA | pygame.HWSURFACE)
            if bg != None:
                self.Bitmap.fill(bg)
            self.Bitmap.blit(bitmap, (0, 0))

            self.Width = self.Bitmap.get_width()
            self.Height = self.Bitmap.get_height()

        """ Render """  ####################################
        def Render(self, to, pos=(0, 0)):
            if self.Text != self.LastText:
                # TEXT HAS BEEN CHANGED
                self.LastText = self.Text

                # RECREATE BITMAP (Dynamic Text Rendering)
                bitmap = self.Font.render(self.Text, True, self.Color)
                self.Bitmap = pygame.Surface(bitmap.get_size(), pygame.SRCALPHA | pygame.HWSURFACE)
                if self.Bg != None:
                    self.Bitmap.fill(self.Bg)
                self.Bitmap.blit(bitmap, (0, 0))

                self.Width = self.Bitmap.get_width()
                self.Height = self.Bitmap.get_height()

            to.blit(self.Bitmap, (self.Left + pos[0], self.Top + pos[1]))

    """ display """  ########################################################################
    class Image:

        def __init__(self, bitmap, pos=(0, 0)):
            self.Bitmap = bitmap
            self.Left = pos[0]
            self.Top = pos[1]
            self.Height = bitmap.get_height()
            self.Width = bitmap.get_width()

        def Render(self, to, pos=(0, 0)):
            to.blit(self.Bitmap, (self.Left + pos[0], self.Top + pos[1]))











""" main """############################################################################################################
def main():
    pass
    # scope = display()
    # scope.test()
    # time.sleep(10)




if __name__ == "__main__":
    main()

    # pass