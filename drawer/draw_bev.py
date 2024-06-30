import cv2
import numpy as np

import config as cfg

class DrawBEV:
    def __init__(self):
        self.w = 640
        self.h = 640
        self.base_space = self.create_base_space(self.w, self.h)
        self.world2top = self.create_w2t_mat()

    def create_base_space(self, w, h):
        base_space = np.zeros((h, w), np.uint8)
        return base_space

    def create_w2t_mat(self):
        tf_mat = np.array([[0, -1, 0, 0],
                           [0, 0, -1, 0],
                           [1, 0, 0, 0],
                           [0, 0, 0, 1]])
        return tf_mat

    def draw_bev(self, pcd):
        tf_points = pcd@self.world2top.T
        tf_points[:, 0] += self.w / 2
        tf_points[:, 1] += self.h - tf_points[:, 1]
        tf_points = np.array(tf_points, dtype=np.int64)

        valid_idx = ((tf_points[:, 0] >= 0) & (tf_points[:, 0] <= self.w) & \
                (tf_points[:, 1] >= 0) & (tf_points[:, 1] <= self.h))

        valid_points = tf_points[valid_idx]
        print(valid_points)
        cv2.imshow("bev", self.base_space)
        cv2.waitKey()
