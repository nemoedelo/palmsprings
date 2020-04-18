from abc import abstractmethod


class Cloth:
    def __init__(self, v=None, h=None):
        self.__v = v
        self.__h = h

    @abstractmethod
    def calculate_cost(self):
        pass

    @property
    def size(self):
        if self.__v is not None:
            return self.__v
        elif self.__h is not None:
            return self.__h
        else:
            raise ValueError
