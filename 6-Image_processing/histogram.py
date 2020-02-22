#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:53:37 2020

@author: j-bd
"""

import argparse

import cv2
import numpy as np
from matplotlib import pyplot as plt


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Grayscale histogram",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 grayscale_histogram.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def grey_hist(image):
    '''Realise histogram for grey image'''
    image_g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original", image_g)

    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

def color_hist(image):
    '''Realise histogram for rgb image'''
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title("’Flattened’ Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

def color_hist2(image):
    '''Realise histogram for rgb image'''
    color = ('b', 'g', 'r')
    plt.figure()
    plt.title("’Flattened’ Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    for i, col in enumerate(color):
        histr = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    grey_hist(image)
    color_hist(image)
    color_hist2(image)


if __name__ == "__main__":
    main()
