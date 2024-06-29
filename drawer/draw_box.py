import cv2
import config as cfg

class DrawBox:
    def __init__(self, mode):
        self.mode = self.check_mode(mode)

    def check_mode(self, mode):
        if not ((mode != "2D") or (mode != "3D")):
            print("Choose the drawing mode 2D/3D")
        print(mode)
        return mode

    def draw_box(self, image, label):
        drawn_image = None
        if(self.mode == "2D"):
            drawn_image = self.draw_box_2d(image, label)
        elif(self.mode == "3D"):
            drawn_image = self.draw_box_3d(image, label)
        
        return drawn_image

    def draw_box_2d(self, image, label):
        image = image.copy()
        for lbl in label:
            ctgr = lbl["category"]
            coords = lbl["coords"]
            cv2.rectangle(image, (int(float(coords[0])), int(float(coords[1]))), (int(float(coords[2])), int(float(coords[3]))), cfg.CTGR_COLOR[ctgr])

        return image
    
    def draw_box_3d(self, image, label):
        print(label)

