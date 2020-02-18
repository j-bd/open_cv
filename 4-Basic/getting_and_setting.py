#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:49:16 2020

@author: j-bd
"""
import argparse

import cv2


def arguments_parser():
    '''Retrieve user commands'''
    parser = argparse.ArgumentParser(
        prog="Pixel",
        usage='''%(prog)s [OpenCV]''',
        formatter_class=argparse.RawDescriptionHelpFormatter, description='''
        To lauch execution:
        -------------------------------------
        python3 getting_and_setting.py
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
    '''Display image'''
    image = cv2.imread(path)
    cv2.imshow("Image", image)
    cv2.waitKey()
    return image

def change_pix(image):
    '''Modify pixcel value'''
    (ch_b, ch_g, ch_r) = image[0, 0]
    print(f"Pixel at (0, 0) - Red: {ch_r}, Green: {ch_g}, Blue: {ch_b}")
    image[0, 0] = (0, 0, 255)
    (ch_b, ch_g, ch_r) = image[0, 0]
    print(f"Pixel at (0, 0) - Red: {ch_r}, Green: {ch_g}, Blue: {ch_b}")
    cv2.imshow("Updated", image)
    cv2.waitKey()

def change_zone(image):
    '''Modify multiple pixels'''
    corner = image[2:50, 2:50]
    cv2.imshow("Corner", corner)
    cv2.waitKey()
    image[2:50, 2:50] = (0, 255, 0)
    cv2.imshow("Updated_", image)
    cv2.waitKey()

def main():
    '''Launch main steps'''
    args = arguments_parser()

    image = display(args["image"])
    change_pix(image)
    change_zone(image)


if __name__ == "__main__":
    main()
