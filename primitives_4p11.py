import sys
import os
import time
from dataclasses import dataclass




def intersectionFinder(rectNodes1, rectNodes2):
    if(rectNodes1.x > rectNodes2.x):
        rectLeft = rectNodes2
        rectRight = rectNodes1
    else:
        rectLeft = rectNodes1
        rectRight = rectNodes2

    XLeft = min(rectNodes1.x, rectNodes2.x)
    XRight = max(rectNodes1.x, rectNodes2.x)
    if(XLeft + rectLeft.W) <= (XRight)