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
        if(self.load_data == False):
            print("Terminating Process")
            return

    def __len__(self):
        return len()

    def __getitem__(self, idx):
        return {"image": self.images[idx], "label": self.labels[idx], "pcd": self.point_clouds[idx]}

    def load_data(self, path):
        image_sequences = glob(op.join(path, "data_object_image_2", "training", "image_2", "*.png"))
        pcd_sequences = glob(op.join(path, "data_object_velodyne", "training", "velodyne", "*.bin"))
        label_sequences = glob(op.join(path, "data_object_label_2", "training", "label_2", "*.txt"))
        print(f"image : {len(image_sequences)}, pcd : {len(label_sequences)}, pcd : {len(pcd_sequences)}")
        if(len(image_sequences) == len(pcd_sequences) == len(label_sequences)):
            self.images = image_sequences
            self.point_clouds = pcd_sequences
            self.labels = label_sequences
            print("data load success")
        else:
            print("data load fail")
            return False



