import cv2
import numpy as np

from drawer.draw_box import DrawBox
from drawer.draw_bev import DrawBEV

class DataCollector:
    def __init__(self, mode, options):
        self.image = None
        self.label = None
        self.pcd = None
        self.box_drawer = DrawBox(mode)
        self.bev = DrawBEV()
        self.options = options

    def __call__(self, image, label, pcd):
        self.image = image
        self.label = label
        self.pcd = pcd

        result = []

        for opt in self.options:
            if opt == "box":
                result.append(self.box_drawer.draw_box(self.image, self.label))
            elif opt == "bev":
                result.append(self.bev.draw_bev(self.pcd))
        
        return result
