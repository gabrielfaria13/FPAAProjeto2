import unittest
from main import maxmin_select

class TestMaxMinSelect(unittest.TestCase):
    def test_single_element(self):
        arr = [5]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (5, 5))

    def test_two_elements(self):
        arr = [3, 7]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (3, 7))

    def test_multiple_elements(self):
        arr = [3, 1, 8, 5, 2, 9, 4, 7]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (1, 9))
    
    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (1, 8))

    def test_reverse_sorted_list(self):
        arr = [8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (1, 8))

if __name__ == "__main__":
    unittest.main()
