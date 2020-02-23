#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:10:50 2020

@author: j-bd
"""

import argparse

import cv2
import numpy as np
from matplotlib import pyplot as plt


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Multi-dimensional histograms",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 mult_dim_hist.py
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

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)


if __name__ == "__main__":
    main()