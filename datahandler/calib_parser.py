import numpy as np

class CalibParser:
    def __init__(self):
        self.calib_data = {"camera_matrix": None, "velo2cam": None}

    def __call__(self, calib_file):
        with open(calib_file) as f:
            lines = f.readlines()
            for line in lines:
                key = line.split(":")[0]
                if(key == "P2"):
                    self.calib_data["camera_matrix"] = line.split(":")[1][:-1]
                elif(key == "Tr_velo_to_cam"):
                    self.calib_data["velo2cam"] = line.split(":")[1][:-1]
        
        self.set_matrix()
        return self.calib_data

    def set_matrix(self):
        i_mat = np.eye(4)
        for key, value in self.calib_data.items():
            i_mat[:3] = np.array(self.calib_data[key][1:].split(" ")).reshape(3, -1).astype(np.float32)
            self.calib_data[key] = i_mat
            i_mat = np.eye(4)
