#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:45:51 2020

@author: j-bd
"""

import argparse

import cv2
import numpy as np
from matplotlib import pyplot as plt


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Histogram with mask",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 histogram_with_mask.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def plot_histogram(image, title, mask=None):
    '''Computes a histogram for each channel in the image and plots it'''
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("Numbers of Pixels")

    for (idx, color) in enumerate(colors):
        hist = cv2.calcHist([image], [idx], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

def mask_creation(image):
    '''Create a predefined mask and applied it to an image'''
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(mask, (273, 106), (445, 362), 255, -1)
    cv2.imshow("Mask", mask)

    masked = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Applying the Mask", masked)
    return mask

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)
    plot_histogram(image, "Histogram for Original Image")

    mask = mask_creation(image)
    plot_histogram(image, "Histogram for Masked Image", mask=mask)


if __name__ == "__main__":
    main()
