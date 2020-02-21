#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:03:38 2020

@author: j-bd
"""

import argparse

import cv2
import numpy as np


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Arithmetic",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 arithmetic.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def arithmetic(image):
    '''Calculation process'''
    print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
    print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

    print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
    print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

    matrice = np.ones(image.shape, dtype="uint8") * 100
    cv2.imshow("100", matrice)
    added = cv2.add(image, matrice)
    cv2.imshow("Added", added)

    matrice = np.ones(image.shape, dtype="uint8") * 50
    subtracted = cv2.subtract(image, matrice)
    cv2.imshow("Subtracted", subtracted)
    cv2.waitKey()

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    arithmetic(image)


if __name__ == "__main__":
    main()
