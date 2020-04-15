class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = self.speed + 10

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        print("The car turned", direction)

    def show_speed(self):
        return self.speed
