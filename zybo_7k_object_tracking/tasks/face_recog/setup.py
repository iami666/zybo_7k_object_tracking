# Created by viv at 19.11.18

"""
python setup.py build_ext --inplace
"""


from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('face_recog_cy.pyx'))