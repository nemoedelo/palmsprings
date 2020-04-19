from itertools import cycle
from random import randint

from megafon.Card import Card
from megafon.Number import Number


class CardGenerator:

    def generate_card(self, name):
        numbers = self.roll_unique(15, 1, 90)
        line_1 = self.prepare_line(numbers[0:5])
        line_2 = self.prepare_line(numbers[5:10])
        line_3 = self.prepare_line(numbers[10:15])
        return Card(line_1, line_2, line_3, name)

    def roll_unique(self, quantity, start, limit):
        used_numbers = []
        result = []
        while len(result) < quantity:
            val = randint(start, limit)
            if val in used_numbers:
                continue
            else:
                used_numbers.append(val)
                result.append(val)
        return result

    def prepare_line(self, numbers):
        indices = []
        sorted_numbers = numbers
        sorted_numbers.sort()
        result = [None for n in range(0, 9)]
        while len(indices) is not 5:
            val = randint(0, 8)
            if val in indices:
                continue
            else:
                indices.append(val)
        indices.sort()
        index_gen = cycle(indices)

        for n in sorted_numbers:
            result[next(index_gen)] = Number(n)

        return result
