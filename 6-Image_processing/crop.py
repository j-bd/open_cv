#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:34:32 2020

@author: j-bd
"""

import argparse

import cv2


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Cropping",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 crop.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def crop(image):
    '''Crop image with a standard position'''
    cv2.rectangle(image, (240, 30), (335, 120), (255, 0, 0))
    cv2.imshow("Zone", image)
    cropped = image[30:120, 240:335]
    cv2.imshow("Selection", cropped)

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    crop(image)


if __name__ == "__main__":
    main()
