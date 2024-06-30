import cv2

import config as cfg

from datahandler import DataLoader
from datahandler import LabelParser
from datahandler import PCDParser
from datahandler import DataCollector
from datahandler import CalibParser

class Visualizer:
    def __init__(self, path, vis_mode, vis_option):
        self.path = path
        self.mode = vis_mode
        self.option = vis_option

        self.DL = DataLoader(path)
        self.LP = LabelParser(self.mode)
        self.PP = PCDParser()
        self.DC = DataCollector(self.mode, self.option)
        self.CP = CalibParser()

        self.image = None
        self.label = None
        self.pcd = None
        self.calib = None

    def __len__(self):
        return len(self.DL)

    def get_data(self, idx):
        image_file = self.DL[idx]["image"]
        label_file = self.DL[idx]["label"]
        pcd_file = self.DL[idx]["point_cloud"]
        calib_file = self.DL[idx]["calib"]
        
        self.image = cv2.imread(image_file)
        self.label = self.LP(label_file)
        self.pcd = self.PP(pcd_file)
        self.calib = self.CP(calib_file)

        results =  self.DC(self.image, self.label, self.pcd)
        self.visualize(results)

    def visualize(self, results):
        for rst in results:
            cv2.imshow("bounding box image", rst)

        cv2.waitKey(0)


def main():
    data_path = cfg.DATA_PATH
    vis_mode = cfg.VIS_MODE
    vis_option = cfg.VIS_OPTION
    vis = Visualizer(data_path, vis_mode, vis_option)

    for i in range(len(vis)):
        vis.get_data(i)
    

if __name__ == "__main__":
    main()

