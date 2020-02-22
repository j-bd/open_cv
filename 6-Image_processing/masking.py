#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:56:00 2020

@author: j-bd
"""

import argparse

import cv2
import numpy as np


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Masking",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 masking.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def masking(image):
    '''Apply predifined mask on the image'''
    mask = np.zeros(image.shape[:2], dtype="uint8")
    (cent_x, cent_y) = (image.shape[1] // 2, image.shape[0] // 2)
    cv2.rectangle(
        mask, (cent_x - 75, cent_y - 75), (cent_x + 75, cent_y + 75), 255, -1
    )
    cv2.imshow("Mask", mask)

    masked = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Mask Applied to Image", masked)

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    masking(image)


if __name__ == "__main__":
    main()
