import cv2

class DrawBox:
    def __init__(self, mode):
        self.mode = self.check_mode(mode)

    def check_mode(self, mode):
        if((mode is not "2D") or (mode is not "3D")):
            print("Choose the drawing mode 2D/3D")

        return mode

    def draw_box(self, image, label):
        image_original = image.copy()


