import numpy as np
import os.path as op

from glob import glob


class DataLoader:
    def __init__(self, path):
        self.path = path
        self.images = None
        self.point_clouds = None
        self.labels = None
        self.load_data(self.path)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        return {"image": self.images[index], "point_cloud": self.point_clouds[index], "label": self.labels[index]}

    def load_data(self, path):
        image_sequences = glob(op.join(path, "data_object_image_2", "training", "image_2", "*.png"))
        pcd_sequences = glob(op.join(path, "data_object_velodyne", "training", "velodyne", "*.bin"))
        label_sequences = glob(op.join(path, "data_object_label_2", "training", "label_2", "*.txt"))
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

