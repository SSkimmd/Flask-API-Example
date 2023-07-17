class Item(dict):
    def __init__(self, name, description):
        dict.__init__(self, name=name, description=description)