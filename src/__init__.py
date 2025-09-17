"""
VarSelect - Selective Sobel Framework

An innovative selective Sobel framework that efficiently avoids superfluous 
convolutions within homogeneous image regions by capitalizing on pixel-wise variance.
"""

__version__ = "0.1.0"
__author__ = "ProfCDuqueTec"
__email__ = ""

from .varselect import VarSelect

__all__ = ["VarSelect"]