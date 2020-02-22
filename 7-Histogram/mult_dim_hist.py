#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:31:44 2020

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

def dim2_hist(image):
    '''Create an histogram based on different image channel'''
    chans = cv2.split(image)
    fig = plt.figure()

    ax = fig.add_subplot(131)
    hist = cv2.calcHist(
        [chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256]
    )
    p = ax.imshow(hist, interpolation="nearest")
    ax.set_title("2D Color Histogram for G and B")
    plt.colorbar(p)

    ax = fig.add_subplot(132)
    hist = cv2.calcHist(
        [chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256]
    )
    p = ax.imshow(hist, interpolation="nearest")
    ax.set_title("2D Color Histogram for G and R")
    plt.colorbar(p)

    ax = fig.add_subplot(133)
    hist = cv2.calcHist(
        [chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256]
    )
    p = ax.imshow(hist, interpolation="nearest")
    ax.set_title("2D Color Histogram for B and R")
    plt.colorbar(p)

    print(
        "2D histogram shape: {}, with {} values".format(
            hist.shape, hist.flatten().shape[0]
        )
    )

def dim2_hist2(image):
    '''Create an histogram based on different image channel'''
#    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
#    hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
    hist = cv2.calcHist([image], [1, 2], None, [64, 64], [0, 256, 0, 256])
    plt.imshow(hist, interpolation='nearest')
    plt.colorbar()
    plt.show()

def dim3_hist(image):
    '''Create a 3D histogram'''
    hist = cv2.calcHist(
        [image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256]
    )
    print(
        "3D histogram shape: {}, with {} values".format(
            hist.shape, hist.flatten().shape[0]
        )
    )
    plt.show()

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    dim2_hist(image)

    dim3_hist(image)


if __name__ == "__main__":
    main()
