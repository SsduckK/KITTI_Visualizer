import cv2

import config as cfg

from datahandler import DataLoader
from datahandler import LabelParser
from datahandler import PCDParser
from datahandler import DataCollector


class Visualizer:
    def __init__(self, path):
        self.path = path
        self.DL = DataLoader(path)
        self.LP = LabelParser("2D")
        self.PP = PCDParser()
        self.DC = DataCollector()

        self.image = None
        self.label = None
        self.pcd = None

    def __len__(self):
        return len(self.DL)

    def get_data(self, idx):
        image_file = self.DL[idx]["image"]
        label_file = self.DL[idx]["label"]
        pcd_file = self.DL[idx]["point_cloud"]
        
        self.image = cv2.imread(image_file)
        self.label = self.LP(label_file)
        self.pcd = self.PP(pcd_file)

        return self.DC(self.image, self.label, self.pcd)


def main():
    data_path = cfg.DATA_PATH
    vis = Visualizer(data_path)
    
    for idx in range(len(vis)):
        vis.get_data(idx)


if __name__ == "__main__":
    main()

