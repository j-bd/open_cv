#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:44:49 2020

@author: j-bd
"""

import argparse

import numpy as np
import imutils
import cv2


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Translation",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 translation.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def translate(image):
    '''Translate image in a predefined way'''
    mat = np.float32([[1, 0, 25], [0, 1, 50]])
    shifted = cv2.warpAffine(image, mat, (image.shape[1], image.shape[0]))
    cv2.imshow("Shifted Down and Right", shifted)

    mat = np.float32([[1, 0, -50], [0, 1, -90]])
    shifted = cv2.warpAffine(image, mat, (image.shape[1], image.shape[0]))
    cv2.imshow("Shifted Up and Left", shifted)

def main():
    '''Launch main steps'''
    args = arguments_parser()
    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    translate(image)


if __name__ == "__main__":
    main()
