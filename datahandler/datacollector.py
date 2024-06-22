import cv2
import numpy as np

class DataCollector:
    def __init__(self):
        self.image = None
        self.label = None
        self.pcd = None

    def __call__(self, image, label, pcd):
        self.image = image
        self.label = label
        self.pcd = pcd
        

