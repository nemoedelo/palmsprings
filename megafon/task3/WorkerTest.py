import unittest

from megafon.task3.Position import Position


class WorkerTest(unittest.TestCase):
    def test_something(self):
        worker = Position("Elena", "Kulagina", 100000, 30000)
        self.assertEqual(worker.get_full_name(), "Elena Kulagina")
        self.assertEqual(worker.get_total_income(), 130000)


if __name__ == '__main__':
    unittest.main()
