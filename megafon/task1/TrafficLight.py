import time
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.colors = cycle(["green", "yellow", "red"])
        self.current_state = next(self.colors)

    def print_state(self):
        print(self.current_state)

    def switch_state(self):
        if self.current_state == "red":
            time.sleep(7)
        elif self.current_state == "yellow":
            time.sleep(2)
        elif self.current_state == "red":
            time.sleep(1)
        self.current_state = next(self.colors)
