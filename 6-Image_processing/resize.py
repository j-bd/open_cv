#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:30:40 2020

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

def resize(image):
    '''Resize input image'''
    # Ratio computation
    ratio = 150.0 / image.shape[1] # width

    new_dim = (150, int(image.shape[0] * ratio)) # (width, height)
    resized = cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized (Width)", resized)

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    resize(image)


if __name__ == "__main__":
    main()
