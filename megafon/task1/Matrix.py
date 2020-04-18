class Matrix:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        result = []
        for i, row in enumerate(self.values):
            row_result = []
            result.append(row_result)
            for j, val in enumerate(row):
                row_result.append(val + other.values[i][j])
        return Matrix(result)
