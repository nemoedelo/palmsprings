from megafon.task4.Car import Car


class WorkCar(Car):

    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            raise ValueError("The speed is too large")
        else:
            return self.speed
