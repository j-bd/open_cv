#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:50:10 2020

@author: j-bd
"""

import argparse

import cv2
import numpy as np


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Splitting and merging",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 splitting_and_merging.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def split_merge(image):
    '''Realize image split and merge'''
    (ch_b, ch_g, ch_r) = cv2.split(image)
    cv2.imshow("Red", ch_r)
    cv2.imshow("Green", ch_g)
    cv2.imshow("Blue", ch_b)

    merged = cv2.merge([ch_b, ch_g, ch_r])
    cv2.imshow("Merged", merged)

    zeros = np.zeros(image.shape[:2], dtype="uint8")
    cv2.imshow("Red", cv2.merge([zeros, zeros, ch_r]))
    cv2.imshow("Green", cv2.merge([zeros, ch_g, zeros]))
    cv2.imshow("Blue", cv2.merge([ch_b, zeros, zeros]))

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    split_merge(image)


if __name__ == "__main__":
    main()
