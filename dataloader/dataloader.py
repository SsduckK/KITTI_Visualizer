import numpy as np
import os.path as op

from glob import glob


class DataLoader:
    def __init__(self, path, cam_idx):
        self.path = path
        self.cam_idx = cam_idx
        self.images = None
        self.point_clouds = None
        self.labels = None
        self.load_data(self.path, self.cam_idx)

    def __len__(self):
        return len()

    def load_data(self, path, cam_idx):
        image_sequences = glob(op.join(path, "*", cam_idx, "data", "*.png"))
        pcd_sequences = glob(op.join(path, "*", "velodyne_points", "data", "*.bin"))
        label_sequences = glob(op.join(path, "*", "oxts", "data", "*.txt"))
        print(f"image : {len(image_sequences)}, pcd : {len(label_sequences)}, pcd : {len(pcd_sequences)}")
        if(self.check_valid_dataset(len(image_sequences), len(pcd_sequences), len(label_sequences))):
            self.images = image_sequences
            self.point_clouds = pcd_sequences
            self.labels = label_sequences
            print("==>DATASET CREATE SUCCESSED \ncontinue")
        else:
            print("==> DATASET CREATE FAILED \nshutdown")
            return

    def check_valid_dataset(self, images, pcds, labels):
        if(images == pcds == labels):
            return True
        else:
            False

