#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:17:29 2020

@author: j-bd
"""

import argparse

import cv2


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Adaptive thresholding",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 adaptive_thresholding.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def adaptive_thresh(blurred):
    '''Apply adaptive thresholding'''
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4
    )
    cv2.imshow("Mean Thresh", thresh)

    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15,
        3
    )
    cv2.imshow("Gaussian Thresh", thresh)

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"], 0)
    cv2.imshow("Original", image)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    adaptive_thresh(blurred)


if __name__ == "__main__":
    main()
