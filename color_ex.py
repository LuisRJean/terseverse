#importing the required modules
import os
import sys
import time
import numpy as np
from PIL import Image
import imp
import glob
from sklearn.cluster import KMeans
import skimage.filters as skf
import skimage.color as skc
import skimage.morphology as skm
from skimage.measure import label

class Back():
    def __init__(self, max_distance=5, use_lab=True) -> None:
        pass

    def get_background(self, image):
        # convert to grayscale
        gray = skc.rgb2gray(image)
        # apply threshold
        thresh = skf.threshold_otsu(gray)
        # apply morphology
        binary = gray > thresh
        binary = skm.binary_closing(binary, skm.disk(5))
        # label the image
        labels = label(binary)
        # get the largest label
        largest_label = np.argmax(np.bincount(labels.flat)[1:]) + 1
        # get the mask
        mask = labels == largest_label
        # apply the mask
        masked = np.zeros_like(image)
        masked[mask] = image[mask]
        return masked

        