#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:10:05 2020

@author: j-bd
"""


import argparse

import cv2
import numpy as np


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Simple thresholding",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 simple_thresholding.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def thresholding(image, blurred):
    '''Apply predefined threshold'''
    (th_v, th_im) = cv2.threshold(blurred, 80, 255, cv2.THRESH_BINARY)
    cv2.imshow("Threshold Binary", th_im)
    (th_v, th_im_inv) = cv2.threshold(blurred, 80, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("Threshold Binary Inverse", th_im_inv)

    cv2.imshow("Masked", cv2.bitwise_and(image, image, mask=th_im_inv))


def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"], 0)
    cv2.imshow("Original", image)

    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow("blurred", blurred)

    thresholding(image, blurred)


if __name__ == "__main__":
    main()
