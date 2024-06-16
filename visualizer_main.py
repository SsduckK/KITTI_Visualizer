import config as cfg

from datahandler import DataLoader
from datahandler import LabelParser
from datahandler import PCDParser
from datahandler import DataCollector


def initialize():
    path = cfg.DATA_PATH
    DL = DataLoader(path)
    LP = LabelParser("2D")
    PP = PCDParser()
    DC = DataCollector()
    return DL, LP, PP, DC


def get_data(idx, DL, LP, PP):
    image = DL[idx]["image"]
    label = DL[idx]["label"]
    label_instance = LP(label)
    pcd = DL[idx]["point_cloud"]
    scene_pcd = PP(pcd)

    return image, label_instance, scene_pcd

def main():
    data_loader, label_parser, points_parser, data_collector = initialize()
    image, label, pcd = get_data(1, data_loader, label_parser, points_parser)
    print(image, label, pcd)


if __name__ == "__main__":
    main()

