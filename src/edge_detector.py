#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import necessary libraries 
import os
import cv2
import argparse


# In[2]:


# filter noise, choices for filter : averaging, gaussian, median and bilateral
def filter_noise(image, filter=None):
    if filter.lower()=='averaging':
        blur_img = cv2.blur(image, (5, 5))
    elif filter.lower()=='median':
        blur_img = cv2.medianBlur(image, 5)
    elif filter.lower()=='gaussian':
        blur_img = cv2.GaussianBlur(image, (5, 5), 0)
    elif filter.lower()=='bilateral':
        blur_img = cv2.bilateralFilter(image, 5, 75, 75)
    return blur_img


# In[3]:


if __name__ == '__main__':

    # set up the argument
    parser = argparse.ArgumentParser()
    parser.add_argument('image')
    parser.add_argument('filter', default='bilateral', help='choose a filter: average, gaussian, median and bilateral')
    args, unknown = parser.parse_known_args()

    # load the image
    img_base = cv2.imread(args.image)
    
    # convert the image into gray scale
    img_gray = cv2.cvtColor(img_base, cv2.COLOR_BGR2GRAY)
 
    # filter noise 
    img_filt = filter_noise(img_gray, filter=args.filter)

    # threshold image
    _, img_thres = cv2.threshold(img_filt, 170, 255, cv2.THRESH_BINARY)

    # detect edge 
    edges = cv2.Canny(img_thres, 100, 200)

    # draw detected edges in green
    for i in range(edges.shape[0]):
        for j in range(edges.shape[1]):
            if edges[i][j] >= 70:
                img_base[i][j][0] = 0
                img_base[i][j][1] = 255
                img_base[i][j][2] = 0

    # show detected edges
    cv2.imshow("Detected Edges", img_base)


# 
