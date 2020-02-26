#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:19:09 2020

@author: j-bd
"""

import argparse

import cv2
import numpy as np


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Counting coins",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 counting_coins.py
        --image "path/to/image/directory"

        All arguments are mandatory.
        '''
    )
    parser.add_argument(
        "-i", "--image", required=True, help="Path to the image"
    )
    args = vars(parser.parse_args())
    return args

def edges_detection(grayscale_image):
    '''Provide a corresponding edge image'''
    blurred = cv2.GaussianBlur(grayscale_image, (9, 9), 0)
    edged = cv2.Canny(blurred, 30, 100)
    cv2.imshow("Edged", np.hstack([grayscale_image, edged]))
    return edged

def contours_detection(grayscale_image, edged):
    '''Provide object contours'''
    contours, hierarchy = cv2.findContours(
        edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    print("I count {} coins in this image".format(len(contours)))
    coins = grayscale_image.copy()
    # we have the contour index. By specifying a negative value of − 1, we are
    # indicating that we want to draw all of the contours
    cv2.drawContours(coins, contours, -1, (0, 255, 0), 2)
    cv2.imshow("Coins", coins)
    return contours

def object_cropping(contours, image):
    '''Crop provided object'''
    for (idx, contour) in enumerate(contours):
        (x_val, y_val, w_val, h_val) = cv2.boundingRect(contour)

        print("Coin number {}".format(idx + 1))
        coin = image[y_val:y_val + h_val, x_val:x_val + w_val]
        cv2.imshow("Coin", coin)

        mask = np.zeros(image.shape[:2], dtype="uint8")
        ((center_x, center_y), radius) = cv2.minEnclosingCircle(contour)
        cv2.circle(mask, (int(center_x), int(center_y)), int(radius), 255, -1)
        mask = mask[y_val:y_val + h_val, x_val:x_val + w_val]
        cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask=mask))
        cv2.waitKey()

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)

    edged = edges_detection(cv2.imread(args["image"], 0))

    contours = contours_detection(cv2.imread(args["image"], 0), edged)

    object_cropping(contours, image)


if __name__ == "__main__":
    main()
