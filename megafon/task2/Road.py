class Road:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def cost_in_tons(self, height, weight):
        return (height * weight * self.width * self.length) / 1000
