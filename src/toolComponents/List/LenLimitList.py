# -*- utf-8 -*-
class LenLimitList:
    def __init__(self, _maxlen=20, interable=()):
        self.maxlen = _maxlen
        self.data = [x for x in interable]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return self.data.__str__()

    def __getitem__(self, key):
        return self.data[key]

    def keys(self):
        return self.data.k
    def pop(self, index) -> None:
        self.data.pop(index)

    def append(self, value) -> None:
        if self.__len__() < self.maxlen:
            self.data.append(value)
            return
        else:
            self.data = self.data[1:]
            self.data.append(value)