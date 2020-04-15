import unittest

from megafon.task4.SportCar import SportCar


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sport_car = SportCar(100, "red", "jaguar")
        self.assertRaises(ValueError, sport_car.show_speed)
        sport_car.stop()
        self.assertEqual(sport_car.show_speed(), 0)


if __name__ == '__main__':
    unittest.main()
