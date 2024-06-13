import unittest

from whiteboard import solution

class MatchTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
    def test_two(self):
        self.assertEqual(solution([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
    def test_three(self):
        self.assertEqual(solution([1]), [1,0])
    def test_four(self):
        self.assertEqual(solution([]), [])
if __name__ == '__main__':
    unittest.main()












