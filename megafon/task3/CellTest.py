import unittest

from megafon.task3.Cell import Cell


class MyTestCase(unittest.TestCase):
    def test_something(self):
        cell = Cell(22)
        print(cell.make_order(5))


if __name__ == '__main__':
    unittest.main()
