class LabelParser:
    def __call__(self, label):
        parsed_label = self.parse_label(label)
        return parsed_label

    def parse_label(self, label):
        with open(label) as f:
            lines = f.readlines()
            for line in lines:
                print(line)
