# -*- coding: utf-8 -*-
# @Author: vivekpatel99
# @Date:   2018-10-06 15:43:12
# @Last Modified by:   vivekpatel99
# @Last Modified time: 2018-10-06 16:43:29

"""

ptr_frbuf, ptr_frbuf_2, ptr_frbuf_3, ptr_frbuf_4, ptr_vdma, ptr_vdma_2, ptr_vdma_3, ptr_vdma_4
"""
import sys
import cv2
import ctypes.util
import ctypes
import time
import def
# from PyQt5.QtWidgets import QApplication
#
# from lib._Time import timecount
# from lib.vision.vision import Vision
# from lib._logger import logging
# from gui import gui
import os
# script_dir = os.path.abspath(os.path.dirname(__file__))
# lib_path = os.path.join(script_dir, 'def.so')
#
# _lib_pform_init = ctypes.cdll.LoadLibrary(ctypes.util.find_library(lib_path))

def ctypes_plateform_Init():
    # _lib_pform_init.platform_Init.retype= POINTER(POINTER(c_uint))
    _lib_pform_init.platform_Init()

    # return  _lib_pform_init.platform_Init()
def main():
    """
    """
    # vid = Vision(cam_num=0)
    # vid.is_camera_connected()
    cap = cv2.VideoCapture(0)
    time.sleep(5)
    out = cv2.VideoWriter("out.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25, (640,480))
    while True:
        # ret, frame = vid.get_video()
        #vid.display('img', frame)
        ret, frame = cap.read()
        cv2.imwrite('frame_5.jpg', frame)
        out.write(frame)

        if cv2.waitKey(300) & 0xFF == ord("q"):
            break

    # vid.video_cleanUp()


if __name__ == '__main__':
    # print("{:#08x}".format(255))
    # main()

    # ctypes_plateform_Init()
    # app = QApplication(sys.argv)
    # a_winow = gui.Window()
    # sys.exit(app.exec_())