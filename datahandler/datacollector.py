import cv2
import numpy as np

class DataCollector:
    def __init__(self):
        self.image = None
        self.label = None
        self.pcd = None

    def __call__(self, image, label, pcd):
        self.image = cv2.imread(image)
        self.label = label
        self.pcd = pcd
        self.img_show()
        
    def img_show(self):
        cv2.imshow("image", self.image)
        cv2.waitKey()

