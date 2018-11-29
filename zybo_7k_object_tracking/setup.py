# Created by viv at 19.11.18

"""
python setup.py build_ext --inplace
"""

import sys
from distutils.core import setup
from Cython.Build import cythonize

setup(
	ext_modules=cythonize('/home/debian/zybo_project/zybo_7k_object_tracking/tasks/face_recog/face_recog_cy.pyx')
)
