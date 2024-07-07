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
        pcd = pcd @ self.world2top.T
        pcd[:, :2] /= 0.05
        pcd[:, 0] += 320
        pcd[:, 1] += 320
        pcd = pcd.astype(np.uint8)
        valid_indices = (pcd[:, 0] >= 0) & (pcd[:, 0] < self.w) & (pcd[:, 1] >= 0) & (pcd[:, 1] < self.h)
        print(pcd[:5])
        pcd = pcd[valid_indices]
        print("asdfasdf")
        print(pcd[:5])

        print(self.base_space.shape)
        print(pcd[:, 1].shape, " " , pcd[:, 0].shape)

        self.base_space[pcd[:, 1], pcd[:, 0]] = 255
        cv2.imshow("bev", self.base_space)
        cv2.waitKey()
