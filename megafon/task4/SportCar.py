from megafon.task4.Car import Car


class SportCar(Car):

    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            raise ValueError("The speed is too large")
        else:
            return self.speed
