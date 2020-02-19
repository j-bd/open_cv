#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:28:26 2020

@author: j-bd
"""

import numpy as np
import cv2


def image_init():
    '''Return a 300 pixels square RGB image'''
    return np.zeros((300, 300, 3), dtype = "uint8")

def lines(image):
    '''Draw predifined lines'''
    green = (0, 255, 0)
    cv2.line(image, (0, 0), (300, 300), green)
    cv2.imshow("Canvas", image)
    cv2.waitKey()

    red = (0, 0, 255) # BGR
    cv2.line(image, (300, 0), (0, 300), red, 3) # thickness
    cv2.imshow("Canvas", image)
    cv2.waitKey()
    return image

def rectangles(image):
    '''Draw predefined rectangles'''
    green = (0, 255, 0)
    cv2.rectangle(image, (10, 10), (60, 60), green)
    cv2.imshow("Canvas", image)
    cv2.waitKey()

    red = (0, 0, 255)
    cv2.rectangle(image, (50, 200), (200, 225), red, 5)
    cv2.imshow("Canvas", image)
    cv2.waitKey()

    blue = (255, 0, 0)
    cv2.rectangle(image, (200, 50), (225, 125), blue, -1)
    cv2.imshow("Canvas", image)
    cv2.waitKey()
    return image

def bullseye(image):
    '''Draw a predefined bullseye'''
    (centerX, centerY) = (image.shape[1] // 2, image.shape[0] // 2)
    white = (255, 255, 255)
    for radius in range(0, 200, 25):
        cv2.circle(image, (centerX, centerY), radius, white, 2)
    cv2.imshow("Canvas", image)
    cv2.waitKey()
    return image

def main():
    '''Launch main steps'''
    canvas = image_init()
    canvas = lines(canvas)
    canvas = rectangles(canvas)

    canvas = image_init()
    canvas = bullseye(canvas)


if __name__ == "__main__":
    main()
