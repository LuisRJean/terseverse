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