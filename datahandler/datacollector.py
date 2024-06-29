import cv2
import numpy as np

from drawer.draw_box import DrawBox

class DataCollector:
    def __init__(self, mode, options):
        self.image = None
        self.label = None
        self.pcd = None
        self.drawer = DrawBox(mode)
        self.options = options

    def __call__(self, image, label, pcd):
        self.image = image
        self.label = label
        self.pcd = pcd

        result = []

        for opt in self.options:
            if opt == "box":
                result.append(self.drawer.draw_box(self.image, self.label))
        
        return result
