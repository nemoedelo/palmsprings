from megafon.task2.Cloth import Cloth


class Suit(Cloth):

    def __init__(self, h):
        super().__init__(h=h)

    def calculate_cost(self):
        return 2 * self.size + 0.3
