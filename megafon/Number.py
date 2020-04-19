class Number:
    def __init__(self, val):
        self.val = val
        self.chosen = False

    def flip(self):
        self.chosen = True
