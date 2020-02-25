#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:10:39 2020

@author: j-bd
"""

import argparse

import cv2
import numpy as np


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Sobel and Laplacian",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 sobel_and_laplacian.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def laplacian(image):
    '''Apply Laplacian filter'''
    lap = cv2.Laplacian(image, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))
    cv2.imshow("Laplacian", lap)

def sobel(image):
    '''Apply Sobel filter'''
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1)

    sobel_x = np.uint8(np.absolute(sobel_x))
    sobel_y = np.uint8(np.absolute(sobel_y))

    sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)

    cv2.imshow("Sobel X", sobel_x)
    cv2.imshow("Sobel Y", sobel_y)
    cv2.imshow("Sobel Combined", sobel_combined)

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"], 0)
    cv2.imshow("Original", image)

    laplacian(image)


if __name__ == "__main__":
    main()
