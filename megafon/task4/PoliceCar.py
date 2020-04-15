from megafon.task4.Car import Car


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, True)

    def show_speed(self):
        return self.speed
