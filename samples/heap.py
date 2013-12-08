

class Heap(object):
    def __init__(self):
        self.array = []

    def add_elem(self, elem):
        index = len(self.array)
        self.append(elem)
        n = index


