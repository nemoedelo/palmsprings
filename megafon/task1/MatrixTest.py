import unittest

from megafon.task1.Matrix import Matrix


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = Matrix([[1, 5], [3, 4]])
        b = Matrix([[-1, -5], [-3, -4]])
        result = a + b
        self.assertEqual([[0, 0], [0, 0]], result.values)


if __name__ == '__main__':
    unittest.main()
