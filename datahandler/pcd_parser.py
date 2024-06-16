import numpy as np

class PCDParser:
    def __init__(self):
        self.scene_pcd = []

    def __call__(self, pcd_file):
        pcd = np.fromfile(pcd_file, dtype=np.float32)
        pcd = pcd.reshape(-1, 4)
        return pcd
