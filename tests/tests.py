import unittest
from src.ans import can_seat

class TestCanSeat(unittest.TestCase):
    def test_can_seat(self):
        self.assertTrue(can_seat(6))
        self.assertFalse(can_seat(9))

    def test_edge_case(self):
        self.assertTrue(can_seat(8))
        self.assertFalse(can_seat(0))

    def test_large_group(self):
        self.assertFalse(can_seat(100))


if __name__ == '__main__':
    unittest.main()
