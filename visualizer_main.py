import config as cfg

from datahandler import DataLoader
from datahandler import LabelParser

def main():
    path = cfg.DATA_PATH
    DL = DataLoader(path)
    LP = LabelParser()
    LP(DL[1][2])

if __name__ == "__main__":
    main()

