#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:58:54 2020

@author: j-bd
"""

import argparse

import cv2
import numpy as np


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Histogram with mask",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 histogram_with_mask.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def averaging_blur(image):
    '''Compute blur image with predefined kernel'''
    blurred = np.hstack(
        [image, cv2.blur(image, (3, 3)), cv2.blur(image, (5, 5)),
         cv2.blur(image, (7, 7))]
    )
    cv2.imshow("Averaged", blurred)

def gaussian_blur(image):
    '''Compute blur image with predefined kernel'''
    blurred = np.hstack(
        [image, cv2.GaussianBlur(image, (3, 3), 0),
         cv2.GaussianBlur(image, (5, 5), 0), cv2.GaussianBlur(image, (7, 7), 0)]
    )
    cv2.imshow("Gaussian", blurred)

def median_blur(image):
    '''Compute blur image with predefined kernel'''
    blurred = np.hstack(
        [image, cv2.medianBlur(image, 3), cv2.medianBlur(image, 5),
         cv2.medianBlur(image, 7)]
    )
    cv2.imshow("Median", blurred)

def bilateral_blur(image):
    '''Compute blur image with predefined kernel'''
    blurred = np.hstack(
        [image, cv2.bilateralFilter(image, 5, 21, 21),
         cv2.bilateralFilter(image, 7, 31, 31),
         cv2.bilateralFilter(image, 9, 41, 41)]
    )
    cv2.imshow("Bilateral", blurred)


def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    averaging_blur(image)
    gaussian_blur(image)
    median_blur(image)


if __name__ == "__main__":
    main()
