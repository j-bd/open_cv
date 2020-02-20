#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:54:22 2020

@author: j-bd
"""

import argparse

import cv2
import numpy as np


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Rotation",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 rotation.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def rotate(image):
    '''Proceed rotation'''
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    mat = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(image, mat, (w, h))
    cv2.imshow("Rotated by 45 Degrees", rotated)

    mat = cv2.getRotationMatrix2D(center, -90, 2.0)
    rotated = cv2.warpAffine(image, mat, (w, h))
    cv2.imshow("Rotated by -90 Degrees", rotated)

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    image = rotate(image)


if __name__ == "__main__":
    main()
