#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:05:15 2020

@author: j-bd
"""

import argparse

import cv2


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Resizing",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 resize.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def flip(image):
    '''Realize different flipping'''
    flipped = cv2.flip(image, 1)
    cv2.imshow("Flipped Horizontally", flipped)

    flipped = cv2.flip(image, 0)
    cv2.imshow("Flipped Vertically", flipped)

    flipped = cv2.flip(image, -1)
    cv2.imshow("Flipped Horizontally & Vertically", flipped)
    cv2.waitKey()

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    flip(image)


if __name__ == "__main__":
    main()
