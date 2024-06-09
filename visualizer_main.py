import config as cfg

from dataloader import DataLoader

def main():
    path = cfg.DATA_PATH
    cam_idx = cfg.CAM_IDX
    DL = DataLoader(path, cam_idx)


if __name__ == "__main__":
    main()

