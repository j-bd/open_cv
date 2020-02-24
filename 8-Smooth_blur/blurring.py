#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:58:54 2020

@author: j-bd
"""

import argparse

import cv2
import numpy as np
from matplotlib import pyplot as plt


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

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    averaging_blur(image)


if __name__ == "__main__":
    main()

