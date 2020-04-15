import unittest

from megafon.task1.TrafficLight import TrafficLight


class TrafficLightTest(unittest.TestCase):
    def test_something(self):
        traffic_light = TrafficLight()
        self.assertEqual(traffic_light.current_state, "green")
        traffic_light.switch_state()
        self.assertEqual(traffic_light.current_state, "yellow")
        traffic_light.switch_state()
        self.assertEqual(traffic_light.current_state, "red")
        traffic_light.switch_state()
        self.assertEqual(traffic_light.current_state, "green")


if __name__ == '__main__':
    unittest.main()
