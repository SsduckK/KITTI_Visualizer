class LabelParser:
    def __init__(self, mode):
        self.mode = mode

    def __call__(self, label):
        parsed_label = self.parse_label(label)
        return parsed_label

    def parse_label(self, label):
        scene_instances = []
        with open(label) as f:
            lines = f.readlines()
            for instance in lines:
                parsed_instance = self.split_elem(instance)
                scene_instances.append(parsed_instance)
        return scene_instances

    def split_elem(self, instance):
        elems = instance.split(" ")
        category = elems[0]
        if(self.mode == "2D"):
            coords = elems[4:8]
        elif(self.mode == "3D"):
            coords = elems[-7:]
            coords[-1] = coords[-1][:-1]
        else:
            print("Choose 2D/3D")
            return
        return {"category": category, "coords": coords}

