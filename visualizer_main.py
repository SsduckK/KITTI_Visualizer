import config as cfg

from datahandler import DataLoader
from datahandler import LabelParser

def main():
    path = cfg.DATA_PATH
    DL = DataLoader(path)
    LP = LabelParser("2D")
    instance = LP(DL[2]["label"])
    print(instance)

if __name__ == "__main__":
    main()

