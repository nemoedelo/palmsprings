import unittest

from megafon.task5.Handle import Handle
from megafon.task5.Pen import Pen
from megafon.task5.Pencil import Pencil


class StationeryTest(unittest.TestCase):
    def test_something(self):
        pencil = Pencil("black")
        pencil.draw()

        pen = Pen("blue")
        pen.draw()

        handle = Handle("green")
        handle.draw()


if __name__ == '__main__':
    unittest.main()
