class Cell:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def validate(self, obj):
        if not isinstance(obj, Cell):
            raise ValueError("It's not allowed to use operators on other types")

    def __add__(self, other):
        self.validate(other)
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        self.validate(other)
        if (other.cell_count >= self.cell_count):
            self.cell_count -= other.cell_count

    def __mul__(self, other):
        self.validate(other)
        return Cell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        self.validate(other)
        return Cell(self.cell_count // other.cell_count)

    def make_order(self, line_size):
        result = ""
        quantity = self.cell_count
        while quantity >= line_size:
            for _ in range(0, line_size):
                result += "*"
                quantity -= 1
            result += "\n"
        for _ in range(0, quantity):
            result += "*"

        return result
