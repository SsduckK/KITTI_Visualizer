import config as cfg

from dataloader import DataLoader

def main():
    path = cfg.DATA_PATH
    DL = DataLoader(path)


if __name__ == "__main__":
    main()

