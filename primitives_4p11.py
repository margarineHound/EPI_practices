import sys
import os
import time
from dataclasses import dataclass
from collections import namedtuple

Rectangle = namedtuple('Rectangle', ('x', 'y', 'W', 'H'))




def intersectionFinder(rectNodes1, rectNodes2):
    if(rectNodes1.x > rectNodes2.x):
        rectLeft = rectNodes2
        rectRight = rectNodes1
    else:
        rectLeft = rectNodes1
        rectRight = rectNodes2

    if (rectNodes1.y > rectNodes2.y):
        rectLow = rectNodes2
        rectHigh = rectNodes1
    else:
        rectLow = rectNodes1
        rectHigh = rectNodes2

    XLeft = min(rectNodes1.x, rectNodes2.x)
    XRight = max(rectNodes1.x, rectNodes2.x)
    if(((XLeft + rectLeft.W) <= XRight) or ((XRight + rectRight.W) <= XLeft)):
        print("No intersection")
        return False
    else:

        intX = (XRight)
        intW = (XLeft + rectRight.W) - intX
        intY = rectLow.y
        intH = (intY + rectLow.H) - rectHigh.y
        print(f"Intersection: x:{intX}, y:{intY}, W:{intW}, H:{intH}")

    return(intX, intW, intY, intH)