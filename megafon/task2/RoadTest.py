import unittest

from megafon.task2.Road import Road


class RoadTest(unittest.TestCase):
    def test_something(self):
        road = Road(20, 5000)
        self.assertEqual(road.cost_in_tons(25, 5), 12500)


if __name__ == '__main__':
    unittest.main()
