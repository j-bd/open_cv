#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:06:29 2020

@author: j-bd
"""

import argparse

import cv2


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Otsu and Riddler thresholding",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 otsu_and_riddler.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"], 0)
    cv2.imshow("Original", image)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)


if __name__ == "__main__":
    main()
