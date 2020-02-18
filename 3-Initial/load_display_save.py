#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:44:59 2020

@author: j-bd
"""

import argparse

import cv2


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Basic function",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 load_display_save.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def display(path):
    '''Display information about image'''
    image = cv2.imread(path)
    print(f"width: {image.shape[1]} pixels")
    print(f"height: {image.shape[0]} pixels")
    print(f"channels: {image.shape[2]}")
    cv2.imshow("Image", image)
    cv2.waitKey()
    return image

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = display(args["image"])

    cv2.imwrite("newimage.png", image)


if __name__ == "__main__":
    main()
