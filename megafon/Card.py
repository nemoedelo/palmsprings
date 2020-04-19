class Card:

    def __init__(self, line_1, line_2, line_3, name):
        """3 строки по 9 клеток"""
        self.line_1 = line_1
        self.line_2 = line_2
        self.line_3 = line_3
        self.name = name

    def is_winner(self):
        result = self.check(self.line_1) and self.check(self.line_2) and self.check(self.line_3)
        if result:
            print(f"{self.name} is winner!")
        return result

    def check(self, line):
        for num in line:
            if num is None:
                continue
            if not num.chosen:
                return False
        return True

    def find_val(self, line, value_to_find):
        for num in line:
            if num is None:
                continue
            if num.val == value_to_find:
                return num
        else:
            return None

    def handle_round(self, new_number):
        optional_number = self.find_val(self.line_1 + self.line_2 + self.line_3, new_number)
        if optional_number is not None:
            optional_number.flip()
            print(f"Found number: {optional_number.val}")
        return optional_number

    def __str__(self):
        result = ""
        result += self.print_line(self.line_1)
        result += self.print_line(self.line_2)
        result += self.print_line(self.line_3)
        return result

    def print_line(self, line):
        result = ""
        for n in line:
            if n is None:
                result += "   "
            elif n.chosen is True:
                result += "-- "
            else:
                result += str(n.val).rjust(3)
        result += "\n"
        return result
