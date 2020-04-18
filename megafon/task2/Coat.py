from megafon.task2.Cloth import Cloth


class Coat(Cloth):

    def __init__(self, v):
        super().__init__(v=v)

    def calculate_cost(self):
        return self.size / 6.5 + 0.5
