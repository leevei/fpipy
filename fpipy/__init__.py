# -*- coding: utf-8 -*-
# flake8: noqa

"""Top-level package for Fabry-Perot Imaging in Python."""

__author__ = """fpipy developers"""
__email__ = 'matti.a.eskelinen@student.jyu.fi'
__version__ = '0.1.0'

from . import simulate
from . import data
from . import  meta
from .io import read_hdt, read_ENVI_cfa
from .raw import raw_to_radiance, demosaic, subtract_dark
