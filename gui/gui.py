# -*- coding: utf-8 -*-
# @Author: vivekpatel99
# @Date:   2018-10-06 15:10:40
# @Last Modified by:   vivekpatel99
# @Last Modified time: 2018-10-06 19:39:14

"""
This module contains class and functions for the gui

"""

import sys
from PyQt5.QtWidgets import (QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

#from lib.vision.vision import Vision


class Window(QWidget):
    """docstring for window"""

    def __init__(self):
        # call parents class
        super(Window, self).__init__()
        self.init_ui()

    # initilize user interface
    def init_ui(self):
        """
        """
        # self.vd_frame = vd_frame
        self.start_btn = QPushButton('Start')
        self.stop_btn = QPushButton('Stop')

        # horizontal layout
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch(1)
        horizontal_layout.addWidget(self.start_btn)
        horizontal_layout.addWidget(self.stop_btn)

        # vertical_layout
        vertical_layout = QVBoxLayout(self)
        vertical_layout.addWidget(self.start_btn)
        vertical_layout.addWidget(self.stop_btn)


        # window place on the screen
        v_layout_move_sides = 800
        v_layout_move_updown = 200
        v_layout_width = 1500
        v_layout_height = 1800
        self.setGeometry(v_layout_move_sides,
                         v_layout_move_updown,
                         v_layout_width,
                         v_layout_height
                         )

        vertical_layout.addLayout(horizontal_layout)



        # layout.addStretch(1)
        self.setLayout(vertical_layout)
        self.setWindowTitle("Obect tracking with Zybo 7k")

        self.show()


def main():
    app = QApplication(sys.argv)
    a_winow = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
